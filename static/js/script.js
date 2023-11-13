function openMenu() {
    let menuBtn = document.querySelector('.toggle_btn');
    let menuBtnIcon = document.querySelector('.toggle_btn i');
    let dropDownMenu = document.querySelector('.dropdown_menu');
    let pageLinks = document.querySelectorAll('.category');
    function openDropDown() {
        dropDownMenu.classList.toggle('open');
        const menuIsOpen = dropDownMenu.classList.contains('open');
        menuBtnIcon.classList = menuIsOpen ? 'fa-solid fa-xmark' : 'fa-solid fa-bars';
    }
    menuBtn.onclick = openDropDown;
    pageLinks.forEach((nav_but) => {
        nav_but.onclick = openDropDown;
    })
}

addEventListener('load', openMenu);