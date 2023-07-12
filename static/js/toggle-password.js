// window.addEventListener('load', handleToggle)

const toggleEl = document.querySelector('.login i')
const inputEl = document.querySelector('#id_password')
toggleEl.addEventListener('click', handleToggle)



function handleToggle(e){
    if (e) {
        if (inputEl.type === 'text') {
            inputEl.type = 'password'
            toggleEl.setAttribute('class', 'fa-solid fa-eye-slash')
        } else {
            inputEl.type = 'text'
            toggleEl.setAttribute('class', 'fa-solid fa-eye')
        }
    }
}

handleToggle()

// {#        <i class="fa-solid fa-eye"></i>#}
