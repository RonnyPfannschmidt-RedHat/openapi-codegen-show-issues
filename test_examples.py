from typing import Any, Protocol
import example.models as oapi_codegen_models
import model_codegen as datamodel_gen_models
import model_pydantic_manual
import pytest


type RootModel = (
    oapi_codegen_models.PassMe
    | datamodel_gen_models.PassMe
    | model_pydantic_manual.PassMe
)


class Loader(Protocol):
    def __call__(self, **data: object) -> RootModel: ...


def load_oapi_model(**data: object) -> oapi_codegen_models.PassMe:
    return oapi_codegen_models.PassMe(**data)


def load_oapi_root(**data: Any) -> oapi_codegen_models.PassMe:
    return oapi_codegen_models.PassMe.from_dict(data)


def load_datagen(**data: Any) -> datamodel_gen_models.PassMe:
    return datamodel_gen_models.PassMe(**data)


def load_manual(**data: Any) -> model_pydantic_manual.PassMe:
    return model_pydantic_manual.PassMe(**data)


@pytest.mark.parametrize(
    "input_data",
    [
        "1234",
        "here",
        pytest.param(
            "not", marks=[pytest.mark.xfail(strict=True, reason="not shoultn match")]
        ),
    ],
)
@pytest.mark.parametrize(
    "loader", [load_oapi_model, load_oapi_root, load_manual, load_datagen]
)
def test_fun_str(loader: Loader, input_data: str) -> None:
    loaded = loader(mangled_string=input_data)
    print(loaded)

    if hasattr(loaded, "to_dict"):
        print("to_dict", loaded.to_dict())
    print("model_dump", loaded.model_dump())

    pytest.fail(repr(loaded))
