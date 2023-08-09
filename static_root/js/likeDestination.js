const buttonsDiv = document.querySelectorAll('.buttons-catalogue')



buttonsDiv.forEach(div => {
    const likeButton = div.querySelectorAll('a')[0]

    likeButton.addEventListener("click", event =>{
        event?.preventDefault()
        const destinationId = Number(likeButton.id)

        const currentHostname = window.location.hostname;
        let BASE_URL = ''
        if (currentHostname === '127.0.0.1') {
            BASE_URL = `http://127.0.0.1:8000/api/like/${destinationId}/`;
        } else if (currentHostname === '3.120.130.253') {
            BASE_URL = `http://3.120.130.253/api/like/${destinationId}/`;
        } else if (currentHostname === 'ec2-3-120-130-253.eu-central-1.compute.amazonaws.com') {
            BASE_URL = `http://ec2-3-120-130-253.eu-central-1.compute.amazonaws.com/api/like/${destinationId}/`;
        } else if (currentHostname === 'destinations-catalogue.eu') {
            BASE_URL = `http://destinations-catalogue.eu/api/like/${destinationId}/`;
        }

        if (currentUser === 'AnonymousUser') {
            window.location.href = '/profile/login/';
            return;
        }

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