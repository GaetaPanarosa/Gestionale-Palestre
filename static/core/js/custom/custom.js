$(document).ready(function () {
    "use strict";
    $('.select2-results__message').text('Nessun Risultato');
    $('#form_trainer > .card-body > .row > .col-lg-4 > .form-group > .input-group > #id_sex').addClass('standardSelect').removeClass('form-control');
    $('.selectpicker').selectpicker;
    $('a.chosen-single.chosen-default>span').text('Scegli fascia');
    $('#add_trainer_box').hide();
    $('#add_hours_box').hide();
    $('a.add-trainer-button').click(function (event) {
        $('#add_trainer_box').show().fadeIn("slow");
        $('#aggiungi_istruttore>.card>h1').replaceWith(
            '    <div class="row px-2">\n' +
            '                        <h1 class="m-3">Inserimento nuovo istruttore</h1>\n' +
            '        <div class="close-button p-3 ml-auto" onclick="closeButtonTrainer()" id="closex\_button"><i class="iconsminds-close"></i></div>\n' +
            '                    </div>\n'
        )
    });
    $('.add-hour-button').click(function () {
        $('#hours_form').attr('action', 'fasce_orarie_corso');
        $('#add_hours_box').show().fadeIn(100);
        $('#aggiungi_fasce_orarie>.card>h2').replaceWith(
            '    <div class="row px-2">\n' +
            '                        <h2 class="m-3">Inserimento fasce orarie</h2>\n' +
            '        <div class="close-button p-3 ml-auto" onclick="closeButtonHour()" id="close_button_hour"><i class="iconsminds-close"></i></div>\n' +
            '                    </div>\n'
        )
    })
    $('.del-hour-button').click(function (event) {
        var pk = $('select#hour_list').val();
        $.ajax({
            type: 'GET', // GET or POST
            contentType: 'application/x-www-form-urlencoded;charset=utf-8',
            url: 'cancella_fascia/' + pk + '/', // the file to call
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
                        }
                    })
                } else {
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

    })
    $('.mod-hour-button').click(function () {
        $('#add_hours_box').show().fadeIn(100);
        var pk = $('select#hour_list').val();
        $('#hours_form').attr('action', '/modifica_fasce/' + pk + '/');
        $('#aggiungi_fasce_orarie>.card>.card-header').replaceWith(
            '<div class="card-header">\n' +
            '    <div class="row px-2">\n' +
            '                        <strong>Inserimento fasce orarie</strong>\n' +
            '        <div class="close-button ml-auto" onclick="closeButtonHour()" id="close_button_hour"><i class=" fa fa-times"></i></div>\n' +
            '                    </div>\n' +
            '</div>'
        )
        console.log(pk)
        $.ajax({
            type: 'GET',
            url: 'info_fascia/' + pk + '/',
            success: function (response) {
                console.log(response)
                $('#id_start_hour').val(response['start_hour']);
                $('#id_end_hour').val(response['end_hour']);
                $('#id_hours_pk').val(response['pk']);
            }
        })
        return false
    });
    $('#form_trainer > .card-body > .row > .col-lg-4 > .form-group > .input-group > input').addClass('input-sm form-control-sm');
})

function disableCourse(pk, event) {
    $.ajax({
        data: {'pk': pk},
        type: 'GET',
        url: 'disattiva_corso/',
        success: function (response) {
            if (response.status == '200') {
                toastSuccess('Corso disattivato', "Il corso è stato disattivato con successo.")
            } else {
                toastError('Errore', response.reason.toString())
            }
        }
    });
    return false
}

function enableCourse(pk) {
    $.ajax({
        data: {'pk': pk},
        type: 'GET',
        url: '/corsi/riattiva_corso/',
        success: function (response) {
            if (response.status == '200') {
                toastSuccess('Corso riattivato', "Il corso è stato riattivato con successo.")
            } else {
                toastError('Errore', response.reason.toString())
            }
        }
    });
    return false
}

function closeButtonTrainer() {
    $('#add_trainer_box').hide().fadeOut("slow");
    $('form#form_trainer').val('');
};

function closeButtonHour() {
    $('#add_hours_box').hide().fadeOut("slow");
    $('form#form_trainer').val('');
};

function disactiveHour(form_id) {
    console.log($('form#' + form_id).serialize())
    $.ajax({
        type: 'GET',
        url: 'disattiva_fascia_corso/',
        data: $('form#' + form_id).serialize(),
        success: function (response) {
            if (response.status == '200') {
                toastSuccess('Fascia oraria disattivato', "La fasica oraria è stata disattivata con successo.")
            } else {
                toastError('Errore', response.reason.toString())
            }
        }
    })
}

function restoreHour(form_id) {
    console.log($('form#' + form_id).serialize())
    $.ajax({
        type: 'GET',
        url: '/riattiva_fascia_corso/',
        data: $('form#' + form_id).serialize(),
        success: function (response) {
            if (response.status == '200') {
                toastSuccess('Fascia oraria riattivata', "La fascia oraria è stata riattivata con successo.")
            } else {
                toastError('Errore', response.reason.toString())
            }
        }
    })
}

function disactiveDay(pk) {
    $.ajax({
        type: 'GET',
        url: '/disattiva_giorno_corso/',
        data: {'pk': pk},
        success: function (response) {
            if (response.status == '200') {
                toastSuccess('Giorno disattivato', "Il giorno è stato disattivato con successo.")
            } else {
                toastError('Errore', response.reason.toString())
            }
        }
    })
}

function restoreDay(pk) {
    $.ajax({
        type: 'GET',
        url: '/riattiva_giorno_corso/',
        data: {'pk': pk},
        success: function (response) {
            if (response.status == '200') {
                toastSuccess('Giorno riattivato', "Il giorno è stato riattivato con successo.")
            } else {
                toastError('Errore', response.reason.toString())
            }
        }
    })
}

