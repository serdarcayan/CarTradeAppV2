const navShow = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const links = document.querySelectorAll('nav-links li')

    burger.addEventListener('click', () => {
        nav.classList.toggle('nav-active');

        // links.forEach((link,index)=>{
        //     link.style.animation = "linksFade .5s ease forwards ";
        // });
        burger.classList.toggle('close');
    });

}
navShow();