sphinx-changelog Documentation
------------------------------

Sphinx changelog is a sphinx extension to render changelogs into your documentation.
Currently it supports rendering towncrier changelogs.


To use it first put the following into your ``conf.py`` file to enable the extension::

    extensions = [
        ...
        'sphinx_changelog'
    ]


then put the following rst into your documentation:

.. code-block:: rst

    .. changelog::
       :towncrier:

By default it will assume the root of the repository (location of the ``pyproject.toml`` file) is up one leve from the location of the rst file with the directive in it.
This makes the default equivalent to:

.. code-block:: rst

    .. changelog::
       :towncrier: ../

The path should point to the root of the repository from the location of the file with the directive in it.

If you want to include the rendered changelog as well as the development one rendered by towncrier you can add the ``:changelog_file:`` option:

.. code-block:: rst

    .. changelog::
       :towncrier: ../
       :changelog_file: ../CHANGELOG.rst

The changelog file is assumed to be an ReST file, and will be included below the towncrier output.
It is possible to use just the changelog include and not towncrier.


Skipping towncrier on Release Builds
------------------------------------

If you combine the towncrier and changelog file options, when the documentation builds on a release there will be no fragments to render.
This means that towncrier will still render an empty changelog duplicating the pre-rendered header for the release.
To disable towncrier output if no fragment files are found add the ``:towncrier-skip-if-emtpy:`` option to the directive:

.. code-block:: rst

    .. changelog::
       :towncrier: ../
       :towncrier-skip-if-empty:
       :changelog_file: ../CHANGELOG.rst


sphinx-changelog's Changelog
----------------------------

.. changelog::
   :towncrier:
   :changelog_file: ../CHANGELOG.rst
