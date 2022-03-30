'use strict';

// modal box
const modal = document.querySelector('.login-form');

const showModal = () => {
    modal.style.display='block';
}
const hideModal = () => {
    modal.style.display='none';
}

// close버튼
const close_btn = document.querySelector('.close-btn');
close_btn.addEventListener('click', hideModal);

const token =  localStorage.getItem('access_token');
const login_btn = document.querySelector('#login-btn');
if (!token){
    // 로그인 버튼
    login_btn.addEventListener('click', showModal);
} else {
    login_btn.textContent='로그아웃';
    login_btn.addEventListener('click',()=>{
        window.localStorage.removeItem('access_token');
        location.reload();
    })
}


// 제출 버튼
const submit_btn = document.querySelector('#login-submit');

const login_form_post = () => {
    fetch(
        'http://127.0.0.1:5000/login',{
            method:'post',
            headers: {
                'Accept':'application/json',
                'Content-Type':'application/json;charset=utf-8'
            },
            body:JSON.stringify({
                'user-id': modal.querySelectorAll('input')[0].value,
                'user-pw': modal.querySelectorAll('input')[1].value,
            })
        }
    )
    .then((res)=>{
        if (res.status == 404){
            alert('아이디가 틀렸습니다!')
        } else if (res.status == 403) {
            alert('비밀번호가 틀렸습니다!')
        } else {
            const result = res.json()
            window.localStorage.setItem('access_token', result['access_token']);
            window.location.href='http://127.0.0.1:5000/';
            location.reload();
        }
    })
}
submit_btn.addEventListener('click', login_form_post)

let register_show = false;
const recruit_btn = document.querySelector('#recruit_button');
const register_form = document.querySelector('#recuit-box-sub');

recruit_btn.addEventListener('click', ()=>{
    if (!token) {
        alert("로그인이 필요합니다!");
        location.reload();
    } else if (token && !register_show) {
        recruit_btn.textContent='취소';
        register_form.style.display='block';
        register_show=true;
        
    } else if (token && register_show) {
        recruit_btn.textContent='모집';
        register_form.style.display='none';
        register_show=false;
    }

})
register_btn = document.querySelector('#registration');
register_btn.addEventListener('click', ()=> {
    let post_acname = $("#ac_name").val();
    let post_acmaxnum = $("#ac_maxnum").val();
    let post_time = $("#ac_time").val();
    let post_place = $("#ac_place").val();
    let post_content = $("#ac_content").val();
    $.ajax({
                    type: "POST",
                    url: "/main/registration",
                    headers: {'authorization': token},
                    data: {
                        give_acname: post_acname,
                        give_acmaxnum: post_acmaxnum,
                        give_time: post_time,
                        give_place: post_place,
                        give_content: post_content
                    },
                    success: function (response) { // 성공하면
                        if (response["result"] == "success") {
                            alert("모집 등록 성공!")
                            // 성공 시 페이지 새로고침하기
                            window.location.reload();
                        } else {
                            alert("서버 오류!")
                        }
                    }
                })

})

