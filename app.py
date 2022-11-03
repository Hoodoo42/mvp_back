from site import check_enableusersite
from typing import Optional
from click import option
from dbcreds import production_mode
import dbhelpers as dbh
from flask import Flask, request, make_response
import apihelpers as apih
import json
from flask_cors import CORS
from uuid import uuid4

app = Flask(__name__)
CORS(app)

# @app.patch('/api/gamer')
# def update_gamer():

        
if (production_mode == True):
    print("Running in Production Mode")
    importbjoern# type: ignore
    bjoern.run(app, "0.0.0.0", 5042)
else:
    from flask_cors import CORS
    CORS(app)
    print("Running in Testing Mode!")
    app.run(debug=True)