#===============================================================================
# Version 1.0. Matplotlib web-interface
#===============================================================================
"""
`main.py` implements a web-based interface for creating and editing Matplotlib figures.

Options and parameters of figures are managed by JSON data structures. JSON is easy to 
modify and resend to implement figure modify the figure. Additional python code can be sent
to do  data cleaning and more advanced manipulations with the data and figures.

Please see the documentation for the web-based interface.

The `main.py` file sets up a Flask server via the console command:

    env FLASK_APP=main:app flask run

The set of global variables are:
    - df: Pandas Dataframe storing the dataset
    - fig: Matplotlib figure generated every time the JSON is sent to the server
    - ax: Matplotlib axis stored for easier manipulation of numerious axis parameters dynamically
    
Shortcomings of Version 1.0:
    - no Exception handling (Exceptions handled by Flask and the console where it runs)
    - supports only one figure at a time (can implement a mutable list of figures later)
    - your ideas welcome! Please email me at: artem.neklyudov@gmail.com

"""

#===============================================================================
## Modules ##
#-------------------------------------------------------------------------------

# for working with data
import pandas as pd
import numpy as np

# drawing and editing the figure
import matplotlib as mpl
import matplotlib.pyplot as plt

# for the dynamic code execution
from functools import reduce

# for sending figure to the webpage
from io import BytesIO
import base64 as b64

# for the Flask server and json operations
from flask import Flask, jsonify, render_template, request
import json as js

# for storing histories of commands
from collections import deque
from pickle import dump, load


#===============================================================================
## Defaults ##
#-------------------------------------------------------------------------------

mpl.rcParams['figure.figsize'] = [8,4]
mpl.rcParams['savefig.dpi'] = 200


#===============================================================================
## GLobals ##
#-------------------------------------------------------------------------------

df = pd.DataFrame()
fig = None
ax = None

# Load code and pictures histories:
try:
    with open('code_history.pkl','rb') as f:
        codes = load(f)
except:
    codes = deque(maxlen=5000)
    pass
try:
    with open('pict_history.pkl','rb') as f:
        pictures = load(f)
except:
    pictures = deque(maxlen=5000)
    pass


#===============================================================================
## Functions ##
#-------------------------------------------------------------------------------

# Using web-inputs to create the figure
def create_figure(params):
    """
    The function creates the figure based on webpage inputs
    """
    
    # 1. Convert text inputs to a proper dictionary of graphical parameters
    original_params = params
    params = params.replace("'", "\"")
    params = js.loads(params)

    ## 1.1 evaluate parameters which have python code in them (recurvisely)
    def eval_param(params):
        """
        Sub-function implements python code evaluation feature
        """
        if type(params) is dict and len(params)>0:
            for x in params:
                if type(params[x]) is str and params[x][0:3] == '.py':
                    params[x] = eval(params[x][4:])
                    continue
                eval_param(params[x])
    eval_param(params)

    ## 1.2 Make sure the assertion tests pass
    if 'axes' not in params:
        params['axes'] = dict()
    if 'figure' not in params:
        params['figure'] = dict()
    assert len(params) == 3 # 'axes', 'figure' and the plot type

    # 2. Create new figure based on the plot type specified
    plot_kind = (set(params) - {'axes','figure'}).pop()
    f = plt.figure(**params['figure'])
    ax = f.add_subplot(1, 1, 1, **params['axes'])
    reduce(getattr, plot_kind.split("."), df)(ax=ax, **params[plot_kind])

    ## 2.1 Some of the properties may be affected when figure is filled with content
    # we re-set those in the following loop
    for prop in ('xticks',
                 'yticks',
                 'ylim',
                 'xlim',
                 'xbound',
                 'ybound',
                 'xlabel',
                 'ylabel',
                 'xscale',
                 'yscale',
                 'xticklabels',
                 'yticklabels'):
        if prop in params['axes']:
            getattr(ax, 'set_'+prop)(params['axes'][prop])

    ## 2.2 Make a nice-looking layout
    plt.tight_layout()

    # 3. Register the figure parameters in the history:
    if original_params in pictures:
        pictures.remove(original_params)
    pictures.append(original_params) # if it was there before, will appear at the beginning of the history

    return [f,ax]


def code_execute(code):
    """
    The function handles dynamic code execution.
    
    When the user asks to `print` something it returns the output of print command
    Otherwize it prints the data in the DataFrame to an html table and returns
    """
    output = df_to_html(df)

    # 1a. Handle print commands:
    if code[0:6] == 'print(':
        inside = code[6:-1]
        output = '<pre><code><xmp>' + repr(eval(inside)) + '</xmp></code></pre>'
        # print commands are not saved in the history

    # 1b. Handles other non-empty code
    elif not code == '':

        # 1.1 Execute
        exec(code, globals(), globals())
        # df could have changed after code execution, so once again:
        output = df_to_html(df)

        # 1.2 Register the code in history:
        if code in codes:
            codes.remove(code)
        codes.append(code) # if it was there before, will appear at the beginning of the history

    return output


def df_to_html(df):
    """
    Returns the html representation of the dataset
    
    Minor Tweak: You can change here how many rows/columns you would like to see.
    """
    if len(df) > 0:
        return df.to_html(max_rows=10,max_cols=9)
    else:
        return ''


def covert_figure(fig):
    """
    Converts a figure to png
    """
    # 1. Creates a buffer for the figure in png format
    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    
    # 2. Converts to base64 representation to enter the html <img> tag later
    image = b64.b64encode(buffer.read()).decode('ascii').replace('\n','')

    return 'data:image/png;base64,' + image


def code_h_format(what):
    """
    Converts content of code/pictures history to an html form
    
    Minor Tweak: You can change the html tags however you like.
    Another Tweak: Can change the length of displayed history (100 currently)
    """
    if len(what) == 0:
        return ''
    res = '<ul>'
    # pick the last 100 (note deque does not support [-100:] slicing)
    for lines in (what[-1-x] for x in range(100) if len(what)>x):
        res += '<li><pre><code>'
        res += lines
        res += '</code></pre></li>'
    res += '</ul>'
    return res


#===============================================================================
## Execution ##
#-------------------------------------------------------------------------------

# 1. Build a flask application
app = Flask(__name__)

# 2. Use the html page template
@app.route('/', defaults={'js': 'index'})
def index(js):
    return render_template('{0}.html'.format(js), js=js)

# 3. Specify the Ajax-based response function
@app.route('/process', methods=['POST'])
def process():
    """
    The main function which responds to the html form submission.
    
    The Flask server has it under the /process address.
    """

    # 1. Obtain inputs from the webpage
    code = request.form.get('Python_Code', '', type=str)
    graph = request.form.get('Figure_Parameters', '', type=str)

    if graph == '' or len(df) == 0:

        # 1a. Execute the code
        output = code_execute(code)

        # 2a. Return an 'empty' picture
        result = jsonify(src='data:image/png;base64,',
                         params=js.dumps(dict()),
                         repr=output,
                         codes=code_h_format(codes),
                         graphs=code_h_format(pictures),
                         slide=1)

    else:

        # 1b. Create a picture
        global fig, ax
        f, ax = create_figure(graph)
        fig = f

        # 2b. Execute additional code (after creating the picture):
        output = code_execute(code)

        # 3b. Convert figure and return
        fig_png = covert_figure(f)
        params = {}
        params['figure'] = {'dpi': f.dpi,
                            'frameon': f.frameon,
                            'facecolor': f.get_facecolor(),
                            'edgecolor': f.get_edgecolor(),
                            'figsize': [f.get_figwidth(), f.get_figheight()]}
        params['axes'] = {'xticks': [float(_) for _ in ax.get_xticks()],
                          'xticklabels': [_.get_text() for _ in ax.get_xticklabels()],
                          'xlim': [float(_) for _ in ax.get_xlim()],
                          'frame_on': ax.get_frame_on()}
        result = jsonify(src=fig_png,
                         params=js.dumps(params),
                         repr=output,
                         codes=code_h_format(codes),
                         graphs=code_h_format(pictures),
                         slide=0)

    return result


@app.teardown_appcontext
def teardown_db(response_or_exception):
    """
    Save code and picture history to disk
    """
    with open('code_history.pkl','wb') as f:
        dump(codes, f)
    with open('pict_history.pkl','wb') as f:
        dump(pictures, f)
