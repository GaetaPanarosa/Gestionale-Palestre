$(document).ready(function (event) {
    $('#hours_form').submit(function (event) {
        let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            data: $(this).serialize(),
            type: $(this).attr('method'), // GET or POST
            contentType: 'application/x-www-form-urlencoded;charset=utf-8',
            url: $(this).attr('action'), // the file to call
            success: function (response) {
                if (response.status == '200') {
                    iziToast.success({
                        title: 'Operazione Effettuata!',
                        message: response.reason,
                        position: 'center',
                        duration: 600,
                        onClosing: function () {
                            location.reload();
                        }
                    })
                } else {
                    iziToast.error({
                        title: 'Operazione non riuscita!',
                        message: response.reason,
                        position: 'center',
                        duration: 600,
                        onClosing: function () {
                            event.preventDefault()
                        }
                    });
                }
            }
        });
        return false
    })
    $('#add_course_day_hours').submit(function (event) {
        var hours = $('#id_hours').val()
        let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
        var value = $(this).serialize() + '&hours_arr=' + JSON.stringify(hours);
        $.ajax({
            data: value,
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
                        duration: 400,
                        timeout: 500,
                        onClosing: function () {
                            location.reload()
                        }
                    })
                } else {
                    iziToast.error({
                        title: 'Operazione non riuscita!',
                        message: response.reason,
                        position: 'center',
                        onClosing: function () {
                            event.preventDefault()
                        }
                    });
                }
            }
        });
        return false
    });
    $('#add_course_id').submit(function (event) {
        let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
        console.log($(this).serialize())
        $.ajax({
            data: $(this).serialize(),
            type: $(this).attr('method'), // GET or POST
            contentType: 'application/x-www-form-urlencoded;charset=utf-8',
            url: $(this).attr('action'), // the file to call
            success: function (response) {
                if (response.status == '200') {
                    iziToast.success({
                        title: 'Operazione Effettuata!',
                        message: response.reason,
                        position: 'center',
                        duration: 1000,
                        timeout: 1000,
                        onClosing: function () {
                            location.reload();
                            $('#details_order_collapse').removeClass('show');
                            $('#course_day_hours_collapse').addClass('show');
                        }
                    })
                } else {
                    console.log(response.reason);
                    iziToast.error({
                        title: 'Operazione non riuscita!',
                        message: response.reason,
                        position: 'center',
                        duration: 1000,
                        timeout: 1000,
                        onClosing: function () {
                            event.preventDefault()
                        }
                    });
                }
            }
        });
        return false
    });
    $("#form_trainer").submit(function (event) {
        let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
        console.log($(this).serialize())
        $.ajax({
            data: $(this).serialize(),
            type: $(this).attr('method'), // GET or POST
            url: $(this).attr('action'), // the file to call
            success: function (response) {
                if (response.status == '200') {
                    iziToast.success({
                        title: 'Operazione Effettuata!',
                        message: response.reason,
                        position: 'center',
                        duration: 400,
                        timeout: 500,
                        onClosing: function () {
                            location.reload();
                        }
                    })
                } else {
                    iziToast.error({
                        title: 'Operazione non riuscita!',
                        message: response.reason,
                        position: 'center',
                        onClosing: function () {
                            event.preventDefault()
                        }
                    });
                }
            }
        });
        return false
    });
})