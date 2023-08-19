// const currentUser = userData['currentUser'];
//
// const tokenInput = document.querySelector('input[name="csrfmiddlewaretoken"]');
// const csrfToken = tokenInput.value;
// const editButtons = document.querySelectorAll('.fa-pencil');
// editButtons.forEach(editButton => {
//     editButton.addEventListener('click', event => {
//         event?.preventDefault();
//         const commentElement = editButton.parentElement.parentElement;
//         let commentContent = commentElement.textContent.trim();
//         const commentId = commentElement.id;
//         const commentCreator = commentElement.previousElementSibling.textContent.trim();
//         if (currentUser === commentCreator) {
//             const editForm = commentElement
//                 .parentElement.parentElement.parentElement
//                 .previousElementSibling
//                 .querySelector('.destination-details');
//             const inputs = editForm.elements;
//             const textArea = inputs[0];
//             const editButton = inputs[3];
//             textArea.value = commentContent;
//             editButton.addEventListener('click', (event) => {
//                 event?.preventDefault()
//                 const updatedContent = textArea.value;
//
//                 const currentHostname = window.location.hostname;
//                 let BASE_URL = ''
//                 if (currentHostname === '127.0.0.1') {
//                     BASE_URL = `http://127.0.0.1:8000/api/edit_comment/${commentId}/`;
//                 } else if (currentHostname === '3.120.130.253') {
//                     BASE_URL = `http://3.120.130.253/api/edit_comment/${commentId}/`;
//                 } else if (currentHostname === 'ec2-3-120-130-253.eu-central-1.compute.amazonaws.com') {
//                     BASE_URL = `http://ec2-3-120-130-253.eu-central-1.compute.amazonaws.com/api/edit_comment/${commentId}/`;
//                 } else if (currentHostname === 'destinations-catalogue.eu') {
//                     BASE_URL = `http://destinations-catalogue.eu/api/edit_comment/${commentId}/`;
//                 }
//
//                     fetch(BASE_URL, {
//                         method: 'PUT',
//                         headers: {
//                             'Content-Type': 'application/json',
//                             'X-CSRFToken': csrfToken
//                         },
//                         body: JSON.stringify({
//                             id: commentId,
//                             "content": updatedContent,
//                             })
//                         })
//                         .then((response) => response.json())
//                         .then((response_data) => {
//                             textArea.value = '';
//                             for (const node of commentElement.childNodes) {
//                                 if (node.nodeType === Node.TEXT_NODE) {
//                                   node.nodeValue = response_data['updated_comment'].content;
//                                   break;
//                                 }
//                               }
//                         })
//                         .catch((error) => {
//                             console.log(error)})
//             })
//         } else {
//              window.location.href = '/permission-denied/';
//         }
//     })
// })


const currentUser = userData.currentUser;
const tokenInput = document.querySelector('input[name="csrfmiddlewaretoken"]');
const csrfToken = tokenInput.value;
const editButtons = document.querySelectorAll('.fa-pencil');
const sendButton = document.querySelector('form > button');
const currentPath = window.location.href.split('/catalogue')[0];


editButtons.forEach(editButton => {
    editButton.addEventListener('click', event => {
        // Disable all edit buttons
        editButtons.forEach(editButton => {
            editButton.style.pointerEvents = 'none';
            editButton.style.cursor = 'auto';
        });

        event?.preventDefault();
        const commentElement = editButton.parentElement.parentElement;
        let commentContent = commentElement.textContent.trim();
        const commentId = commentElement.id;
        const commentCreator = commentElement.previousElementSibling.textContent.trim();

        if (currentUser === commentCreator) {
            const editForm = commentElement
                .parentElement.parentElement.parentElement
                .previousElementSibling
                .querySelector('.destination-details');
            const inputs = editForm.elements;
            const textArea = inputs[0];
            textArea.value = commentContent;

            // Add event listener to the send button
            const sendButtonClickHandler = (event) => {
                event?.preventDefault();
                sendButton.removeEventListener('click', sendButtonClickHandler); // Remove the event listener

                const updatedContent = textArea.value;
                const BASE_URL = `${currentPath}/api/edit_comment/${commentId}/`;

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
                    // Enable edit buttons after the update is complete
                    editButtons.forEach(editButton => {
                        editButton.style.pointerEvents = 'auto';
                        editButton.style.cursor = 'pointer';
                    });
                })
                .catch((error) => {
                    console.log(error);
                });
            };

            sendButton.addEventListener('click', sendButtonClickHandler);
        } else {
            window.location.href = '/permission-denied/';
        }
    });
});

