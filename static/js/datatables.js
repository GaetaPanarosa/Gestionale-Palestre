jQuery('#course_table').DataTable({
    processing: true,
    serverSide: true,
    ajax: '/control_panel/corsi/course_table/',
    lengthMenu: [[10, 25, 50, -1], [10, 25, 50, "All"]],
    language: {
        url: "//cdn.datatables.net/plug-ins/1.10.20/i18n/Italian.json"
    }
});


jQuery('#prenotation_table').DataTable({
    processing: true,
    serverSide: true,
    ajax: '/control_panel/prenotation/prenotation_table/',
    lengthMenu: [[10, 25, 50, -1], [10, 25, 50, "All"]],
    language: {
        url: "//cdn.datatables.net/plug-ins/1.10.20/i18n/Italian.json"
    }
});

jQuery('#users_table').DataTable({
    processing: true,
    serverSide: true,
    ajax:'/control_panel/lista_iscritti/iscritti_table/',
    lengthMenu: [[10, 25, 50, -1], [10, 25, 50, "All"]],
    language: {
        url: "//cdn.datatables.net/plug-ins/1.10.20/i18n/Italian.json"
    }
});