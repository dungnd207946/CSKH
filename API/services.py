import pymysql
from pymysql.cursors import DictCursor
from myapp.templates.config import mysql
from flask import jsonify, flash, request

#NV = nhan_vien
def create(list, sqlQuery):
    try:
        data = request.json
        bindData = [data.get(item, None) for item in list]
        if None in bindData:
            return jsonify({'message': 'Missing data'}), 400
        bindData = tuple(bindData)
        if request.method =='POST':
            conn = mysql.connect()
            cursor = conn.cursor(DictCursor)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Create successfully!')
            respone.status_code = 200
            return respone
        else:
            respone = jsonify('Create fail!')
            return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def get(sqlQuery):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(DictCursor)
        cursor.execute(sqlQuery)
        dataRows = cursor.fetchall()
        respone = jsonify(dataRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def update(list, sqlQuery):
    try:
        data = request.json
        bindData = [data.get(item, None) for item in list]
        if None in bindData:
            return jsonify({'message': 'Missing data'}), 400
        bindData = tuple(bindData)
        if request.method == 'PUT':
            conn = mysql.connect()
            cursor = conn.cursor(DictCursor)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Update successfully!')
            respone.status_code = 200
            return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def delete(sqlQuery):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(DictCursor)
        cursor.execute(sqlQuery)
        conn.commit()
        respone = jsonify('Delete successfully!')
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()