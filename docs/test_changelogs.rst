:orphan:

========================
sphinx-changelog's Tests
========================

This file tests all valid combinations of the directive.

Towncrier
#########

.. changelog::
   :towncrier:

Towncrier skip-if-empty
#######################

.. changelog::
   :towncrier:
   :towncrier-skip-if-empty:


Towncrier and rst
#################

.. changelog::
   :towncrier:
   :changelog_file: ../CHANGELOG.rst

rst
###

.. changelog::
   :changelog_file: ../CHANGELOG.rst
