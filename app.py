from dbcreds import production_mode
import dbhelpers as dbh
from flask import Flask, request, make_response
import apihelpers as apih
import json
from flask_cors import CORS
from uuid import uuid4

app = Flask(__name__)
CORS(app)

# ## GAMER
@app.get('/api/gamer')
def get_gamer():
    is_valid = apih.check_endpoint_info(request.headers, ['id'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = dbh.run_statement('CALL get_gamer(?)', [request.headers.get('id')])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps('Sorry Error', default=str), 500)     

@app.post('/api/gamer')
def gamer_signup():
    is_valid = apih.check_endpoint_info(request.json, ['username', 'password'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    token = uuid4().hex
    results = dbh.run_statement('CALL gamer_signup(?,?,?)', [request.json.get('username'), request.json.get('password'), token])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps('Sorry error', default=str), 500)  

@app.delete('/api/gamer')
def delete_gamer():
    is_valid = apih.check_endpoint_info(request.json, ['password'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = dbh.run_statement('CALL gamer_delete(?)', [request.json.get('password')])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps('Sorry error', default=str), 500)


# @app.patch('/api/gamer')
# def update_gamer():

#  ## GAMER LOGIN/LOGOUT

@app.post('/api/gamer_login')
def login_gamer():
    is_valid = apih.check_endpoint_info(request.json, ['username', 'password'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    token = uuid4().hex
    results = dbh.run_statement('CALL gamer_login(?,?,?)', [request.json.get('username'), request.json.get('password'), token])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps('sorry, error', default=str), 500) 

@app.delete('/api/gamer_login')
def logout_gamer():
    is_valid = apih.check_endpoint_info(request.headers, ['token'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = dbh.run_statement('CALL gamer_logout(?)', [request.headers.get('token')])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps('sorry, error', default=str), 500)

# ## POINTS

@app.get('/api/points')
def get_all_points():
    results = dbh.run_statement('CALL points_get')
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps('sorry, error', default=str), 500)

@app.patch('/api/points')
def update_points():
    is_valid = apih.check_endpoint_info(request.headers, ['gamer_id'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = dbh.run_statement('CALL points_update(?,?)', [request.json.get('points_input'), request.headers.get('gamer_id')])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps('sorry, error', default=str), 500)   



        
if (production_mode == True):
    print("Running in Production Mode")
    importbjoern# type: ignore
    bjoern.run(app, "0.0.0.0", 5042)
else:
    from flask_cors import CORS
    CORS(app)
    print("Running in Testing Mode!")
    app.run(debug=True)