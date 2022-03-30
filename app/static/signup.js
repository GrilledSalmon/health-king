let check = false;

// 아이디 중복 검사
function check_id() {
    let id = $('#input_id').val();

    $.ajax({
        type: 'POST',
        url: '/user/check',
        data: { 'id': id },
        success: function (response) {
            if (response['result'] == 'success') {
                alert(`사용 가능한 아이디입니다.`)
                check = true;
            } else {
                alert(`이미 사용중인 아이디입니다.`)
            }
        }
    });

}

// 가입하기 버튼을 누르면 동작
function postdata() {
    let id = $('#input_id').val();
    let password = $('#input_password').val();
    let password_check = $('#input_password2').val();
    let name = $('#input_name').val();

    if (!check) {
        alert('아이디 중복 여부를 확인해주세요.')
    } else if (password.length < 4) {
        alert('비밀번호의 길이는 4자 이상이어야 합니다.')
    } else if (password != password_check) {
        alert('비밀번호가 동일하지 않습니다.')
    } else {
        $.ajax({
            type: 'POST',
            url: '/user',
            data: { 'id': id, 'password': password, 'name': name },
            success: function (response) {
                if (response['result'] == 'success') {
                    alert(`가입이 완료되었습니다!`);

                    // 가입 완료 시 홈으로 보내줌
                    window.location.href = 'http://127.0.0.1:5000/'
                }
            }
        });
    }
}