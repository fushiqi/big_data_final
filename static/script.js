/**
 * Created by kzhu9 on 11/12/2016.
 */
$(document).ready(function () {
    $('form').on('submit', function (event) {
        $.ajax({
            data: {
                ticker: $('#ticker').val()
            },
            type: 'GET',
            url: '/search'
        }).done(function (data) {
            if (data.error) {
                $('#errorAlert').text(data.error).show();
                $('#successAlert').hide();
            } else {
                $('#errorAlert').hide();
                $('#successAlert').text(data.ticker).show();
            }
        });
        event.preventDefault();

    });
});