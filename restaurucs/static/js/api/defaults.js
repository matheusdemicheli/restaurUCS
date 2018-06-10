$(document).bind("mobileinit", function(){
    /*
    Sobrescrita de valores padrões.
    */
    $.mobile.ajaxEnabled = true;
    $.mobile.linkBindingEnabled = true;
    $.mobile.allowCrossDomainPages = true;
    $.mobile.defaultPageTransition = "none";
    $.mobile.changePage.defaults.changeHash = false;
    $.mobile.hashListeningEnabled = false;
    $.mobile.pushStateEnabled = false;
});
