const buttonsDiv = document.querySelectorAll('.buttons-catalogue')

buttonsDiv.forEach(div => {
    const likeButton = div.querySelectorAll('a')[0]
    const hrefValue = Number(likeButton.getAttribute("href").split('/')[3]);

    likeButton.addEventListener("click", event =>{
        event?.preventDefault()
        if (currentUser === 'AnonymousUser') {
            window.location.href = '/profile/login/';
            return;
        }

        const BASE_URL = `http://127.0.0.1:8000/api/like/${hrefValue}/`;
        fetch(BASE_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
            },
        })
        .then(response => response.json())
        .then(data => {
            const thumb = likeButton.querySelector('i')

            if (data.message === 'Destination liked.') {
                thumb.classList.remove('fa-regular')
                thumb.classList.add('fa-solid')
            } else if (data.message === 'Destination unliked.') {
                thumb.classList.remove('fa-solid')
                thumb.classList.add('fa-regular')
            }

            for (const node of likeButton.childNodes) {
                if (node.nodeType === Node.TEXT_NODE) {
                  node.nodeValue = ` ${data['total_likes']}`;
                  break;
                }
            }

        })
        .catch(error => {
            console.error('Error:', error);
        });

    })

})