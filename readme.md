# Scripting environment for testing molecular dynamics engine from Concord Consortium 'lab' repository

## To get started:

Unfortunately there are two hiccups in the installation process. It is necessary to install readline by hand using easy_install instead of pip, and matplotlib must be installed *after* `pip install -r requirements.txt`

    $ python vendor/virtualenv.py script-md
    $ source script-md/bin/activate
    (script-md)$ easy_install readline
    (script-md)$ pip install -r requirements.txt
    (script-md)$ pip install matplotlib

Once the smoke test passes, install the lab repo:

    $ npm install

    (optionally)

    $ npm link <path to local installation of lab repo>

## Matplotlib smoke test:

    (script-md)$ ipython --pylab
    ...
    In [1]: x = randn(100000)

    In [2]: hist(x, 100)

You should see a histogram approximating a normal distribution.

## Example script:

Some data from the constrained random walk of the center of mass of the Lab molecular dynamics simulation is in data/. Once you have done the install steps above, to plot this data, run `./plot-cm-random-walk.py` in the root of this repository to generate the figure; open `figure/cm-random-walk.png` to view the figure.

You *may* find that you need Python 2.7 installed.
