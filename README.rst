=========
TinyIndex
=========


.. image:: https://img.shields.io/pypi/v/tinyindex.svg
        :target: https://pypi.python.org/pypi/tinyindex

.. image:: https://img.shields.io/travis/dotwork/tinyindex.svg
        :target: https://travis-ci.org/dotwork/tinyindex

.. image:: https://readthedocs.org/projects/tinyindex/badge/?version=latest
        :target: https://tinyindex.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/dotwork/tinyindex/shield.svg
     :target: https://pyup.io/repos/github/dotwork/tinyindex/
     :alt: Updates


Document indexing for TinyDB. Basically ensures
deterministic (as long as there aren't any changes
to the table) yielding of documents. A very trivial
example usage:

```python
from tinyindex import Index

idx = Index(table, *keys)
for item in idx:
   ...

idx[0]
idx[0:4]
```


* Free software: MIT license
* Documentation: https://tinyindex.readthedocs.io.


Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
