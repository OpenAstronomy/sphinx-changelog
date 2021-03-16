Sphinx_Changelog v1.0.0 (2021-03-16)
====================================

No significant changes.


Sphinx_Changelog v0.1rc5 (2021-03-03)
=====================================

Bug Fixes
---------

- Do not raise exceptions inside the directive as this can cause the sphinx
  parallel build to fail. (`#8 <https://github.com/OpenAstronomy/sphinx-changelog/pull/8>`__)


Sphinx_Changelog v0.1rc4 (2021-03-02)
=====================================

Features
--------

- Add a flag to skip running towncrier if no fragment files are found. (`#6 <https://github.com/OpenAstronomy/sphinx-changelog/pull/6>`__)


Bug Fixes
---------

- Fix resolving paths relative to the file containing the changelog directive. (`#6 <https://github.com/OpenAstronomy/sphinx-changelog/pull/6>`__)


Sphinx_Changelog v0.1rc3 (2021-03-02)
=====================================

Bug Fixes
---------

- Raise a more helpful error if no towncrier config can be found. (`#5 <https://github.com/OpenAstronomy/sphinx-changelog/pull/5>`__)


Sphinx_Changelog v0.1rc2 (2021-03-01)
=====================================

Features
--------

- Implement options for changelog backend. Including the existing changelog and
  towncrier are currently available. (`#1 <https://github.com/OpenAstronomy/sphinx-changelog/pull/1>`__)


Bug Fixes
---------

- Fix use of template and update to parsing code from a newer towncrier version (`#3 <https://github.com/OpenAstronomy/sphinx-changelog/pull/3>`__)


Sphinx_Changelog v0.1rc1 (2021-03-01)
=====================================

Initial implementation copied from `sunpy <https://sunpy.org>`__.
