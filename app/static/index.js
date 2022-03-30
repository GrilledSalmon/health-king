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
    .then((res)=>res.json())
    .then((result)=>{
        window.localStorage.setItem('access_token', result['access_token']);
        window.location.href='http://127.0.0.1:5000/';
        location.reload();
    });
}

// 버튼 누르면 값들 가져와서 post 요청
submit_btn.addEventListener('click', login_form_post)
