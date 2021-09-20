.. _installation:

Installation
============

Installation from PyPI
----------------------
dask_lsf packages are published on the `Python Package Index
<https://pypi.org/project/Sphinx/>`_.  The preferred tool for installing
packages from *PyPI* is :command:`pip`.  This tool is provided with all modern
versions of Python.

On Linux or MacOS, you should open your terminal and run the following command.

::

   (.venv) $ pip install dask_lsf


Using virtual environments
~~~~~~~~~~~~~~~~~~~~~~~~~~

When installing Sphinx using pip,
it is highly recommended to use *virtual environments*,
which isolate the installed packages from the system packages,
thus removing the need to use administrator privileges.
To create a virtual environment in the ``.venv`` directory,
use the following command.

::

   $ python -m venv .venv

Installation from source
------------------------

You can install dask_lsf directly from a clone of the `Git repository`__.  This
can be done either by cloning the repo and installing from the local clone, on
simply installing directly via :command:`git`.

::

   $ git clone  https://github.com/akarshanarora/dask_lsf
   $ cd dask_lsf
   $ pip install .

::

    $ pip install git+https://github.com/akarshanarora/dask_lsf

__  https://github.com/akarshanarora/dask_lsf
