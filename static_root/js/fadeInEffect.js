function fadeInElement(element, duration) {
    element.style.opacity = 0;
    const startTime = performance.now();

    function updateOpacity(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        element.style.opacity = progress;

        if (progress < 1) {
            requestAnimationFrame(updateOpacity);
        }
    }

    requestAnimationFrame(updateOpacity);
}

const exploreHeading = document.querySelector('.explore-heading');
const exploreDescription = document.querySelector('.explore-description');

fadeInElement(exploreHeading, 2000);
fadeInElement(exploreDescription, 2000);