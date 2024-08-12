"""
Broken Examples Home

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 0.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from pydantic import BaseModel, ValidationError, field_validator
from oapi_codegen.confused_values.models.more_values import MoreValues
from oapi_codegen.confused_values.models.more_values_refext import MoreValuesRefext
from oapi_codegen.confused_values.models.values import Values
from typing import Any, TYPE_CHECKING
from typing import Self

PASSMENICEVALUES_ANY_OF_SCHEMAS = ["MoreValues", "MoreValuesRefext", "Values"]


class PassMeNiceValues(BaseModel):
    """
    more-values is matched first
    """

    # data type: MoreValuesRefext
    anyof_schema_1_validator: MoreValuesRefext | None = None
    # data type: MoreValues
    anyof_schema_2_validator: MoreValues | None = None
    # data type: Values
    anyof_schema_3_validator: Values | None = None
    if TYPE_CHECKING:
        actual_instance: MoreValues | MoreValuesRefext | Values | None = None
    else:
        actual_instance: Any = None
    any_of_schemas: set[str] = {"MoreValues", "MoreValuesRefext", "Values"}

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError(
                    "If a position argument is used, only 1 is allowed to set `actual_instance`"
                )
            if kwargs:
                raise ValueError(
                    "If a position argument is used, keyword arguments cannot be used."
                )
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator("actual_instance")
    def actual_instance_must_validate_anyof(cls, v):
        instance = PassMeNiceValues.model_construct()
        error_messages = []
        # validate data type: MoreValuesRefext
        if not isinstance(v, MoreValuesRefext):
            error_messages.append(
                f"Error! Input type `{type(v)}` is not `MoreValuesRefext`"
            )
        else:
            return v

        # validate data type: MoreValues
        if not isinstance(v, MoreValues):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MoreValues`")
        else:
            return v

        # validate data type: Values
        if not isinstance(v, Values):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Values`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError(
                "No match found when setting the actual_instance in PassMeNiceValues with anyOf schemas: MoreValues, MoreValuesRefext, Values. Details: "
                + ", ".join(error_messages)
            )
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[MoreValuesRefext] = None
        try:
            instance.actual_instance = MoreValuesRefext.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[MoreValues] = None
        try:
            instance.actual_instance = MoreValues.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # anyof_schema_3_validator: Optional[Values] = None
        try:
            instance.actual_instance = Values.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError(
                "No match found when deserializing the JSON string into PassMeNiceValues with anyOf schemas: MoreValues, MoreValuesRefext, Values. Details: "
                + ", ".join(error_messages)
            )
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(
            self.actual_instance.to_json
        ):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict[str, Any] | MoreValues | MoreValuesRefext | Values | None:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(
            self.actual_instance.to_dict
        ):
            return self.actual_instance.to_dict()
        else:
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())
