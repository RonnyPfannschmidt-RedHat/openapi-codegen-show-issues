from typing import Protocol


# import model_pydantic_manual
import pytest

from oapi_codegen.broken_string.models.pass_string import PassString as PassStringOapi
from datamodel_codegen.broken_string import PassString as PassStringDG
from raw_pydantic.broken_string import PassString as PassStringRawPyDantic


type RootModel = (
    PassStringOapi | PassStringDG
    # | model_pydantic_manual.PassMe
)


def load_oapi_from_dict(**data: object) -> PassStringOapi:
    return PassStringOapi.from_dict(data)


class Loader(Protocol):
    def __call__(self, **data: object) -> RootModel: ...


@pytest.mark.parametrize(
    "input_data",
    [
        "1234",
        "here",
        pytest.param(
            "not",
            marks=[pytest.mark.xfail(strict=True, reason="'not' shouldn't match")],
        ),
    ],
)
@pytest.mark.parametrize("kind", ["mangled_string_one", "mangled_string_any"])
@pytest.mark.parametrize(
    "loader",
    [
        pytest.param(PassStringOapi, id="oapi"),
        pytest.param(load_oapi_from_dict, id="oapi.from_dict"),
        pytest.param(PassStringDG, id="datagen"),
        pytest.param(PassStringRawPyDantic, id="raw.pydantic"),
    ],
)
def test_fun_str(loader: Loader, input_data: str, kind: str) -> None:
    loaded = loader(**{kind: input_data})
    print(loaded)

    if hasattr(loaded, "to_dict"):
        print("to_dict", loaded.to_dict())
    print("model_dump", loaded.model_dump())

    print(repr(loaded))
