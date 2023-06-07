from flask import Flask, request
import json
import dbhelpers

app = Flask(__name__)

@app.get("/api/clients")
def get_clients():
    results = dbhelpers.run_procedure('call all_clients()', [])
    if(type(results) == list):
        return json.dumps(results, default=str)
    else:
        return "Something has gone wrong, sorry"
    
@app.get("/api/loyal_clients")
def get_loyal_clients():
    max_points = request.args.get('max_points')
    results = dbhelpers.run_procedure('call loyal_clients(?)', [max_points])
    if(type(results) == list):
        return json.dumps(results, default=str)
    else:
        return "Something has gone wrong, sorry"

@app.post("/api/clients")
def post_client():
    username = request.json.get("username")
    password = request.json.get("password")
    results = dbhelpers.run_procedure('call new_client(?,?)', [username, password])
    if(type(results) == list):
        return json.dumps(results, default=str)
    else:
        return "Something has gone wrong, sorry"

@app.delete("/api/clients")
def delete_client():
    username = request.json.get("username")
    password = request.json.get("password")
    results = dbhelpers.run_procedure('call delete_client(?,?)', [username, password])
    return json.dumps(results, default=str)


@app.patch("/api/clients")
def patch_client():
    username = request.json.get("username")
    points = request.json.get("points")
    results = dbhelpers.run_procedure('call update_points(?,?)', [username, points])
    if(type(results) == list):
        return json.dumps(results, default=str)
    else:
        return "Something has gone wrong, sorry"
    
app.run(debug=True)