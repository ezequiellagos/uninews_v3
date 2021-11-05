
$(document).ready(function() {

    
} );

function darkMode() {

    // localStorage.setItem('darkMode', true);


    // if (localStorage.getItem('darkMode') === 'true') {
    //     $('body').addClass('dark-mode');
    //     $('#dark-mode-switch').prop('checked', true);
    // }
    $("body").toggleClass("light-mode dark-mode");
    $("aside").toggleClass("sidebar-light-primary sidebar-dark-primary");
    $("nav").toggleClass("navbar-light navbar-dark");
    $("#dark_mode_switch").toggleClass("fa-moon fa-sun");
    $("#dark_mode_switch").toggleClass("text-navy text-yellow");

}