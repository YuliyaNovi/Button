window.onscroll = function() { scrollFunction() };

functions crollFunction() {
    if(document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
    document.getElementByID("top-btn").style.display = "block";
    } else {
        document.getElementByID("top-btn").style.display = "none";
        }
}

function topFunction() {
document.body.scrollTop = 0;
document.documentElement.scrollTop = 0;}