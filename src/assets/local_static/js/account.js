'use strict';
$(document).ready(function () {
    // Register Form Handler
    let registerForm = $(".register-form")
    let registerFormMethod = registerForm.attr("method")
    let registerFormEndpoint = registerForm.attr('data-endpoint')
    let navigate = registerForm.attr('href')


    function displaySubmitting(submitBtn, defaultText, doSubmit) {
        if (doSubmit) {
            submitBtn.addClass("disabled")
            submitBtn.html("<i class='fa fa-spin fa-spinner'></i> Sending...")
        } else {
            submitBtn.removeClass("disabled")
            submitBtn.html(defaultText)
        }

    }

    registerForm.submit(function (e) { // using instead of onClick
        e.preventDefault()

        let registerFormSubmitBtn = registerForm.find("[type='submit']")
        let registerFormSubmitBtnTxt = registerFormSubmitBtn.text()
        let registerFormData = registerForm.serialize()
        let thisForm = $(this)
        displaySubmitting(registerFormSubmitBtn, "", true)
        console.log(registerFormData)

        $.ajax({
            method: registerFormMethod,
            url: registerFormEndpoint,
            data: registerFormData,
            success: function (data) {
                setTimeout(function () {
                    displaySubmitting(registerFormSubmitBtn, registerFormSubmitBtnTxt, false)
                }, 500)
                window.location.href = navigate;

            },
            error: function (error) {
                let jsonData = error.responseJSON
                let errors =[]
                $.each(jsonData, function (key, value) { 
                   errors.push(value)
                })
                console.log(errors)
                console.log(error)
                setTimeout(function () {
                    displaySubmitting(registerFormSubmitBtn, registerFormSubmitBtnTxt, false)
                }, 500)
            }
        })
    })
})