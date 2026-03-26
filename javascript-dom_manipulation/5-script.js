#!/usr/bin/node

document.getElementById('update_header').addEventListener('click', function() {
    const newItem = document.createElement('header');
    newItem.textContent = 'New Header!!!';
    document.querySelector('header').replaceWith(newItem);
});