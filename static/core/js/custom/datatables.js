$('#course_table').DataTable({
    processing: true,
    serverSide: true,
    ajax: '/corsi/course_table/',
    lengthMenu: [[10, 25, 50, -1], [10, 25, 50, "All"]],
    language: {
        url: "//cdn.datatables.net/plug-ins/1.10.20/i18n/Italian.json"
    }
});
$('#course_table_disactivated').DataTable({
    processing: true,
    serverSide: true,
    ajax: '/corsi/course_disactivated_table/',
    lengthMenu: [[10, 25, 50, -1], [10, 25, 50, "All"]],
    language: {
        url: "//cdn.datatables.net/plug-ins/1.10.20/i18n/Italian.json"
    }
});


$('#prenotation_table').DataTable({
    processing: true,
    serverSide: true,
    ajax: '/prenotation/prenotation_table/',
    lengthMenu: [[10, 25, 50, -1], [10, 25, 50, "All"]],
    language: {
        url: "//cdn.datatables.net/plug-ins/1.10.20/i18n/Italian.json"
    }
});

$('#users_table').DataTable({
    processing: true,
    serverSide: true,
    ajax: '/lista_iscritti/iscritti_table/',
    lengthMenu: [[10, 25, 50, -1], [10, 25, 50, "All"]],
    language: {
        url: "//cdn.datatables.net/plug-ins/1.10.20/i18n/Italian.json"
    }
});