"""
An implementation of JSON Schema for Python

The main functionality is provided by the validator classes for each of the
supported JSON Schema versions.

Most commonly, `validate` is the quickest way to simply validate a given
instance under a schema, and will create a validator for you.
"""

from jsonschema_core.exceptions import (
    ErrorTree, FormatError, RefResolutionError, SchemaError, ValidationError
)
from jsonschema_core._format import (
    FormatChecker,
    draft3_format_checker,
    draft4_format_checker,
    draft6_format_checker,
    draft7_format_checker,
)
from jsonschema_core._types import TypeChecker
from jsonschema_core.validators import (
    Draft7Validator,
    RefResolver,
    validate,
)

import importlib_metadata
__version__ = importlib_metadata.version("jsonschema")
