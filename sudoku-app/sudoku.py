import random
import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for,request, jsonify,Response,json
)
bp = Blueprint('sudoku', __name__, url_prefix='/')
from . import validate
from . import backtrack
import time
from . import db
from . import peter_norving

@bp.route('/')
def index():
    return render_template('sudoku/base.html')

@bp.route('/sudoku/solve/backtracking',methods=['POST'])
def solve_backtracking():
    resp = ""
    input_str = request.json['input_str']
    arr = validate.make_input_arr(input_str)
    start_time = time.time()
    solution_str = backtrack.return_solution(arr)
    execution_time = (time.time() - start_time)

    print("sol str"+solution_str)
    if(solution_str!="false"):
        data = {
            'valid'  : 'true',
            'solution_String':solution_str,
            'execution_time':str(execution_time)
        }   
        js = json.dumps(data)
        resp = Response(js, status=200, mimetype='application/json')
    else:
        data = {
            'valid'  : 'false',
        }   
        js = json.dumps(data)
        resp = Response(js, status=200, mimetype='application/json')
    return resp


@bp.route('/sudoku/solve/norving',methods=['POST'])
def solve_peter_norving():
    resp = ""
    input_str = request.json['input_str']
    print(input_str)
    start_time = time.time()
    solution_str = peter_norving.return_solution(input_str)
    execution_time = (time.time() - start_time)
    data = {
            'valid'  : 'true',
            'solution_String':solution_str,
            'execution_time':str(execution_time)
        }
    js = json.dumps(data)
           
    resp = Response(js, status=200, mimetype='application/json')
    return resp

@bp.route('/sudoku/random/generate',methods=['GET'])
def generate_random_sudoku():
    db_instance = db.get_db()
    size_table = db_instance.execute(
                'SELECT COUNT(*) FROM sudoku_pattern'
            ).fetchone()[0]
    print(size_table)
    random_id = random.randrange(1,size_table)

    random_sudoku_str = db_instance.execute(
                'SELECT pattern FROM sudoku_pattern where id=?',(int(random_id),)
            ).fetchone()[0]
    print(random_sudoku_str)
    db_instance.close()
    data = {
            'sudoku_str'  : random_sudoku_str,
        }   
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    return resp



@bp.route("/sudoku/validate",methods=['POST'])
def validate_sudoku():
    resp = ""
    input_str = request.json['input_str']
    print(input_str)
    arr = validate.make_input_arr(input_str)
    if(validate.isValidConfig(arr,9)):
        data = {
            'valid'  : 'true',
        }   
        js = json.dumps(data)
        resp = Response(js, status=200, mimetype='application/json')
    else:
        data = {
            'valid'  : 'false',
        }   
        js = json.dumps(data)
        resp = Response(js, status=200, mimetype='application/json')
    return resp