function utilizarhorasextra(id)
{
    console.log(id);
    token = document.getElementsByName('csrfmiddlewaretoken')[0].value;

    $.ajax(
    {
        type: 'POST',
        url: '/horasextras/utilizar-horasextra/' + id + '',
        data:
        {
            csrfmiddlewaretoken: token
        },
        success: function(result)
        {
            console.log(result);
            $('#mensagem').text(result.mensagem);
            $('#horas').text(result.horas);
        }
    });
}