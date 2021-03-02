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
from towncrier._settings import load_config


def _get_date():
    return date.today().isoformat()


def generate_changelog_for_docs(directory):
    """
    The main entry point.
    """
    directory = os.path.abspath(directory)
    config = load_config(directory)
    if config is None:
        raise ValueError(f"No vaild towncrier configuration could be found in the directory {directory}")

    curdir = os.getcwd()
    os.chdir(directory)

    print("Loading template...")
    if config["template"] is None:
        template = pkg_resources.resource_string(
            "towncrier", "templates/template.rst"
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

    fragments, _ = find_fragments(
        base_directory, config["sections"], fragment_directory, definitions
    )

    print("Rendering news fragments...")
    fragments = split_fragments(fragments, definitions)
    rendered = render_fragments(
        # The 0th underline is used for the top line
        template,
        config["issue_format"],
        fragments,
        definitions,
        config["underlines"][1:],
        config["wrap"],
    )

    project_version = get_version(
        os.path.join(directory, config["package_dir"]), config["package"]
    )

    package = config.get("package")
    if package:
        project_name = get_project_name(
            os.path.abspath(os.path.join(directory, config["package_dir"])), package
        )
    else:
        # Can't determine a project_name, but maybe it is not needed.
        project_name = ""

    project_date = _get_date()

    top_line = config["title_format"].format(
        name=project_name, version=project_version, project_date=project_date
    )
    top_line += u"\n" + (config["underlines"][0] * len(top_line)) + u"\n"

    os.chdir(curdir)
    return top_line + rendered
