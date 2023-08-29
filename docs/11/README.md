As this is a use case demo. I would like to demonstrate how to use the library `HTTP.jl` to test the get ( method http ) in Baserow. There aren't many tutorials on the internet about `HTTP.jl`, so what I'm writing can help anyone or not. I recently wrote about this code here: [Baserow API for the Julia programming language](https://community.baserow.io/t/baserow-api-for-the-julia-programming-language/459) as demo, [Using HTTP.jl to communicate with Baserow](https://github.com/JuliaWeb/HTTP.jl/discussions/1099) as sample/demo, [community-julia-discourse]()

Maybe in the future I’ll develop some library in julia to interact with Baserow as  `HTTP.jl`. However, as my idea is to present a code demonstration that can be used by anyone here, something like this:

```julia
using HTTP;
using Pkg; 
Pkg.add("HTTP")

headers = Dict("Authorization" => "Token add-token-here")
resp = HTTP.request("GET", "https://api.baserow.io/api/database/fields/table/add-id-table/", headers)
println(resp.status)
println(String(resp.body))
```

The output of this code would be something like this:
```markdown
[ Info: Precompiling HTTP [hash-id]
Updating registry at ~/.julia/registries/General.toml
Resolving package versions…
No Changes to ~/.julia/environments/v1.8/Project.toml
No Changes to ~/.julia/environments/v1.8/Manifest.toml
200 # status http, get
[{“id”:id-dd,“table_id”:id-add,“name”:“name”,“order”:0,“type”:“text”,“primary”:true,“r> ead_only”:false,“text_default”:”"}]
julia>
```
