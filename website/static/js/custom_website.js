$(document).ready(function (event) {
    $('#terms').click(function () {
        if ($(this).prop('checked') === true) {
            $('#register').removeAttr('disabled');
        } else {
            event.preventDefault();
        }
    });
    $('#register_form').submit(function (event) {
        let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            data: $(this).serialize(),
            type: $(this).attr('method'), // GET or POST
            contentType: 'application/x-www-form-urlencoded;charset=utf-8',
            url: $(this).attr('action'), // the file to call
            success: function (response) {
                if (response.status == '200') {
                    console.log(response)
                    iziToast.success({
                        title: 'Operazione Effettuata!',
                        message: response.reason,
                        position: 'center',
                        duration: 10,
                        onClosing: function () {
                            $.ajax({
                                data: {'csrfmiddlewaretoken':csrfmiddlewaretoken, 'username': response.data.username, 'password':response.data.password},
                                type: 'POST', // GET or POST
                                contentType: 'application/x-www-form-urlencoded;charset=utf-8',
                                url: '/login',
                                success: function (response) {
                                    console.log(response)
                                    location.href = '/login'
                                }// the file to call
                            })
                        }
                    })
                } else {
                    iziToast.error({
                        title: 'Operazione non riuscita!',
                        message: response.reason,
                        position: 'center',
                        timeout: 20000,
                    });
                }
            }
        });
        return false
    })
    $('#login_form').submit(function (event) {
        console.log('click')
        let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            data: $(this).serialize(),
            type: $(this).attr('method'), // GET or POST
            contentType: 'application/x-www-form-urlencoded;charset=utf-8',
            url: $(this).attr('action'), // the file to call
            success: function (response) {
                if (response.status == 'error') {
                    console.log(response)
                    $('#errors').append('<div class="alert mt-3 alert-danger" role="alert">' + response.reason + '</div>')
                } else {
                    location.href = '/login'
                }
            }, error(response) {
                console.log(response)
            }
        });
        return false
    })


    if (window.screen.width <= 767) {
        $("#logo").removeClass("col-lg-2");
    }
})





