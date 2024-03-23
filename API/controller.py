from flask import Blueprint
from myapp import app
from API.services import create, get, update, delete


nhan_vien = Blueprint("nhan_vien", __name__)

@nhan_vien.route('/create_nv', methods=['POST'])
def them_nhan_vien():
    du_lieu_bang_nhan_vien = ('ten', 'so_dien_thoai', 'vai_tro')
    sqlQuery = 'INSERT INTO nhan_vien(ten, so_dien_thoai, vai_tro) VALUES(%s, %s, %s)'
    return create(du_lieu_bang_nhan_vien,sqlQuery)

@nhan_vien.route('/get_nv', methods=['GET'])
def tim_nhan_vien():
    sqlQuery = 'SELECT ten FROM nhan_vien'
    return get(sqlQuery)

@nhan_vien.route('/update_nv', methods=['PUT'])
def update_nhan_vien():
    du_lieu_bang_nhan_vien = ( 'ten', 'so_dien_thoai', 'vai_tro', 'id')
    sqlQuery = 'UPDATE nhan_vien SET ten =%s, so_dien_thoai =%s, vai_tro=%s WHERE id =%s'
    return update(du_lieu_bang_nhan_vien, sqlQuery)

@nhan_vien.route('/delete_nv', methods=['DELETE'])
def delete_nhan_vien_by_name():
    sqlQuery = 'DELETE FROM nhan_vien WHERE ten = "Dung" '
    return delete(sqlQuery)