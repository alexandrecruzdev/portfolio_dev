menu_button = document.querySelector('#menu_button')
menu_container = document.querySelector('#menu_container')
menu_button.addEventListener('click',()=>{
    if(menu_container.style.display == 'block')
    {
        menu_container.style.display = 'none'
        menu_button.src = "static/img/menu.png"
    }
    else
    {
        menu_container.style.display = 'block'
        menu_button.src = "static/img/close.png"
    }
})