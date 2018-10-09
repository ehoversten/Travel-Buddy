$(document).ready(function () {

    $('.form_container').hide();

    $('#add_trip_btn').click(function () {
        // console.log("add trip form toggled");
        $('.form_container').slideToggle("swing");
    });


    $('#ajax_btn').click(function () {
        console.log("ajax button clicked");
        $.ajax({
            url: 'travels/ajax_testing',
            success: function (serverResponse) {
                console.log("success, Server Response: ", serverResponse);
            }
        })
    });

    $('#add_trip_ajax_form').submit(function (e) {
        e.preventDefault();
        console.log("ajax form submission");
        $.ajax({
            url: $(this).attr('action'),
            method: 'post',
            data: $(this).serialize(),
            success: function (serverResponse) {
                console.log("success, Server Response: ", serverResponse);
                $('#placeholder3').html(serverResponse)
            }
        })
    })



});