const toggleEl1 = document.querySelector('.fa-eye-slash.first')
const toggleEl2 = document.querySelector('.fa-eye-slash.second')
const inputEl1 = document.querySelector('#id_password1')
const inputEl2 = document.querySelector('#id_password2')
toggleEl1.addEventListener('click', handleToggleCreate)
toggleEl2.addEventListener('click', handleToggleCreateSecond)
const errorContent = document.querySelector('.error-message p').textContent

if (errorContent !== '') {
    toggleEl1.style.cssText = 'top:54%;'
    toggleEl2.style.cssText = 'top:70.8%;'
} else {
    toggleEl1.style.cssText = 'top:52%;'
    toggleEl2.style.cssText = 'top:69%;'
}

function handleToggleCreate(e){
    if (e) {
        if (inputEl1.type === 'text') {
            inputEl1.type = 'password'
            toggleEl1.setAttribute('class', 'fa-solid fa-eye-slash first')
        } else {
            inputEl1.type = 'text'
            toggleEl1.setAttribute('class', 'fa-solid fa-eye first')
        }
    }
}

handleToggleCreate()

function handleToggleCreateSecond(e){
    if (e) {
        if (inputEl2.type === 'text') {
            inputEl2.type = 'password'
            toggleEl2.setAttribute('class', 'fa-solid fa-eye-slash second')
        } else {
            inputEl2.type = 'text'
            toggleEl2.setAttribute('class', 'fa-solid fa-eye second')
        }
    }
}

handleToggleCreateSecond()