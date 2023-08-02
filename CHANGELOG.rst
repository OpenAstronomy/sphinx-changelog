Sphinx_Changelog 1.4.1 (2023-08-02)
===================================

Bug Fixes
---------

- Fix opening towncrier templates. (`#21 <https://github.com/OpenAstronomy/sphinx-changelog/pull/21>`__)


Sphinx_Changelog 1.4.0 (2023-08-02)
===================================

Features
--------

- The ``towncrier`` version is now pinned to a specific version in ``sphinx_changelog`` dependencies. (`#17 <https://github.com/OpenAstronomy/sphinx-changelog/pull/17>`__)
- Update supported version of towncrier to 23.6. (`#20 <https://github.com/OpenAstronomy/sphinx-changelog/pull/20>`__)


v1.3.0 (2023-03-01)
===================

Notes
-----

This release pins the version of towncrier to 22.12.0, this is because we rely on private API in towncrier, so changes are needed on every release.

Changes
-------

- Update to towncrier 22.12.0, and other fixes by @dstansby in https://github.com/OpenAstronomy/sphinx-changelog/pull/17
- Migrate to github actions by @Cadair in https://github.com/OpenAstronomy/sphinx-changelog/pull/18

New Contributors
----------------

- @dstansby made their first contribution in https://github.com/OpenAstronomy/sphinx-changelog/pull/17


v1.2.0 (2022-08-31)
===================

Notes
-----

This release requires towncrier 22.8.0

Changes
-------
* docs: Fix typo in level by @jmartens in https://github.com/OpenAstronomy/sphinx-changelog/pull/13
* Fix for removed `top_line` argument in towncrier renderer by @ConorMacBride in https://github.com/OpenAstronomy/sphinx-changelog/pull/14

New Contributors
----------------

* @jmartens made their first contribution in https://github.com/OpenAstronomy/sphinx-changelog/pull/13
* @ConorMacBride made their first contribution in https://github.com/OpenAstronomy/sphinx-changelog/pull/14

**Full Changelog**: https://github.com/OpenAstronomy/sphinx-changelog/compare/v1.1.2...v1.2.0


Sphinx_Changelog v1.1.2 (2021-08-19)
====================================

Bug Fixes
---------

- Explicitly specify encoding when writing changelog. (`#11 <https://github.com/OpenAstronomy/sphinx-changelog/pull/11>`__)
- Fixed rendering to match towncrier, which means that top_line should not be included in the template. (`#12 <https://github.com/OpenAstronomy/sphinx-changelog/pull/12>`__)


Sphinx_Changelog v1.1.1 (2021-05-14)
====================================

Bug Fixes
---------

- Re-implement the ``:towncrier-skip-if-empty:`` flag as it was dropped in the upgrade to 21.3. (`#10 <https://github.com/OpenAstronomy/sphinx-changelog/pull/10>`__)


Sphinx_Changelog v1.1.0 (2021-05-11)
====================================

No significant changes.


Sphinx_Changelog 1.1.0rc1 (2021-05-11)
======================================

Features
--------

- Update to support only the latest release of towncrier as there were some substantial changes. (`#9 <https://github.com/OpenAstronomy/sphinx-changelog/pull/9>`__)
- Added support for controlling the title underline used by towncrier in the changelog directive. (`#9 <https://github.com/OpenAstronomy/sphinx-changelog/pull/9>`__)


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
