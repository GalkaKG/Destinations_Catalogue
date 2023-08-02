const currentUser = userData.currentUser;
const tokenInput = document.querySelector('input[name="csrfmiddlewaretoken"]');
const csrfToken = tokenInput.value;
const editButtons = document.querySelectorAll('.fa-pencil');
editButtons.forEach(editButton => {
    editButton.addEventListener('click', event => {
        event?.preventDefault();
        const commentElement = editButton.parentElement.parentElement;
        let commentContent = commentElement.textContent.trim();
        const commentId = commentElement.id;
        const commentCreator = commentElement.previousElementSibling.textContent;

        if (currentUser === commentCreator) {
            const editForm = commentElement
                .parentElement.parentElement.parentElement
                .previousElementSibling
                .querySelector('.destination-details');
            const inputs = editForm.elements;
            const textArea = inputs[0];
            const editButton = inputs[3];
            textArea.value = commentContent;
            editButton.addEventListener('click', (event) => {
                event?.preventDefault()
                const updatedContent = textArea.value;
                const BASE_URL = `http://127.0.0.1:8000/api/edit_comment/${commentId}/`;

                    fetch(BASE_URL, {
                        method: 'PUT',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': csrfToken
                        },
                        body: JSON.stringify({
                            id: commentId,
                            "content": updatedContent,
                            })
                        })
                        .then((response) => response.json())
                        .then((response_data) => {
                            textArea.value = '';
                            for (const node of commentElement.childNodes) {
                                if (node.nodeType === Node.TEXT_NODE) {
                                  node.nodeValue = response_data['updated_comment'].content;
                                  break;
                                }
                              }
                        })
                        .catch((error) => {
                            console.log(error)})
            })
        } else {
             window.location.href = '/permission-denied/';
        }
    })
})
