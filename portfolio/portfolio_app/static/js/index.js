
menu_button = document.querySelector('#menu_button')
menu_container = document.querySelector('#menu_container')
menu_container.style.height = "0px"
menu_button.src = "static/img/menu.png"

menu_button.addEventListener('click',()=>{
   if(menu_container.style.height == "0px")
   {
    menu_container.style.height = "260px"
    menu_button.src = "static/img/close.png"

   }
   else 
   {
    menu_container.style.height = "0px"
    menu_button.src = "static/img/menu.png"

   }

   
})