const divElements = document.querySelectorAll('.section-explore')
    window.addEventListener("load", (e) => {
        divElements.forEach((el) => {
            if (el.classList.contains('Europe')) {
                el.style.display = 'flex'
            }
        })
    });
    document.querySelectorAll('.li-continent').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const allALinks = document.querySelectorAll('#a-continent')
        allALinks.forEach((a) => {
            a.style.fontSize = '1.3rem'
            a.style.color = '#b7f8f1'
        })

    e.target.style.color = '#fff'
    e.target.style.fontSize = '1.7rem'
    const continent = e.target.textContent.split(' ')[0]

    divElements.forEach((div) => {
       if (div.classList.contains(continent)) {
           div.style.display = 'flex'
       } else {
            div.style.display = 'none'
       }
    })
    });
  });