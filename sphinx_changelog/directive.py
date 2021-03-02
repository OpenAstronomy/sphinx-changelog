from docutils import statemachine
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives import path, unchanged

from .towncrier import generate_changelog_for_docs

__all__ = ['ChangeLog']


class ChangeLog(Directive):
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
    }

    final_argument_whitespace = True

    def render_towncrier(self):
        config_path = self.options.get("towncrier") or "../"
        changelog = generate_changelog_for_docs(config_path)
        return statemachine.string2lines(changelog, convert_whitespace=True)

    def include_changelog(self):
        with open(self.options['changelog_file']) as fobj:
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
