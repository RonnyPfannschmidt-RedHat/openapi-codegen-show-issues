# coding: utf-8

# flake8: noqa

"""
    rating storage

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from oapi_code_fixup.ratings.api.default_api import DefaultApi

# import ApiClient
from oapi_code_fixup.ratings.api_response import ApiResponse
from oapi_code_fixup.ratings.api_client import ApiClient
from oapi_code_fixup.ratings.configuration import Configuration
from oapi_code_fixup.ratings.exceptions import OpenApiException
from oapi_code_fixup.ratings.exceptions import ApiTypeError
from oapi_code_fixup.ratings.exceptions import ApiValueError
from oapi_code_fixup.ratings.exceptions import ApiKeyError
from oapi_code_fixup.ratings.exceptions import ApiAttributeError
from oapi_code_fixup.ratings.exceptions import ApiException

# import models into sdk package
from oapi_code_fixup.ratings.models.named_rating import NamedRating
from oapi_code_fixup.ratings.models.patch_rating_number import PatchRatingNumber
from oapi_code_fixup.ratings.models.ratings_update_request import RatingsUpdateRequest
