import "@typespec/http";
import "@typespec/rest";
import "@typespec/openapi3";

using TypeSpec.Http;
using TypeSpec.Rest;

@service({
  title: "Broken Examples Home",
})
@server("https://example.com", "The service endpoint")
namespace IssueExamples;

@route("/examples")
interface Pets {
  list(): PassMe[];
}

@pattern("here")
scalar HereBeDragons extends string;

@pattern("[0-9]{2-8}")
scalar PettyNumber extends string;

model PassMe {
  mangled_string: PettyNumber | HereBeDragons;

  @doc("values is matched first no matter what")
  confused_values: Values | MoreValues | MoreValuesRefext;

  @doc("more-values is matched first - it may also match if the schema does")
  nice_values: MoreValuesRefext | MoreValues | Values;
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
