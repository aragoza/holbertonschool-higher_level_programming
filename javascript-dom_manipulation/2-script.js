#!/usr/bin/node

const header = document.querySelector('header');
const clickColor = document.getElementById('red_header');
clickColor.addEventListener('click', function() {
  header.classList.add('red');
});