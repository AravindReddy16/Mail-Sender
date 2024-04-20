let load = document.querySelector('.loading');
let open_ = document.querySelector('.open');
let close_ = document.querySelector('.close');
let info = document.querySelector('.info');

window.addEventListener('beforeunload',function() {
    load.style.display = 'flex';
});

open_.addEventListener('click',function() {
    info.style.display = 'block';
});

close_.addEventListener('click',function() {
    info.style.display = 'none';
});