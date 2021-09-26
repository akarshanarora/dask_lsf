.. dask_lsf documentation master file, created by
   sphinx-quickstart on Mon Sep 20 15:09:33 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

dask_lsf documentation!
=======================

**version**: |release|

**dask_lsf** is a python library that offers  *simple* and *intuitive* APIs to launch lsf jobs from python script.
APIs are written around `DASK <https://dask.org/>`_


.. code-block:: pycon

    >>> import dask_lsf as dl

    >>> queue = 'normal'
    >>> project_id = 'dask_lsf'
    >>> memory = 40
    >>> ncores = 1
    >>> njobs = 10

    >>> cluster, client = dl.setupsystem(queue,project_id,memory,ncores,njobs)

.. seealso:: `Examples`_ on how to use Dask in a variety of situations after you have successfully linked your code to LSF.

   .. _Examples: https://examples.dask.org/

.. card:: Installation
    :link: installation
    :link-type: ref
    :class-card: sd-rounded-pill sd-shadow-lg sd-border-2 sd-text-center

    The doc contains a detailed description of
    various ways of installing dask_lsf on your system.

.. card:: API
    :link: api
    :link-type: ref
    :class-card: sd-rounded-pill sd-shadow-lg sd-border-2 sd-text-center

    The doc contains a detailed description of
    the dask_lsf API. The reference describes how the methods work and which parameters can
    be used.

.. toctree::
   :maxdepth: 1
   :caption: Contents:
   :hidden:

   installation
   dask_lsf
