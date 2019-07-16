# Matplotlib-Flasked version 1.0
> Here I would like to present you with a web-based interface for creating and editing Matplotlib figures. For data and other scientists!

## Installation

*Requirements:*
- Python 3: including pandas 0.23.4
- Flask: 1.0.2

*Instructions:*

1. Download the files to your local directory. For example, in my case it is **/Users/artemn9/m-f/**

**Done.** Everything is installed.

## Lauching

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
3. Go to the local address written above in your browser: e.g., http://127.0.0.1:5000/

4. You will see your browser window looking like this:
![first_load](https://uc2ef639de24d55f8595a9151614.previews.dropboxusercontent.com/p/thumb/AAc5J9VTYz7thzD9WGvc_AhtGVo9EZnJAPVEO5tqmmotW4nCjfX9uFbMI25HIYaiv54c2CEYvFrdnddLnlQaR6ZP2S3iZ4HT73zPuNzbdY8WRF6mvaiyENIKvHp7yisnJPIZSw6QZkE12GpLq2etDoivbhnZara7w9VbG_30RIZSBS9F9ziRqnii9iuCrPgB27Nx6l7hPzpGQvUmKTRcuT_t-2cRSE6LgjJzBd2kc3s0hI1H049IANioz2_xVjX7JTlU-5ZElntPdwUVuPUlfdK2tvO2i9izMGeCKrYqdJyMvr1PucAOxscnWQMnZ6Br_m_eq8Gdl2SXiM1QTVwhYAx2bRX_J1vuJHvciq8hwuZJN6geg3Te4lfqDxGua0XgloRr3obasz7cY4yTqeBbzV5UmGUyEpy7kI0xnHNiLAfNS45_Dhb9PP0T-ZuUp5pNiCP9Gn7lbzBpNu4AdZQCP7pG/p.png?fv_content=true&size_mode=5)

5. Click the button on the right "Initialize" so it changes label to "Run everything".
![initialized_window](https://uc3c301a44519d0d2dfcb407e520.previews.dropboxusercontent.com/p/thumb/AAdcPCG4Hyflf9OiNSevESLhJbF9TgiJsBqNHHi5ZCWnzF590Z_wzxZmqPXUpISZhz4azxSstc2RtnZpZKKKXwFJ5FPz6Sx_2Tr0NmdbUjfaaV9AOhREKVeTnEQFTeSr06Mn_950Nt22PCyxAbnPLUdDHcmE3sUHPy7nTP562QJK410pP6qvWcxqcWC48qMfRHhhXCUw1jofDgP3Aha4Q2Ydp4HBRoBHMJyGlnylqJkiFXYfLt_zIE3Ft2fW3VOjl845kNNjIfpE91jhuT-8fkCMiM1tekhILHesOwoP5_j0RwAMhHdeIRaFtsko4yfRxMspQdmdydjKfKZdhzz-l2bDHh_3r7eWLqvv_7-bW04lFMd97qwgXF3CY8Pu2-9t6DAf9RPSTsorH7QJsyS1rgDG-4g1Nlyhp6sHY5ihl3r_5a4j6fMjOlEytNmzHaYqmLEK9ToY8ZnkgjYK2QU4fOgr/p.png?fv_content=true&size_mode=5)

**Done.** You are ready to use it.

## Examples

1. Create a simple random dataset:

Put this code:
~~~python
columns = 'resid1 resid2 resid3 resid4 resid5'.split(' ')
df = pd.DataFrame(np.random.randn(100, 5), columns=columns)
~~~
into the "Python Code" editor box:
![example_1](https://uc70b5ba5c63cb12a2fec2a10080.previews.dropboxusercontent.com/p/thumb/AAcNT1eBLCvFIvHQMKy-LO0yMYPNQBdbkfYgPDqoR6Y0OQtF5SSHvRPwIhEF-ALoq2kHnE6VmX22vauR4xY-bVcSJoHWQphW2HAB6EYKZf4dxBE1wo3niD8NIHJPr-DtoQDEdfXwAQlf6eRPLZ4u7ONgm_LlQp2CyStq3rRbWw-_MXrnkY5t0D2GA3mjaqBl9fVJPDRvvttvB6hSVTxu2-ntjMuyBYdpCi5sXF6AkPFp5x4YVmKfisFcFlxOQH4mOQGIc7WbJA1YOBDN2I6e9Ip_CEmYNmJVXl1YUaspHg3g8J3FkMq3c4Kj-Jt3grBT4Zy-a1PJR1nWjftbjjeifA4qAGyXTkqqYx-IO2kqnbAZTX6HoznkU05Lb4DTPItphQ27lZUvJF0BXBDmpdT2pDdQwwyuf1nFa-digWyqAHZPfeTxujMtBM_52kZpPJvMhAmkmtVt_VJBc6DC1SIkPL9_/p.png?fv_content=true&size_mode=5)

Now click a green button just above the Python editor *"Run code only"*.

2. Create a simple picture describing the dataset:

Put this JSON code:

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
![example_2](https://uc899d5ad4840e79656dc54353d7.previews.dropboxusercontent.com/p/thumb/AAeEkzNOR_qym5O8Ttv7A6etGwXgj3p4VXsrcmJ28-xvn6oWEKUB_GPGiJhb-iE-XKw7HXcB_UmjgBlGp8RKFxkAkTnWytxKsA7G3nXfViOQIL2eNbLpuBz9iiXVJAcgPIQ1FagtpiutqT5FL8Gv-gcAUkXjYR6PloqYLaUkS9TnD0gZXs-rApcAmMNL1rsCpIrk9mt0_o4RafOuF1m_HmaTcO4byYc-cs0okTZldmxDD8wG2ViZ0D5v6tLPQ1CMXCYh9pw1MVKI-dyzI4_6cDFTmbBtiCkgp0765kQmHTiSHX6ZtK3e2eY-ZsVxWKnUWYKMpRCQ8rTQFCxZ_sgd5Aft7goW3LTllBALYlVuVriADPu9IiwFmfUdESnqt659StXrAEZ8-V55U3qsGdPwFGbUAW68mRSQbZ40H2QwBcVnKF1e3n9F3szBuXLOCYU_K3LeykXtiVY16blYS_hXMTY5/p.png?fv_content=true&size_mode=5)

Now click a green button just above the figure parameters editor *"Create figure only"*.

You will see the result:
![example_1_and_2](https://ucbc047b0f0d8cb881ece5c2bc1e.previews.dropboxusercontent.com/p/thumb/AAd0mos3mAtnPRaDbG55OZ6p7YrHEurB32RvPG7TIEkD9OAs9mR4QSZjyE_yMHhLgNNYKgXiXoLGNhwUWfNf-W6ZaxD3bQxM-DWLUCA8CIh_0AOubCh1wfYsruz7Hpax4jFcW8Vq9W85S50ojxAsYPdSRjyqCdQtLYxQxB3M4QRFNqvU6e53UY6Kh-DXaxJ4jgI6Smt-RRenBd8ixShq7fdtEnoq2hAVTzkpZ8geGhUJLvQgE5OL6x2bmKdawLVB4dNWvbOksCcW-K2SlTK8_vWTs4VaqV2tNAQHPyNd5Fh1v6b4fKMjX4eiSwZxz703orpXCPXYNMGQpAcvxl2FzL1zauiBK8pHZYSLw1EzF08nMdZfD3-XnL4YFt18wrFDDDVKd2LVQlnHl7ZQvhEOw3aP1VvdaPW3eyv_x33RWW3HmGxlbCtDj2oIarhAtma_RggvaxxZJ1je8_jGYc-i3SQo/p.png?fv_content=true&size_mode=5)

3. Do a more advanced picture with the same data. For example, you would like to rotate the x-tick-lables and the JSON won't give you such opportunity. What you would like to do is to run the following command:
~~~python
plt.xticks(rotation=35)
~~~
**after** the figure has been created.
In order to do this, keep the same set of JSON parameters in the "Figure Parameters" editor box, and put the code for ticks rotation in the "Python Code" editor box as follows:
![example_3](https://uc5327c8d0a0fd980ea1ff9648e4.previews.dropboxusercontent.com/p/thumb/AAcc279P77p7WMb13Wp-ewbLYbEFy--AQSxsje5DlcFRsFYuJ6qtucvJhczHAo1FhaD0swZxqfU9B9fg0PRM6o8Zx4fo9iJwRGr0u9Y06EMpRho5jc7lkPeejbBcrxYOfHcYuLmrUPmCMFxPrkEOdY-LSAcKq3J9EdGL1HrGCpOgbQjwzCZnjzrAyw5-lIBQUK3bodayMCPdjienWcuYPw_gp3sw0_IIxTtJiIvSfqb0tchw2wQFf2JajVygNwRynvbcve9RO9E1MgEFLHKgGCrGxdRpiaGHDTX8QPCA7QkqIJ3rZ5r9hC7qMGLTNCcSaUYlS7HkQk1j4e1cbk2fwUIIqlg7FpxVSC5BlTH6JJeaBmSHbVk5lQbv8N39Bc-uIz23tV0R7NnCLHqkh8HL33flkRn_01Ddin7719BYgVWRCvXi4Geqc4oT_X85YjGhCwSCYreBo4IhnBqcjbq-DvUt/p.png?fv_content=true&size_mode=5)

Then click the black button "Run everything" on the right. You will see the result:
![final_result](https://uc8ab190f207700b83eafe67214f.previews.dropboxusercontent.com/p/thumb/AAfAa-ImyZAHChXS6BaH3nHUATb92QolT5DGUN1zQJ-z1Lkqacpvx02nchHxve9QAie9iJwGWbcQdUQgu9nFofKQNppItkC-fQuhH0OOvKWKckO-GL4H8MnEBBPGQxay6aotF429JuYju4M08ySWm4TTeKUT5waJncjZcUgM1o_1igqUfPXR0sOWs8S5CBbrViabLC0Ywxl8kbUDIeUVA69y4EHCrOEIxWb-ezv7rcJXAoEO7pDkLhi5cO9sqgalMZssRAE9P1_qZ6I8FhC2dNvgomrDfHkspTYwOHatSsQhHysV3FPYEslNGziQ5mk1jyf2hg12ZBiVbDjPXSXHROtKDPvxxkvAft82sZ3IhnV9wFs7SWHTgrFQuquGfQYzMB4D1X0Nw4zZIJ97yPEnlbYdSfHFpn8lbQsDinMbB5fR0rit6D2dyCL9D2jcMN4NZkqlGSImDweklYRtU1Y0TO8E/p.png?fv_content=true&size_mode=5)

Now you can either "Save as" the result in the png format, or do anything directly to the "fig" global variable, e.g. dump it in a file to use later by putting the code below in the "Python Code" editor box and clicking the "Run code only" button:
~~~python
from pickle import dump
with open('/Users/artemn9/Desktop/figure.dump', 'wb') as f:
    dump(df, f)
~~~

## Hope you enjoy this Version 1.0

> Best Regards,
Artem Neklyudov
