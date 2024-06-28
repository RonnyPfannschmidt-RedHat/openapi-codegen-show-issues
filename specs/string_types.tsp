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
namespace BrokenString;

@route("/string-example")
interface Mangled {
  get(): PassString[];
}

@pattern("here")
scalar HereBeDragons extends string;

@pattern("[0-9]{2,8}")
scalar PettyNumber extends string;

model PassString {
  @oneOf
  mangled_string_one?: PettyNumber | HereBeDragons;

  mangled_string_any?: PettyNumber | HereBeDragons
}
