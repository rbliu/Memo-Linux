_scarlet_ is designed to deblend sources in astrophysical images. It can handle multi-band inputs and generate a model for each deblended child.

# Installation

To install _scarlet_ on `ghk1`, I take advantage of the existing __DMstack__ environment (eg. miniconda) to deploy the dependencies.

```
# on ghk1, bash
$ cd /export/rliu/DM_14_0
$ source loadLSST.bash
$ setup lsst_distrib
```

First, install the dependencies and python packages that would be useful:
```
$ pip install ipython
$ pip install pybind11
$ pip install proxmin
$ pip install fitsio
$ pip install sep

$ git clone git://github.com/requests/requests.git
$ cd requests
$ pip install .
```

Then, build _scarlet_ from source:
```
$ git clone https://github.com/fred3m/scarlet.git
$ cd scarlet
$ python setup.py install
```

And it should be ready to use:
```
$ ipython
$ import scarlet
```


# Reference links
* scarlet.readthedocs.io
* docs.python-requests.org
