jQuery(document).ready(function () {
    "use strict";
    jQuery('#form_trainer > .card-body > .row > .col-lg-4 > .form-group > .input-group > #id_sex').addClass('standardSelect').removeClass('form-control');

    jQuery(".standardSelect").chosen({
        disable_search_threshold: 10,
        no_results_text: "Nessun risultato",
        width: "90%",

    });
    jQuery('.selectpicker').selectpicker;
    jQuery('a.chosen-single.chosen-default>span').text('Scegli fascia');
    jQuery('#add_trainer_box').hide();
    jQuery('#add_hours_box').hide();
    jQuery('a.add-trainer-button').click(function (event) {
        jQuery('#add_trainer_box').show().fadeIn("slow");
        jQuery('#aggiungi_istruttore>.card>.card-header').replaceWith(
            '<div class="card-header">\n' +
            '    <div class="row px-2">\n' +
            '                        <strong>Inserimento nuovo istruttore</strong>\n' +
            '        <div class="close-button ml-auto" onclick="closeButtonTrainer()" id="closex\_button"><i class=" fa fa-times"></i></div>\n' +
            '                    </div>\n' +
            '</div>'
        )
    });

    jQuery('#hours_form').submit(function (event) {
        let csrfmiddlewaretoken = jQuery('input[name=csrfmiddlewaretoken]').val();
        jQuery.ajax({
            data: jQuery(this).serialize(),
            type: jQuery(this).attr('method'), // GET or POST
            contentType: 'application/x-www-form-urlencoded;charset=utf-8',
            url: jQuery(this).attr('action'), // the file to call
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
                        duration: 500,
                        onClosing: function () {
                            event.preventDefault()
                        }
                    });
                }
            }
        });
        return false
    })

    jQuery('#add_course_day_hours').submit(function (event) {
        var hours = jQuery('#id_hours').val()
        let csrfmiddlewaretoken = jQuery('input[name=csrfmiddlewaretoken]').val();
        var value = jQuery(this).serialize() + '&hours_arr=' + JSON.stringify(hours);
        jQuery.ajax({
            data: value,
            type: jQuery(this).attr('method'), // GET or POST
            contentType: 'application/x-www-form-urlencoded;charset=utf-8',
            url: jQuery(this).attr('action'), // the file to call
            success: function (response) {
                if (response.status == '200') {
                    console.log(response)
                    iziToast.success({
                        title: 'Operazione Effettuata!',
                        message: response.reason,
                        position: 'center',
                        duration: 500,

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
    jQuery('#add_course_id').submit(function (event) {
        let csrfmiddlewaretoken = jQuery('input[name=csrfmiddlewaretoken]').val();
        console.log(jQuery(this).serialize())
        jQuery.ajax({
            data: jQuery(this).serialize(),
            type: jQuery(this).attr('method'), // GET or POST
            contentType: 'application/x-www-form-urlencoded;charset=utf-8',
            url: jQuery(this).attr('action'), // the file to call
            success: function (response) {
                if (response.status == '200') {
                    iziToast.success({
                        title: 'Operazione Effettuata!',
                        message: response.reason,
                        position: 'center',
                        duration: 500,
                        onClosing: function () {
                            location.reload();
                            jQuery('#details_order_collapse').removeClass('show');
                            jQuery('#course_day_hours_collapse').addClass('show');
                        }
                    })
                } else {
                    iziToast.error({
                        title: 'Operazione non riuscita!',
                        message: response.reason,
                        position: 'center',
                        duration: 500,
                        onClosing: function () {
                            event.preventDefault()
                        }
                    });
                }
            }
        });
        return false
    });

    jQuery('a.add-hour-button').click(function () {
        jQuery('#hours_form').attr('action', '/control_panel/fasce_orarie_corso');
        jQuery('#add_hours_box').show().fadeIn(100);
        jQuery('#aggiungi_fasce_orarie>.card>.card-header').replaceWith(
            '<div class="card-header">\n' +
            '    <div class="row px-2">\n' +
            '                        <strong>Inserimento fasce orarie</strong>\n' +
            '        <div class="close-button ml-auto" onclick="closeButtonHour()" id="close_button_hour"><i class=" fa fa-times"></i></div>\n' +
            '                    </div>\n' +
            '</div>'
        )
    })

    jQuery('a.del-hour-button').click(function (event) {
        var pk = jQuery('select#hour_list').val();
        jQuery.ajax({
            type: 'GET', // GET or POST
            contentType: 'application/x-www-form-urlencoded;charset=utf-8',
            url: '/control_panel/cancella_fascia/' + pk + '/', // the file to call
            success: function (response) {
                if (response.status == '200') {
                    iziToast.success({
                        title: 'Operazione Effettuata!',
                        message: response.reason,
                        position: 'center',
                        duration: 500,
                        onClosing: function () {
                            location.reload();
                        }
                    })
                } else {
                    iziToast.error({
                        title: 'Operazione non riuscita!',
                        message: response.reason,
                        position: 'center',
                        duration: 500,
                        onClosing: function () {
                            event.preventDefault()
                        }
                    });
                }
            }
        });

    })

    jQuery('a.mod-hour-button').click(function () {
        jQuery('#add_hours_box').show().fadeIn(100);
        var pk = jQuery('select#hour_list').val();
        jQuery('#hours_form').attr('action', '/control_panel/modifica_fasce/' + pk + '/');
        jQuery('#aggiungi_fasce_orarie>.card>.card-header').replaceWith(
            '<div class="card-header">\n' +
            '    <div class="row px-2">\n' +
            '                        <strong>Inserimento fasce orarie</strong>\n' +
            '        <div class="close-button ml-auto" onclick="closeButtonHour()" id="close_button_hour"><i class=" fa fa-times"></i></div>\n' +
            '                    </div>\n' +
            '</div>'
        )
        console.log(pk)
        jQuery.ajax({
            type: 'GET',
            url: 'info_fascia/' + pk + '/',
            success: function (response) {
                console.log(response)
                jQuery('#id_start_hour').val(response['start_hour']);
                jQuery('#id_end_hour').val(response['end_hour']);
                jQuery('#id_hours_pk').val(response['pk']);
            }
        })
        return false
    });

    jQuery('#form_trainer > .card-body > .row > .col-lg-4 > .form-group > .input-group > input').addClass('input-sm form-control-sm');

    jQuery("#form_trainer").submit(function (event) {
        let csrfmiddlewaretoken = jQuery('input[name=csrfmiddlewaretoken]').val();
        console.log(jQuery(this).serialize())
        jQuery.ajax({
            data: jQuery(this).serialize(),
            type: jQuery(this).attr('method'), // GET or POST
            url: jQuery(this).attr('action'), // the file to call
            success: function (response) {
                if (response.status == '200') {
                    iziToast.success({
                        title: 'Operazione Effettuata!',
                        message: response.reason,
                        position: 'center',
                        duration: 500,
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

function closeButtonTrainer() {
    jQuery('#add_trainer_box').hide().fadeOut("slow");
    jQuery('form#form_trainer').val('');
};

function closeButtonHour() {
    jQuery('#add_hours_box').hide().fadeOut("slow");
    jQuery('form#form_trainer').val('');
};


