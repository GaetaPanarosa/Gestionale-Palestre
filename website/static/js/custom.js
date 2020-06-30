$(document).ready(function (event) {
    $('#terms').click(function () {
        if ($(this).prop('checked') === true) {
            $('#register').removeAttr('disabled');
        } else {
            event.preventDefault();
        }
    });

    function login() {

    }

    function register(){

    }
})
