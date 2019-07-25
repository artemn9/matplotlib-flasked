# Matplotlib-Flasked version 1.0
![logo](https://www.aneklyud.com/github/matplotlib-flasked-logo.png)
> Here I would like to present you with a web-based interface for creating and editing Matplotlib figures. For data and other scientists!

## Installation

*Requirements:*
- Python 3: including pandas 0.23.4
- Flask: 1.0.2

*Instructions:*

1. Download the files to your local directory. For example, in my case it is **/Users/artemn9/m-f/**

**Done.** Everything is installed.

## Launching

1. Open your command console and go to the directory with the project. For example:
~~~bash
cd "/Users/artemn9/m-f/"
~~~
2. Launch the Flask local server from within the directory. For example:
~~~bash
env FLASK_APP=main:app flask run
~~~
In my case the output is:
~~~bash
 * Serving Flask app "main:app"
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
~~~
3. In your browser go to the local address written above: e.g., http://127.0.0.1:5000/

4. You will see your browser window looking like this:
![first_load](https://www.aneklyud.com/github/screenshot_1.png)

5. Click the button on the right "Initialize" so it changes label to "Run everything".
![initialized_window](https://www.aneklyud.com/github/screenshot_1b.png)

**Done.** You are ready to use it.

## Examples

1. Create a simple random dataset:

Put this code:
~~~python
columns = 'resid1 resid2 resid3 resid4 resid5'.split(' ')
df = pd.DataFrame(np.random.randn(100, 5), columns=columns)
~~~
into the "Python Code" editor box:
![example_1](https://www.aneklyud.com/github/screenshot_2.png)

Click a green button above the Python editor *"Run code only"*.

2. Create a simple picture describing the dataset:

Put the following JSON code:

~~~python
{
'plot.bar': {
    'y': ['resid2', 'resid3', 'resid4'],
    'color': ['#6abc17','#fad206','#ff4770'],
    'alpha': 0.9,
    'grid': 0,
    'title': ".py str(\'This is my\'+\' Whatever picture\')"
},
'axes': {
    'xlim': [20,80],
    'xticks': ".py [10*x for x in range(11)]",
    'xticklabels': ".py [str(10*x)+\' obs.\' for x in range(11)]",
    'xlabel': 'Observation ids',
    'ylabel': 'Residual value'
},
'figure': {

}
}
~~~
into the "Figure Parameters" editor box:
![example_2](https://www.aneklyud.com/github/screenshot_3.png)

Click a green button above the figure parameters editor *"Create figure only"*.

**The first branch of the JSON is "plot.bar" in this example. However, you can input any plotting function "x.y or x" which can produce plots out of a DataFrame "df" as "df.x.y(...) or df.x(...)". The content of the "plot.bar" branch would be "keyword-unpacked" when calling "df.plot.bar(**kwgs)".**

You will see the result:
![example_1_and_2](https://www.aneklyud.com/github/screenshot_4.png)

*Note that you could type inline python code within your JSON values by typing ".py " (with a whitespace) in front of your inline python code. Flask server will pre-process these strings and replace them with the resulting values.*

3. Do a more advanced picture with the same data. For example, you would like to rotate the x-tick-lables and the JSON won't give you such opportunity. What you would like to do is to run the following command:
~~~python
plt.xticks(rotation=35)
~~~
**after** the figure has been created.
In order to do this, keep the same set of JSON parameters in the "Figure Parameters" editor box, and put the code for the ticks rotation in the "Python Code" editor box as follows:
![example_3](https://www.aneklyud.com/github/screenshot_5.png)

Then click the black button "Run everything" on the right. You will see the result:
![final_result](https://www.aneklyud.com/github/screenshot_5b.png)

Now you can either "Save as" the result in the png format, or do anything directly to the "fig" global variable, e.g. dump it in a file to use later by putting the code below in the "Python Code" editor box and clicking the "Run code only" button:
~~~python
from pickle import dump
with open('/Users/artemn9/Desktop/figure.dump', 'wb') as f:
    dump(fig, f)
~~~

## Hope you enjoy this Version 1.0

> Best Regards,
Artem Neklyudov
