particlesJS.load('particles-js', 'static/plugins/particles/particles.json', function() {
});

particlesJS.load('particles-js2', 'static/plugins/particles/particles.json', function() {
});


let body = $("html, body");
let scrollDown = document.querySelector('.scrollDown');

scrollDown.addEventListener('click', function () {
    body.stop().animate({scrollTop:780}, 500, 'swing');
});



