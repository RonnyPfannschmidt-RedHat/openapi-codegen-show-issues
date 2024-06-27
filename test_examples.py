from typing import Any, Protocol
import example.models as oapi_codegen_models
import model_codegen as datamodel_gen_models
import pytest


type RootModel = oapi_codegen_models.PassMe | datamodel_gen_models.PassMe


class Loader(Protocol):
    def __call__(self, **data: object) -> RootModel: ...


def load_oapi_model(**data: object) -> oapi_codegen_models.PassMe:
    return oapi_codegen_models.PassMe(**data)


def load_oapi_root(**data: Any) -> oapi_codegen_models.PassMe:
    return oapi_codegen_models.PassMe.from_dict(data)


def load_model(**data: Any) -> datamodel_gen_models.PassMe:
    return datamodel_gen_models.PassMe(**data)


@pytest.mark.parametrize("input_data", ["1234", "here", "not"])
@pytest.mark.parametrize("loader", [load_oapi_model, load_oapi_root, load_model])
def test_fun_str(loader: Loader, input_data: str):
    loaded = loader(mangled_string=input_data)
    print(loaded)
    assert False
