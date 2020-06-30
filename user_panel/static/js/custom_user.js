jQuery(document).ready(function () {
    "use strict";
    jQuery('#course_hours').hide();
    jQuery('#alert_prenotation').hide();
    jQuery('#details_prenotation').hide();
    jQuery('#course_day').hide();
    [].slice.call(document.querySelectorAll('select.cs-select')).forEach(function (el) {
        new SelectFx(el);
    });
    jQuery(".standardSelect").chosen({
        disable_search_threshold: 10,
        no_results_text: "Oops, nothing found!",
        width: "100%"
    });
    jQuery('.selectpicker').selectpicker;
    jQuery('a.chosen-single.chosen-default>span').text('Scegli fascia');

})
jQuery('#id_course').on('change', function (event) {
    jQuery('#course_day').show();
});

    jQuery('#user_prenotations').DataTable({
        processing: true,
        serverSide: true,
        order: [[1, "asc"]],
        ajax: "/profile/prenotazioni_utente_table/",
        lengthMenu: [[10, 25, 50, -1], [10, 25, 50, "All"]],
        language: {
            url: "//cdn.datatables.net/plug-ins/1.10.20/i18n/Italian.json"
        }
    });
jQuery('#course_hours_select').on('change', function (event) {
    jQuery('#alert_prenotation').show();
    jQuery('#details_prenotation').show();
})


/* create an array of days which need to be disabled */
var disabledDays = ["2-21-2010", "2-24-2010", "2-27-2010", "2-28-2010", "3-3-2010", "3-17-2010", "4-2-2010", "4-3-2010", "4-4-2010", "4-5-2010"];


/* create datepicker */
jQuery(document).ready(function () {
    jQuery.datetimepicker.setLocale('it');
    var today = new Date().getDay();
    var year = new Date().getFullYear();
    var month = new Date().getMonth();
    var day = new Date().getDate();
    var latency = 7 - today;
    var allowed_week = year + '-' + (month + 1) + '-' + (day + latency)
    var disabled_days = []
    var select_day = function (ct, $i) {
        jQuery('#course_hours_select').empty()
        var pk = jQuery('select#id_course').val();
        var date = new Date(ct).toLocaleDateString()
        var new_date = new Date(ct).getFullYear() + '-' + (new Date(ct).getMonth() + 1) + '-' + new Date(ct).getDate()
        jQuery.ajax({
            type: 'GET',
            url: '/get_hours_for_prenotation/',
            data: {'pk': pk, 'date': date},
            success: function (response) {
                if (response['status'] === '200') {
                    jQuery('#alert_error').append()
                    var len = response['hours'].length;
                    var i;

                    if (len === 1) {


                        jQuery('#hours_name').html("<p>Fascia Oraria: " + jQuery('#course_hours_select option:selected').html() + "</p>")
                        jQuery('#alert_prenotation').show();
                        jQuery('#details_prenotation').show();
                    }
                    for (i = 0; i < len; i++) {
                        jQuery("#course_hours_select").append("<option value=" + response['hours'][i]["id"] + ">" + response['hours'][i]["start_hour"] + " - " + response['hours'][i]["end_hour"] + "</option>")
                        jQuery("#course_hours_select").trigger("chosen:updated");
                    }
                    // jQuery('#hours_name').html("<p>Fascia Oraria: " + jQuery('#course_hours_select option:selected').html() + "</p>")
                    var pk_hour = jQuery('#course_hours_select').val();

                    jQuery.ajax({
                        type: 'GET',
                        data: {'pk_hour': pk_hour, 'date': jQuery('#date').val(), 'course': jQuery('#id_course').val()},
                        url: '/check_hours/',
                        success: function (response) {
                            if (response['status'] === '200') {
                                jQuery('#status_prenotation').html('<p style="color:green">' + response['reason'] + ':' + response['counts'] + '</p>')
                                jQuery('#hours_name').html("<p>Fascia Oraria: " + jQuery('#course_hours_select option:selected').html() + "</p>")
                            } else {
                                jQuery('#status_prenotation').html('<p style="color:red">' + response['reason'] + '</p>')
                            }
                        }
                    })
                    jQuery('#course_name').append("<p>Corso: " + response['course_name'] + "</p>");
                    jQuery('#date_name').html("<p>Giorno: " + date, 'dd/mm/YYYY' + "</p>");
                    jQuery('#course_hours').show();
                    jQuery('#alert_prenotation').show();
                    jQuery('#details_prenotation').show();
                } else {
                    disabled_days.push(date)
                    jQuery('#alert_error').html("<p class='text-danger mt-2'>" + response['reason'] + "</p>")
                    jQuery('#course_hours').hide();
                    jQuery("#course_hours_select").empty();
                }

            },
            error: function (response) {

            }
        })
        return date
    };
    //     jQuery('#date').datetimepicker({
    //     onSelectDate: select_day,
    //     onChangeDate: function () {
    //         jQuery("#course_hours_select").empty();
    //     },
    //     format: 'd/m/Y',
    //     timepicker: false,
    //     formatDate: 'Y/m/d',
    //     minDate: '0',
    //     maxDate: allowed_week,
    //     disabledDates: disabled_days,
    // });
    //
    jQuery('#date').datetimepicker({
        onSelectDate: select_day,
        onChangeDate: function () {
            jQuery("#course_hours_select").empty();
        },
        format: 'd/m/Y',
        timepicker: false,
        formatDate: 'Y/m/d',
        minDate: '0',
        // disabledDates: disabled_days,
    });
    jQuery('#prenotation_form').submit(function (event) {
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
    jQuery('#course_hours_select').on('change', function () {
        var pk_hour = jQuery('#course_hours_select').val();
        jQuery.ajax({
            type: 'GET',
            data: {'pk_hour': pk_hour, 'date': jQuery('#date').val(), 'course': jQuery('#id_course').val()},
            url: '/check_hours/',
            success: function (response) {
                if (response['status'] === '200') {
                    jQuery('#status_prenotation').html('<p style="color:green">' + response['reason'] + ':' + response['counts'] + '</p>')
                    jQuery('#hours_name').html("<p>Fascia Oraria: " + jQuery('#course_hours_select option:selected').html() + "</p>")
                } else {
                    jQuery('#status_prenotation').html('<p style="color:red">' + response['reason'] + '</p>')
                }
            }
        })

    })



});

