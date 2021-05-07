from typing import List, Dict
import simplejson as json
from flask import Flask, request, Response, redirect
from flask import render_template
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'biostatsData'
mysql.init_app(app)


@app.route('/', methods=['GET'])
def index():
    user = {'username': 'IS218 Final Project'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM biostats')
    result = cursor.fetchall()
    return render_template('index.html', title='Home', user=user, biostats=result)


@app.route('/view/<int:data_id>', methods=['GET'])
def record_view(data_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM biostats WHERE id=%s', data_id)
    result = cursor.fetchall()
    return render_template('view.html', title='View Form', data=result[0])


@app.route('/edit/<int:data_id>', methods=['GET'])
def form_edit_get(data_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM biostats WHERE id=%s', data_id)
    result = cursor.fetchall()
    return render_template('edit.html', title='Edit Form', data=result[0])


@app.route('/edit/<int:data_id>', methods=['POST'])
def form_update_post(data_id):
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('biostats_1'), request.form.get('Column_2'), request.form.get('Column_3'),
                 request.form.get('Column_4'), request.form.get('Column_5'), data_id)
    sql_update_query = """UPDATE biostats t SET t.biostats_1 = %s, t.Column_2 = %s, t.Column_3 = %s, t.Column_4 = 
    %s, t.Column_5 = %s WHERE t.id = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/biostats/new', methods=['GET'])
def form_insert_get():
    return render_template('new.html', title='New Biostat Form')


@app.route('/biostats/new', methods=['POST'])
def form_insert_post():
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('biostats_1'), request.form.get('Column_2'), request.form.get('Column_3'),
                 request.form.get('Column_4'), request.form.get('Column_5'))
    sql_insert_query = """INSERT INTO biostats (biostats_1,Column_2,Column_3,Column_4,Column_5) VALUES (%s, %s,%s, %s,%s) """
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/delete/<int:data_id>', methods=['POST'])
def form_delete_post(data_id):
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM biostats WHERE id = %s """
    cursor.execute(sql_delete_query, data_id)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/api/v1/biostats/', methods=['GET'])
def api_browse() -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM biostats')
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/biostats/<int:data_id>', methods=['GET'])
def api_retrieve(data_id) -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM biostats WHERE id=%s', data_id)
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/biostats/', methods=['POST'])
def api_add() -> str:

    content = request.json

    cursor = mysql.get_db().cursor()
    inputData = (content['biostats_1'], content['Column_2'], content['Column_3'],
                 content['Column_4'], request.form.get('Column_5'))
    sql_insert_query = """INSERT INTO biostats (biostats_1,Column_2,Column_3,Column_4,Column_5) VALUES (%s, %s,%s, %s,%s) """
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    resp = Response(status=201, mimetype='application/json')
    return resp


@app.route('/api/v1/biostats/<int:data_id>', methods=['PUT'])
def api_edit(data_id) -> str:
    cursor = mysql.get_db().cursor()
    content = request.json
    inputData = (content['biostats_1'], content['Column_2'], content['Column_3'],
                 content['Column_4'], content['Column_5'], data_id)
    sql_update_query = """UPDATE biostats t SET t.biostats_1 = %s, t.Column_2 = %s, t.Column_3 = %s, t.Column_4 = 
        %s, t.Column_5 = %s WHERE t.id = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    resp = Response(status=201, mimetype='application/json')
    return resp


@app.route('/api/v1/biostats/<int:data_id>', methods=['DELETE'])
def api_delete(data_id) -> str:
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM biostats WHERE id = %s """
    cursor.execute(sql_delete_query, data_id)
    mysql.get_db().commit()
    resp = Response(status=210, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
