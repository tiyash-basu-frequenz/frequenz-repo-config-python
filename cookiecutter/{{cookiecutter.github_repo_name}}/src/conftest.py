# License: {{cookiecutter.license}}
# Copyright © {% now 'utc', '%Y' %} {{cookiecutter.author_name}}

"""Validate docstring code examples.

Code examples are often wrapped in triple backticks (```) within docstrings.
This plugin extracts these code examples and validates them using pylint.
"""

from frequenz.repo.config.pytest import examples
from sybil import Sybil

pytest_collect_file = Sybil(**examples.get_sybil_arguments()).pytest()
