# Scripting environment for testing molecular dynamics engine from Concord Consortium 'lab' repository

## To get started:

Unfortunately there are two hiccups in the installation process. It is necessary to install readline by hand using easy_install instead of pip, and matplotlib must be installed *after* `pip install -r requirements.txt`

    $ python vendor/virtualenv.py script-md
    $ source script-md/bin/activate
    (script-md)$ easy_install readline
    (script-md)$ pip install -r requirements.txt
    (script-md)$ pip install matplotlib

## Smoke test:

    (script-md)$ ipython --pylab
    ...
    In [1]: x = randn(100000)

    In [2]: hist(x, 100)

You should see a histogram approximating a normal distribution.
