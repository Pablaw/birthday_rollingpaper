from flask import Blueprint, render_template, request, jsonify, Flask
from db import db
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    create_access_token, create_refresh_token, jwt_required, get_jwt_identity,
)

login = Blueprint("login", __name__, template_folder="templates")

@login.route('/')
def question():
    return render_template("login.html")

# jwt 관련
@login.route("/token", methods=["POST"])
def create_token():
    user_id = request.json.get("user_id", None)
    password = request.json.get("password", None)

    if user_id != 'test' or password != 'test':
        return jsonify({'msg': '아이디나 비밀번호가 일치하지 않습니다'}), 401

    access_token = create_access_token(identity=user_id)
    refresh_token = create_refresh_token(identity=user_id)
    return jsonify(access_token=access_token, refresh_token=refresh_token), 200

