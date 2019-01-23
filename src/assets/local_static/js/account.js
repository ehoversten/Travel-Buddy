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

    /* I could make this form reusable for the two forms but at the moment seems better to separate them. 1/22/19 */

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
    // Login Form Handler
    let loginForm = $(".login-form")
    let loginFormMethod = loginForm.attr("method")
    let loginFormEndpoint = loginForm.attr('data-endpoint')
    // let navigate = loginForm.attr('href')


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

    loginForm.submit(function (e) { // using instead of onClick
        e.preventDefault()

        let loginFormSubmitBtn = loginForm.find("[type='submit']")
        let loginFormSubmitBtnTxt = loginFormSubmitBtn.text()
        let loginFormData = loginForm.serialize()
        let thisForm = $(this)
        displaySubmitting(loginFormSubmitBtn, "", true)
        console.log(loginFormData)

        $.ajax({
            method: loginFormMethod,
            url: loginFormEndpoint,
            data: loginFormData,
            success: function (data) {
                setTimeout(function () {
                    displaySubmitting(loginFormSubmitBtn, loginFormSubmitBtnTxt, false)
                }, 500)
                // window.location.href = navigate;
                console.log("It works! we guchi")

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
                    displaySubmitting(loginFormSubmitBtn, loginFormSubmitBtnTxt, false)
                }, 500)
            }
        })
    })
})