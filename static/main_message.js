	const nav_btn = document.querySelector('.nav_btn');
	const msg = document.querySelector('#msg_id');

	const msg_content = document.querySelector('#msg_content');
	const msg_name = document.querySelector('#msg_content');
	const msg_pw = document.querySelector('#msg_content');
	const submit_btn = document.querySelector('#submit_btn');

	const candle_1 = document.querySelector('#candle_1');
	const candle_2 = document.querySelector('#candle_2');
	const candle_3 = document.querySelector('#candle_3');
	const candle_4 = document.querySelector('#candle_4');
	const candle_5 = document.querySelector('#candle_5');
	const candle_6 = document.querySelector('#candle_6');
	// const candles = document.querySelectorAll('.btn');

	$(document).ready(function () {

            loadFn();
        });
	// 통신연결 임시 확인

	const loadFn = () => {
//		$.ajax({
//			type: "GET",
//			url: "/message/save_msg",
//			data: {},
//			success: function (response) {
//
//			}
//		});
	}

	function goback () {
		location.href="http://127.0.0.1:9999";
	}

	nav_btn.addEventListener("click", goback);

	let candle_id = '';

	function sel_candle(e) {
		candle_id = e['path'][0]['id'];
	}

	candle_1.addEventListener("click", sel_candle);
	candle_2.addEventListener("click", sel_candle);
	candle_3.addEventListener("click", sel_candle);
	candle_4.addEventListener("click", sel_candle);
	candle_5.addEventListener("click", sel_candle);
	candle_6.addEventListener("click", sel_candle);

	function save_msg() {
			console.log(candle_id)
            let name = $('#msg_name').val()
            let pwd = $('#msg_pw').val()
            let content = $('#msg_content').val()

			if (candle_id == "") {
				alert("전달할 캔들을 선택해주세요");
			} else if (content == "") {
				alert("메시지를 입력해주세요");
			} else if (name == "") {
				alert("닉네임을 입력해주세요");
			} else if (pwd == "") {
				alert("비밀번호를 입력해주세요");
			} else {
				$.ajax({
                    type: "POST",
                    url: "/message/save_msg",
                    data: {msg_give: content, nick_give: name, pwd_give: pwd, candle_give: candle_id},
                    success: function (response) {
                        }
                    });
			}
	}








