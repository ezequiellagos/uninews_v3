
// Dark Mode
$( "#dark_mode_switch" ).click(function() {
    $("body").toggleClass("light-mode dark-mode");
    $("#left_sidebar").toggleClass("sidebar-light-primary sidebar-dark-primary");
    $("#right_sidebar").toggleClass("control-sidebar-light control-sidebar-dark");
    $("nav").toggleClass("navbar-light navbar-dark");
    $("#dark_mode_switch i").toggleClass("fa-sun fa-moon");
    $("#dark_mode_switch i").toggleClass("text-navy text-yellow");

    if( $("body").hasClass("dark-mode") ){
        localStorage.setItem('dark-mode', 'true');
    }else{
        localStorage.setItem('dark-mode', 'false');
    }
});

if(localStorage.getItem('dark-mode') === 'true'){
    $("body").removeClass("light-mode");
    $("#left_sidebar").removeClass("sidebar-light-primary");
    $("#right_sidebar").removeClass("control-sidebar-light");
    $("nav").removeClass("navbar-light");
    $("#dark_mode_switch i").removeClass("fa-moon");
    $("#dark_mode_switch i").removeClass("text-navy");
    
    $("body").addClass("dark-mode");
    $("#left_sidebar").addClass("sidebar-dark-primary");
    $("#right_sidebar").addClass("control-sidebar-dark");
    $("nav").addClass("navbar-dark");
    $("#dark_mode_switch i").addClass("fa-sun");
    $("#dark_mode_switch i").addClass("text-yellow");
}else{
    $("body").removeClass("dark-mode");
    $("#left_sidebar").removeClass("sidebar-dark-primary");
    $("#right_sidebar").removeClass("control-sidebar-dark");
    $("nav").removeClass("navbar-dark");
    $("#dark_mode_switch i").removeClass("fa-sun");
    $("#dark_mode_switch i").removeClass("text-yellow");

    $("body").addClass("light-mode");
    $("#left_sidebar").addClass("sidebar-light-primary");
    $("#right_sidebar").addClass("control-sidebar-light");
    $("nav").addClass("navbar-light");
    $("#dark_mode_switch i").addClass("fa-moon");
    $("#dark_mode_switch i").addClass("text-navy");
}
// End Dark Mode