# DM stack Installation

It is required to have `gcc version>=4.8` to compile DM stack. So I installed RedHat devtoolset-2 at `/opt/rh/devtoolset-2` on `ghk1`. To use it, either type or add the following to `~/.bashrc` : `source /opt/rh/devtoolset-2/enable`.

## lsstsw installation

I was using the `lsstsw` to install DM stack on `ghk1`:

* Get the `lsstsw` repository
```
bash
cd /export/rliu
git clone https://github.com/lsst/lsstsw.git
```

* Deploy and install
```
cd lsstsw
./bin/deploy
. bin/setup.sh
rebuild lsst_distrib
```

* At the end of installing, it will output a build number like `b2953`. We want to tag it as `current`
```
eups tags --clone bNNNN current
```

## Demo test

After installation, you can test DM stack with a sample using `obs_sdss`:
```
mkdir -p demo_data
cd demo_data
curl -L https://github.com/lsst/lsst_dm_stack_demo/archive/13.0.tar.gz | tar xvzf -
cd lsst_dm_stack_demo-13.0
setup obs_sdss
./bin/demo.sh --small
./bin/compare detected-sources_small.txt
```
If the output is `OK`, it means the stack is functioning correctly.

------

There are also other two methods to install DM stack: `conda` package and `newinstall.sh`. The `conda` method does NOT require root permission, so it is a good way to install on some HPC. The `newinstall.sh` method is the source installation, which requires root permission.

## conda installation

They provide some stable releases (e.g. v12.0, v13.0) as conda channels, which . But those are usually not the latest version.

* Get and update Miniconda2 (with python2)
```
wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh -O miniconda.sh
bash miniconda.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"
conda config --set always_yes yes --set changeps1 no
conda update -q conda
```

The installation path `$HOME` should be modified according to your requirement.

* Create lsst 'channel' (or package) and install
```
conda config --add channels http://conda.lsst.codes/stack/0.13.0
conda create -q -n lsst python=2.7
source activate lsst
conda install lsst-distrib
```

## newinstall.sh installation

* Create the directory and get the shell script
```
mkdir -p $HOME/lsst_stack
cd $HOME/lsst_stack
unset LSST_HOME EUPS_PATH LSST_DEVEL EUPS_PKGROOT REPOSITORY_PATH
curl -OL https://raw.githubusercontent.com/lsst/lsst/13.0/scripts/newinstall.sh
```

* Run the shell script and install DM stack
```
bash newinstall.sh
source $LSST_INSTALL_DIR/loadLSST.bash
eups distrib install -t v13_0 lsst_distrib
setup lsst_distrib
```

------

# Multi-version Management

We may need different versions of DM stack to test with different packages. Here I use the `lsstsw` installation on `ghk1` as an example.

The first part is the same (if there is already an lsstsw installation, this part can be skipped):
```
bash
cd /export/rliu
git clone https://github.com/lsst/lsstsw.git
cd lsstsw
./bin/deploy
. bin/setup.sh
```

Select a `branch` to install:
```
rebuild lsst_distrib -b 13.0
```

Here `13.0` can be any ticket or release number (e.g. `tickets/DM-9610`, `w.2017.30`, `12.1`).

Again, you will get a build number after installation (e.g. `b2954`). When you need this version, just type `setup lsst_distrib -t b2954`.

It is always a good idea to check which version is being setup (by `eups list`) before you run any command.

## Links
Some useful EUPS tutorial:

https://developer.lsst.io/build-ci/eups_tutorial.html

https://dev.lsstcorp.org/trac/wiki/EupsTutorial
