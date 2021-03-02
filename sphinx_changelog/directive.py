from pathlib import Path

from docutils import statemachine
from docutils.parsers.rst.directives import flag, path, unchanged
from sphinx.util.docutils import SphinxDirective

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
    }

    final_argument_whitespace = True

    def get_absolute_path(self, apath):
        # This method returns relative and absolute paths
        _, apath = self.env.relfn2path(apath)
        return Path(apath)

    def render_towncrier(self):
        config_path = self.options.get("towncrier") or "../"
        config_path = self.get_absolute_path(config_path)
        skip_if_empty = "towncrier-skip-if-empty" in self.options
        changelog = generate_changelog_for_docs(config_path, skip_if_empty=skip_if_empty)
        return statemachine.string2lines(changelog, convert_whitespace=True)

    def include_changelog(self):
        changelog_filename = self.get_absolute_path(self.options['changelog_file'])
        if not changelog_filename.exists():
            raise ValueError(f"Can not find changelog file at {changelog_filename}")
        with open(changelog_filename) as fobj:
            return statemachine.string2lines(fobj.read(), convert_whitespace=True)

    def run(self):
        # These includes should be in reverse order (apparently)
        # the last one ends up at the top of the rendered output.
        if "changelog_file" in self.options:
            self.state_machine.insert_input(self.include_changelog(), "")

        if "towncrier" in self.options:
            self.state_machine.insert_input(self.render_towncrier(), "")

        return []


class DummyChangelog(ChangeLog):
    def run(self):
        return []


def setup(app):
    app.add_directive('changelog', ChangeLog)

    return {'parallel_read_safe': True, 'parallel_write_safe': True}
