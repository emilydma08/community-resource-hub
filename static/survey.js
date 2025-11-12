document.addEventListener("DOMContentLoaded", () =>{
    const slides = document.querySelectorAll('.q');
    let currentSlide = 0;
    const showSlide = (index) => {
        slides.forEach((s,i) => s.classList.toggle('active',i===index));
    };
    document.querySelectorAll('.next').forEach(btn => {
        btn.addEventListener('click', () => {
            if(currentSlide <slides.length-1) {
                currentSlide++;
                showSlide(currentSlide);
            }
        });
    });

    document.querySelectorAll('.back').forEach(btn => {
        btn.addEventListener('click', () => {
            if(currentSlide > 0) {
                currentSlide--;
                showSlide(currentSlide);
            }
        });
    });



});