'use strict';
$(document).ready(function () {
    $('#errors').hide()
    // Register Form Handler
    let registerForm = $(".register-form")
    let registerFormMethod = registerForm.attr("method")
    let registerFormEndpoint = registerForm.attr('data-endpoint')
    let navigate = registerForm.attr('href')
    // console.log(navigate)



    function displaySubmitting(submitBtn, defaultText, doSubmit) {
        if (doSubmit) {
            submitBtn.addClass("disabled")
            submitBtn.html("<i class='fa fa-spin fa-spinner'></i> Sending...")
        } else {
            submitBtn.removeClass("disabled")
            submitBtn.html(defaultText)
        }

    }

    /* I could make this form reusable for the two forms but at the moment seems better to separate them. 1/22/19 */

    registerForm.submit(function (e) { // using instead of onClick
        e.preventDefault()

        let registerFormSubmitBtn = registerForm.find("[type='submit']")
        let registerFormSubmitBtnTxt = registerFormSubmitBtn.text()
        let registerFormData = registerForm.serialize()
        let thisForm = $(this)
        displaySubmitting(registerFormSubmitBtn, "", true)
        // console.log(registerFormData)
        let error_tag = $('#errors')

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
                let errors = []
                $.each(jsonData, function (key, value) {
                    errors.push(value)
                })
                for (let err of errors) {
                    error_tag.html(`<p>${err[0]["message"]}</p>`)
                }
                error_tag.show()
                
                setTimeout(function () {
                    displaySubmitting(registerFormSubmitBtn, registerFormSubmitBtnTxt, false)
                }, 500)
            }
        })
    })
    // Login Form Handler
    let loginForm = $(".login-form")
    let loginFormMethod = loginForm.attr("method")
    let loginFormEndpoint = loginForm.attr('data-endpoint')
    let _navigate = loginForm.attr('href')


    function displaySubmitting(submitBtn, defaultText, doSubmit) {
        if (doSubmit) {
            submitBtn.addClass("disabled")
            submitBtn.html("<i class='fa fa-spin fa-spinner'></i> Sending...")
        } else {
            submitBtn.removeClass("disabled")
            submitBtn.html(defaultText)
        }

    }


    loginForm.submit(function (e) { // using instead of onClick
        e.preventDefault()

        let loginFormSubmitBtn = loginForm.find("[type='submit']")
        let loginFormSubmitBtnTxt = loginFormSubmitBtn.text()
        let loginFormData = loginForm.serialize()
        let thisForm = $(this)
        let error_p = $('#errors')
        displaySubmitting(loginFormSubmitBtn, "", true)

        $.ajax({
            method: loginFormMethod,
            url: loginFormEndpoint,
            data: loginFormData,
            success: function (data) {
                setTimeout(function () {
                    displaySubmitting(loginFormSubmitBtn, loginFormSubmitBtnTxt, false)
                }, 500)
                window.location.href = _navigate;

            },
            error: function (error) {
                let jsonData = error.responseJSON
                let errors = []
                $.each(jsonData, function (key, value) {
                    errors.push(value)
                })
                // console.log(errors) // message we want to render
                for (let err of errors) {
                    error_p.html(`<p>${ err[0]["message"]}</p>`)
                }
                error_p.show()
                setTimeout(function () {
                    displaySubmitting(loginFormSubmitBtn, loginFormSubmitBtnTxt, false)
                }, 500)
            }
        })
    })
})


// using Generator on error
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*