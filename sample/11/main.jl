using HTTP;
using Pkg; 
Pkg.add("HTTP")

headers = Dict("Authorization" => "Token add-token-here")
resp = HTTP.request("GET", "https://api.baserow.io/api/database/fields/table/add-id-table/", headers)
println(resp.status)
println(String(resp.body))
