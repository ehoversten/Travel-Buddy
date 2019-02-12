$(document).ready(function () {
    // Register Form Handler
    let registerForm = $(".register-form")
    let RegisterFormMethod = contactForm.attr("method")
    let actionEndPoint = registerForm.attr('data-endpoint')

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
        displaySubmitting(registerFormSubmitBtnTxt, "", true)
        console.log(registerFormData)
        $.ajax({
            method: RegisterFormMethod,
            url: actionEndPoint,
            data: registerFormData,
            success: function (data) {
                thisForm[0].reset()
                setTimeout(function () {
                    displaySubmitting(registerFormSubmitBtnTxt, registerFormSubmitBtnTxt, false)
                }, 500)

            },
            error: function (error) {
                let jsonData = error.responseJSON
                let errors =[]
                $.each(jsonData, function (key, value) { 
                   error.push(value)
                })
                console.log(error)
                setTimeout(function () {
                    displaySubmitting(contactFormSubmitBtn, registerFormSubmitBtnTxt, false)
                }, 500)
            }
        })
    })

})