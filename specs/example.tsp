import "@typespec/http";
import "@typespec/rest";
import "@typespec/openapi3";

using TypeSpec.Http;
using TypeSpec.Rest;
using TypeSpec.OpenAPI;

@service({
  title: "Broken Examples Home",
})
@server("https://example.com", "The service endpoint")
namespace confused_values;

@route("/value-order-matters")
interface OrderOfValues {
  get(): PassMe;
}


model PassMe {

  @doc("values is matched first no matter what")
  confused_values?: Values | MoreValues | MoreValuesRefext;

  @doc("more-values is matched first")
  nice_values?: MoreValuesRefext | MoreValues | Values;
}

model Values {
  name: string;
}

model MoreValues {
  ...Values;
  age?: integer;
}

model MoreValuesRefext extends Values {
  size?: integer;
}
