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
const close_btn = document.querySelector('.close-btn');close_btn.addEventListener('click', hideModal);



// 로그인 버튼
const login_btn = document.querySelector('.login-btn');
login_btn.addEventListener('click', showModal);