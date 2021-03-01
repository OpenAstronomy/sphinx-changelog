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

By default it will assume the root of the repository (location of the ``pyproject.toml`` file) is up one leve from the location of the rst file with the directive in it.
This makes the default equivalent to:

.. code-block:: rst

    .. changelog:: ../

You can specify any relative path to the root of the repository.


sphinx-changelog's Changelog
############################

.. changelog:: ../
