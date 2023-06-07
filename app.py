from flask import Flask
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

app.run(debug=True)