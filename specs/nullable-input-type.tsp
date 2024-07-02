import "@typespec/http";
import "@typespec/rest";


using TypeSpec.Http;
using TypeSpec.Rest;

@service({
  title: "rating storage",
})
@server("https://example.com", "Single server endpoint")
namespace Ratings;

model NamedRating {
  name: string;
  @doc("may be left out")
  rating?: integer;
}

model PatchRatingNumber {
  @doc("this one needs a value")
  rating: integer | null;
}



interface Ratings {
  op create(@body rating: NamedRating): {};
  @route("/{id}")
  @post
  op update(id: integer, @body update: NamedRating|PatchRatingNumber): {};
}

