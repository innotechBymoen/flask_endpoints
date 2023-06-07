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


app.run(debug=True)