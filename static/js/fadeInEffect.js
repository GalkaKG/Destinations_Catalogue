// Function to apply the fade-in effect to the elements
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

    // Get the elements to apply the effect
    const exploreHeading = document.querySelector('.explore-heading');
    const exploreDescription = document.querySelector('.explore-description');

    // Call the function to apply the fade-in effect (adjust the duration as needed)
    fadeInElement(exploreHeading, 2000);
    fadeInElement(exploreDescription, 2000);