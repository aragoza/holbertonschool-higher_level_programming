#!/usr/bin/node

const headerNode = document.querySelector('header');
const clickColor = document.getElementById('red_header');
function changeColor () {
  headerNode.style.color = '#FF0000';
}
clickColor.addEventListener('click', changeColor);
