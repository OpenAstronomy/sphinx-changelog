"""
This module provides Utility functions for working with the towncrier
changelog.

This file is based heavily on towncrier, please see
licenses/TOWNCRIER.rst
"""
import os
import sys
from datetime import date
from pathlib import Path

if sys.version_info < (3, 10):
    import importlib_resources as resources
else:
    from importlib import resources

from towncrier._builder import (find_fragments, render_fragments,
                                split_fragments)
from towncrier._project import get_project_name, get_version
from towncrier._settings import load_config_from_options


def _get_date():
    return date.today().isoformat()


def generate_changelog_for_docs(directory, skip_if_empty=True, underline=1, build_env=None):
    """
    Generate a string which is the rendered changelog.

    Parameters
    ----------
    skip_if_empty : `bool`
        Return nothing if no entries are found.
    underline : `int`
        Controls the first underline to be used. The underline characters are
        configurable in the towncrier settings they default to ``["=", "-", "~"]``.
        This int sets the first number, so set to ``1`` to use ``-`` for the
        title and subsequent characters for subsections.
    """
    directory = os.path.abspath(directory)
    base_directory, config = load_config_from_options(directory, None)

    print("Loading template...")
    if isinstance(config.template, tuple):
        template_path = resources.files(config.template[0]).joinpath(config.template[1])
    else:
        template_path = Path(config.template)

    template = template_path.read_text()

    print("Finding news fragments...")

    definitions = config.types

    fragments, fragment_filenames = find_fragments(
        base_directory, config, strict=False
    )

    # register files as dependencies, so e.g. sphinx-autobuild works
    if build_env is not None:
        build_env.note_dependency(template_path)
        for path, _ in fragment_filenames:
            build_env.note_dependency(path)

    # Empty fragments now are an OrderedDict([('', {})])
    if skip_if_empty and not fragments.get('', True):
        return ""

    fragments = split_fragments(
        fragments, definitions, all_bullets=config.all_bullets
    )

    project_version = config.version
    if project_version is None:
        project_version = get_version(
            os.path.join(base_directory, config.package_dir), config.package
        ).strip()

    project_name = config.name
    if not project_name:
        package = config.package
        if package:
            project_name = get_project_name(
                os.path.abspath(os.path.join(base_directory, config.package_dir)),
                package,
            )
        else:
            # Can't determine a project_name, but maybe it is not needed.
            project_name = ""

    project_date = _get_date().strip()

    # Custom title formats can only be added after rendering
    render_title = False if config.title_format else True

    rendered = render_fragments(
        template,
        config.issue_format,
        fragments,
        definitions,
        config.underlines[underline+1:],
        config.wrap,
        {"name": project_name, "version": project_version, "date": project_date},
        top_underline=config.underlines[underline],
        all_bullets=config.all_bullets,
        render_title=render_title,
    )

    if not render_title:  # Prepend the custom title format
        top_line = config.title_format.format(
            name=project_name, version=project_version, project_date=project_date
        )
        rendered = "\n".join([
            top_line,
            config.underlines[underline] * len(top_line),
            rendered,
        ])

    return rendered
