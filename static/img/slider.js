let slideIndex = 0;

function showSlide(n) {
    const slides = document.querySelectorAll('.movie');
    if (n >= slides.length) {
        slideIndex = 0;
    } else if (n < 0) {
        slideIndex = slides.length - 1;
    }
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = 'none';
    }
    slides[slideIndex].style.display = 'block';
}

function moveSlide(n) {
    showSlide(slideIndex += n);
}

showSlide(slideIndex);
