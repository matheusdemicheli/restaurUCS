/* estabelecimento.js */
function adicionar_mascara_telefone(){
    /*
    Adiciona máscara nos campos para preenchimento do telefone.
    */
    $("[id^='id_telefone']").mask('(00) 00000-0000');
    $("[id^='id_telefone']").attr("placeholder", "(00) 00000-0000");
}

function form_submit(event){
    /*
    Remove a máscara dos campos antes do submit.
    */
    event.preventDefault();
    $("[id^='id_telefone']").unmask();
    $(this).unbind('submit').submit();
}

$(document).ready(function(){
    $.noConflict();
    adicionar_mascara_telefone();
    $('form').submit(form_submit);
    $('tr.add-row').click(adicionar_mascara_telefone);
})
