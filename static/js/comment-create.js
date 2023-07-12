// function commentCreate() {
//     const inputElement = document.querySelector('.comment-input')
//     const btnEl = document.getElementById('comment-btn')
//     btnEl.addEventListener('click', getComment)
//     const userId = Number(inputElement.id)
//     const csrftoken = document.querySelector('.destination-details input:nth-child(2)').value
//
//
//     function getComment() {
//         console.log('it works')
//
//         const parentEl = inputElement.parentElement.parentElement
//         const hrefContent = parentEl.querySelector('a').getAttribute("href")
//         const destinationId  = Number(hrefContent.split('/')[2])
//         const comment = inputElement.value
//         const BASE_URL = 'http://localhost:8000/catalogue/'
//
//         const httpHeaders = {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//                  'X-CSRFToken': csrftoken,
//                  // 'X-Requested-With': 'XMLHttpRequest'
//             },
//             body: JSON.stringify({
//                 "author_id": userId,
//                 "destination_id": destinationId,
//                 "content": comment,
//             })
//         }
//
//         fetch(BASE_URL, httpHeaders)
//             .then((res) => res.json())
//             .then((data) => console.log(data))
//
//      }
//
// }
//
// commentCreate()
