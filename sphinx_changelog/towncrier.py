"""
This module provides Utility functions for working with the towncrier
changelog.

This file is based heavily on towncrier, please see
licenses/TOWNCRIER.rst
"""
import os
from datetime import date

import pkg_resources
from towncrier._builder import (find_fragments, render_fragments,
                                split_fragments)
from towncrier._project import get_project_name, get_version
from towncrier._settings import load_config_from_options


def _get_date():
    return date.today().isoformat()


def generate_changelog_for_docs(directory, skip_if_empty=True, underline=1):
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

    curdir = os.getcwd()
    os.chdir(base_directory)

    print("Loading template...")
    if config["template"] is None:
        template = pkg_resources.resource_string(
            "towncrier", "templates/default.rst"
        ).decode("utf8")
    else:
        with open(config["template"], "rb") as tmpl:
            template = tmpl.read().decode("utf8")

    print("Finding news fragments...")

    definitions = config["types"]

    if config.get("directory"):
        base_directory = os.path.abspath(config["directory"])
        fragment_directory = None
    else:
        base_directory = os.path.abspath(
            os.path.join(directory, config["package_dir"], config["package"])
        )
        fragment_directory = "newsfragments"

    fragments, fragment_filenames = find_fragments(
        base_directory, config["sections"], fragment_directory, definitions
    )
    fragments = split_fragments(
        fragments, definitions, all_bullets=config["all_bullets"]
    )

    project_version = config.get('version')
    if project_version is None:
        project_version = get_version(
            os.path.join(base_directory, config["package_dir"]), config["package"]
        ).strip()

    project_name = config.get('name')
    if not project_name:
        package = config.get("package")
        if package:
            project_name = get_project_name(
                os.path.abspath(os.path.join(base_directory, config["package_dir"])),
                package,
            )
        else:
            # Can't determine a project_name, but maybe it is not needed.
            project_name = ""

    project_date = _get_date().strip()

    title_format = config["title_format"] or "{name} {version} ({project_date})"
    top_line = title_format.format(
        name=project_name, version=project_version, project_date=project_date
    )

    rendered = render_fragments(
        template,
        config["issue_format"],
        top_line,
        fragments,
        definitions,
        config["underlines"][underline+1:],
        config["wrap"],
        {"name": project_name, "version": project_version, "date": project_date},
        top_underline=config["underlines"][underline],
        all_bullets=config["all_bullets"],
    )

    os.chdir(curdir)
    return rendered
