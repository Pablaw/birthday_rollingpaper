from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from db import db
import bcrypt

rolling = Blueprint("rolling", __name__, template_folder="templates")

@rolling.route('/')
def question():
    return render_template('rollingpaper.html')

# 롤링 페이퍼 페이지 기본 정보 get
@rolling.route('/<url>')
def get_rollingpaper(url):
    print(url)

    # test 주석
    result = {'url': 'mina', 'rolling_id': 1, 'user_nickname': "mina", "cake_id": "choco"}
    message_count = db.message.count_documents({'rolling_id': 1})

    # result = db.rollingpaper.find_one({'url': url})
    # message_count = db.message.count_documents({'rolling_id': result['rolling_id']})

    print(result)
    print(message_count)

    # if(# 토큰 없을 경우 ):
    return render_template("guestMain.html", mainpage_info=result, message_count=message_count), 200

    # else: # 토큰 있을 경우
    # return render_template("rollingpaper.html", mainpage_info=result, message_count=message_count), 200

# 롤링 페이지 캔들 정보 get
@rolling.route('/detail-data/<url>/<rolling_id>')
def get_candle(url, rolling_id):
    print(type(rolling_id))
    message_list = list(db.message.find({'rolling_id': int(rolling_id)}, {'_id': False}))
    print(message_list)
    return jsonify({'message_list': message_list}), 200


# 메시지 비밀번호 확인
@rolling.route('/message/check', methods=['POST'])
def check_message_password():
    password = request.form['message_password']
    message_id = request.form['message_id']

    data = db.message.find_one({'message_id': int(message_id)}, {'_id': False})

    password2 = data['message_password']

    print(password2)

    if bcrypt.checkpw(password.encode('utf-8'), password2.encode('utf-8')):
        success = True
        message = '비밀번호 일치'
        print("일치")
    else:
        success = False
        message = '비밀번호 불일치, 다시 입력해주세요!'
        print("불일치")

    return jsonify({'success': success, 'message': message, 'data': data})



# 메시지 내용 수정
@rolling.route('/message/update', methods=['POST'])
def message_update():
    message_id_receive = request.form['message_id']
    message_content_receive = request.form['message_content']

    db.message.update_one({'message_id': int(message_id_receive)}, {'$set': {'content': message_content_receive}})
    return jsonify({'message': '수정 완료!'}), 200


# 메시지 삭제
@rolling.route('/message/removal', methods=['POST'])
def message_delete():
    message_id_receive = request.form['message_id']
    print(message_id_receive)
    db.message.delete_one({'message_id': int(message_id_receive)})

    return jsonify({'message': '삭제 완료!'}), 200

