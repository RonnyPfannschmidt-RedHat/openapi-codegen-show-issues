"""
Broken Examples Home

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 0.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar
from example.models.pass_me_confused_values import PassMeConfusedValues
from example.models.pass_me_mangled_string import PassMeMangledString
from example.models.pass_me_nice_values import PassMeNiceValues
from typing import Self


class PassMe(BaseModel):
    """
    PassMe
    """  # noqa: E501

    mangled_string: PassMeMangledString | None = None
    confused_values: PassMeConfusedValues | None = None
    nice_values: PassMeNiceValues | None = None
    __properties: ClassVar[list[str]] = [
        "mangled_string",
        "confused_values",
        "nice_values",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self | None:
        """Create an instance of PassMe from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of mangled_string
        if self.mangled_string:
            _dict["mangled_string"] = self.mangled_string.to_dict()
        # override the default output from pydantic by calling `to_dict()` of confused_values
        if self.confused_values:
            _dict["confused_values"] = self.confused_values.to_dict()
        # override the default output from pydantic by calling `to_dict()` of nice_values
        if self.nice_values:
            _dict["nice_values"] = self.nice_values.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of PassMe from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "mangled_string": PassMeMangledString.from_dict(obj["mangled_string"])
                if obj.get("mangled_string") is not None
                else None,
                "confused_values": PassMeConfusedValues.from_dict(
                    obj["confused_values"]
                )
                if obj.get("confused_values") is not None
                else None,
                "nice_values": PassMeNiceValues.from_dict(obj["nice_values"])
                if obj.get("nice_values") is not None
                else None,
            }
        )
        return _obj
