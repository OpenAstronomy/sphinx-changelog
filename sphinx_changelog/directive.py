import os
from pathlib import Path

from docutils import statemachine
from docutils.parsers.rst.directives import flag, path, unchanged
from sphinx.util.docutils import SphinxDirective
from towncrier._builder import find_fragments
from towncrier._settings import load_config_from_options

from .towncrier import generate_changelog_for_docs

__all__ = ['ChangeLog']


class ChangeLog(SphinxDirective):
    """
    Render the changelog for the current commit using towncrier.

    This directive renders all the towncrier newsfiles into your current
    documentation, this can be used to keep a rendered version of the changelog
    since your last release in your documentation.

    The directive takes one argument which is the location of your
    ``pyproject.toml`` file (towncrier configuration) relative to the
    ``conf.py`` file *not* the file in which the directive is located.
    If this argument is not specified it defaults to :file:`"../"`.

    Examples
    --------

    .. code-block:: rst

        .. changelog::
    """
    required_arguments = 0
    optional_arguments = 0
    option_spec = {
        'changelog_file': path,
        'towncrier': unchanged,
        'towncrier-skip-if-empty': flag,
        'towncrier-title-underline-index': int,
    }

    final_argument_whitespace = True

    def get_absolute_path(self, apath):
        # This method returns relative and absolute paths
        _, apath = self.env.relfn2path(apath)
        return Path(apath)

    def render_towncrier(self):
        config_path = self.options.get("towncrier") or "../"
        config_path = self.get_absolute_path(config_path)

        # to be able to discover new fragments in incremental
        # builds, the `env-before-read-docs` hook needs to know
        # which documents have changelog directives using towncrier
        # and the directory of the fragments so we register a custom
        # dict on the sphinx build env here
        if not hasattr(self.env, 'towncrier_docs'):
            self.env.towncrier_docs = {}

        self.env.towncrier_docs[self.env.docname] = config_path

        skip_if_empty = "towncrier-skip-if-empty" in self.options
        try:
            changelog = generate_changelog_for_docs(
                config_path,
                skip_if_empty=skip_if_empty,
                underline=self.options.get('towncrier-title-underline-index', 0),
                build_env=self.env,
            )
        except Exception as exc:
            raise self.severe(str(exc))
        return statemachine.string2lines(changelog, convert_whitespace=True)

    def include_changelog(self):
        changelog_filename = self.get_absolute_path(self.options['changelog_file'])
        if not changelog_filename.exists():
            raise self.severe(f"Can not find changelog file at {changelog_filename}")

        self.env.note_dependency(str(changelog_filename))
        with open(changelog_filename, encoding='utf8') as fobj:
            return statemachine.string2lines(fobj.read(), convert_whitespace=True)

    def run(self):
        # These includes should be in reverse order (apparently)
        # the last one ends up at the top of the rendered output.
        if "changelog_file" in self.options:
            self.state_machine.insert_input(self.include_changelog(), "")

        if "towncrier" in self.options:
            self.state_machine.insert_input(self.render_towncrier(), "")

        return []


def trigger_changelog_rebuild(app, env, docnames):
    """
    Check if new fragments exist to trigger a rebuild of changelog files.

    This hook is executed in the ``env-before-read-docs`` hook.
    The directive registers documents and the towncrier config in the env
    so we can here check for new files and in case we find new files,
    we trigger the recreation of the documents that include the changelog
    directive. This is done by modifying ``docnames`` inplace to add the
    docname to it.
    """
    towncrier_docs = getattr(env, "towncrier_docs", None)
    if towncrier_docs is None:
        return

    for docname, directory in towncrier_docs.items():
        # we are rebuilding this anyway, no need to check for new fragments
        if docname in docnames:
            return

        # find fragments
        base_directory, config = load_config_from_options(directory, None)
        _, fragment_filenames = find_fragments(
            base_directory, config, strict=False
        )

        # check if any of them is not tracked yet
        for fragment_file, _ in fragment_filenames:
            path = os.path.abspath(fragment_file)

            # we already know about this fragment
            if path in env.dependencies[docname]:
                continue

            docnames.append(docname)
            break


def setup(app):
    app.add_directive('changelog', ChangeLog)
    app.connect("env-before-read-docs", trigger_changelog_rebuild)
    return {'parallel_read_safe': True, 'parallel_write_safe': True}
