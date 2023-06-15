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

By default it will assume the root of the repository (location of the ``pyproject.toml`` file) is up one level from the location of the rst file with the directive in it.
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
To disable towncrier output if no fragment files are found add the ``:towncrier-skip-if-empty:`` option to the directive:

.. code-block:: rst

    .. changelog::
       :towncrier: ../
       :towncrier-skip-if-empty:
       :changelog_file: ../CHANGELOG.rst

Controlling the Underline Used by towncrier
-------------------------------------------

When embedding the directive in an existing rst document you might need to adjust the heading levels used when rendering the changelog.
towncrier provides the "underlines" config option which allows you to control the characters used.
By default the 0th element in this sequence is used for the title and the following ones for the subsections.
This behaviour can be adjusted by setting the ``towncrier-title-underline-index`` option as follows:

.. code-block:: rst

    .. changelog::
       :towncrier: ../
       :towncrier-title-underline-index: 1

Note that this setting does not affect the rendered changelog, so it is probably not very useful when combined with the ``:changelog_file:`` option.

sphinx-changelog's Changelog
----------------------------

.. changelog::
   :towncrier:
   :changelog_file: ../CHANGELOG.rst
