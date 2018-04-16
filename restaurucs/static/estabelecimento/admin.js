/* estabelecimento.js */
function adicionar_mascara_telefone(){
    $("[id^='id_telefone']").mask('(00) 00000-0000')
    $("[id^='id_telefone']").attr("placeholder", "(00) 00000-0000");
}

$(document).ready(function(){
    $.noConflict();
    adicionar_mascara_telefone();
    $("tr.add-row").click(adicionar_mascara_telefone);
})
