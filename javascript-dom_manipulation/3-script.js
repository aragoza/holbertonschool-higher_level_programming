#!/usr/bin/node

const header = document.querySelector('header');
const clickColor = document.getElementById('toggle_header');
clickColor.addEventListener('click', function() {
    if (header.className === 'red'){
        header.classList.remove('red');
        header.classList.add('green');
    } else {
        header.classList.remove('green');
        header.classList.add('red');
}});