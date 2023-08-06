const toggleEl = document.querySelector('.login i')
const inputEl = document.querySelector('#id_password')
toggleEl.addEventListener('click', handleToggle)


function handleToggle(event){
    if (event) {
        if (inputEl.type === 'text') {
            inputEl.type = 'password'
            toggleEl.setAttribute('class', 'fa-solid fa-eye-slash login-eye')
        } else {
            inputEl.type = 'text'
            toggleEl.setAttribute('class', 'fa-solid fa-eye login-eye')
        }
    }
}

handleToggle()

