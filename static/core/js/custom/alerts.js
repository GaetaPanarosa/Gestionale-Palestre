function toastSuccess(title, message) {
    console.log('Method called');
    $.toast({
        text: title,
        heading: message,
        icon: 'success',
        showHideTransition: 'fade',
        allowToastClose: true,
        hideAfter: 1500,
        position: 'mid-center',
        textAlign: 'left',
        loader: true,
        loaderBg: '#9EC600',
        beforeShow: function () {
        },
        afterShown: function () {
        },
        beforeHide: function () {

        },
        afterHidden: function () {
            location.reload();
        }
    });
    return false;
}

function toastError(title, message) {
    console.log('Method called');
    $.toast({
        text: title,
        heading: message,
        icon: 'error',
        showHideTransition: 'fade',
        allowToastClose: true,
        hideAfter: 1500,
        stack: false,
        position: 'mid-center',
        textAlign: 'left',
        loader: true,
        loaderBg: '#F10918',
        beforeShow: function () {
        },
        afterShown: function () {
        },
        beforeHide: function () {

        },
        afterHidden: function () {
            location.reload();
        }
    });
    return false;
}