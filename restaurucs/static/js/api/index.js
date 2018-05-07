/* index.js */


$(window).load(function(){

    $.mobile.allowCrossDomainPages = true;

    function criar_pagina(identificador, url){
        /*
        Carrega uma página no HTML.
        */
        var div_page = $('<div>', {
            "id": identificador,
            "data-role": "page",
            "data-url": url
        })

        $(div_page).load(url);
        $("body").append(div_page);
    }

    // Carrega os dados da página inicial da app.
    $("#home").load('home.html', function(){
        $(this).trigger("create");
    });

    // Carrega as páginas.
    criar_pagina('teste', 'teste.html');
})
