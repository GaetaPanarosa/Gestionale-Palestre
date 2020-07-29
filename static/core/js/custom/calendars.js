$(document).ready(function (event) {
    $.fn.datepicker.dates['en'] = {
        days: ["Domenica", "Lunedi", "Martedi", "Mercoledi", "Giovedi", "Venerdi", "Sabato"],
        daysShort: ["Dom", "Lun", "Mar", "Mer", "Gio", "Ven", "Sab",],
        daysMin: ["Dom", "Lun", "Mar", "Mer", "Gio", "Ven", "Sab",],
        months: ["Gennaio", "February", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicenbre"],
        monthsShort: ["Gen", "Feb", "Mar", "Apr", "Mag", "Giu", "Lug", "Ago", "Set", "Ott", "Nov", "Dic"],
        today: "Today",
        clear: "Clear",
        format: "yyyy-mm-dd",
        titleFormat: "MM yyyy",
        weekStart: 1
    }
    var options = {
        format: 'yyyy-mm-dd',
        language: 'en'
    }
    $('#id_date_of_birth').datepicker(options);
    $('#start_datepicker').datepicker(options);
    $('#start_datepicker').on('changeDate', function (event) {
        var date = event.date.toLocaleDateString();
        alert(date);
        $('#id_start_date').val(date);
    });
    $('#end_datepicker').datepicker(options);
    $('#end_datepicker').on('changeDate', function (event) {
        var date = event.date.toLocaleDateString();
        alert(date)
        $('#id_end_date').val(date);
    });

});