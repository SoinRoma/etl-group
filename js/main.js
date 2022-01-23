particlesJS.load('particles-js', 'particles.json', function() {
});

particlesJS.load('particles-js2', 'particles.json', function() {
});


let body = $("html, body");
let scrollDown = document.querySelector('.scrollDown');

scrollDown.addEventListener('click', function () {
    body.stop().animate({scrollTop:780}, 500, 'swing');
});



