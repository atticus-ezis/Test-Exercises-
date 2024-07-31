document.addEventListener('DOMContentLoaded', () => {
    const track = document.querySelector('.slides');
    const slides = Array.from(track.children);
    const nextButton = document.querySelector('.next-slide');
    const backButton = document.querySelector('.back-slide');
    let currentIndex = 0;

    const setSlidePosition = (slide, index) => {
        slide.style.left = `${index * 100}%`;
    };
    slides.forEach(setSlidePosition);

    const moveToSlide = (track, currentSlide, targetSlide) => {
        track.style.transition = 'transform 0.5s ease-in-out';
        track.style.transform = `translateX(-${targetSlide.style.left})`;
        currentSlide.classList.remove('current-slide');
        targetSlide.classList.add('current-slide');
    };

    const moveToNextSlide = () => {
        const currentSlide = track.querySelector('.current-slide');
        const nextIndex = (currentIndex + 1) % slides.length;
        const nextSlide = slides[nextIndex];
        
        moveToSlide(track, currentSlide, nextSlide);
        currentIndex = nextIndex;
    };

    const moveToPreviousSlide = () => {
        const currentSlide = track.querySelector('.current-slide');
        const prevIndex = (currentIndex - 1 + slides.length) % slides.length;
        const prevSlide = slides[prevIndex];
        
        moveToSlide(track, currentSlide, prevSlide);
        currentIndex = prevIndex;
    };

    nextButton.addEventListener('click', moveToNextSlide);
    backButton.addEventListener('click', moveToPreviousSlide);

    // Autoplay functionality
    setInterval(moveToNextSlide, 3000); // Change slide every 3 seconds
});
