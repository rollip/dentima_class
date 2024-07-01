document.addEventListener('DOMContentLoaded', function () {
    const forms = document.querySelectorAll('form.needs-validation');

    forms.forEach(form => {
        let validationActive = false;

        form.addEventListener('submit', function (event) {
            event.preventDefault();
            event.stopPropagation();

            validationActive = true;
            if (validateForm(form)) {
                processFeedbackForm(event, form);
            }
        }, false);

        const inputs = form.querySelectorAll('.name, .phone, .email');
        inputs.forEach(input => {
            input.addEventListener('input', function () {
                if (validationActive) {
                    validateInput(input);
                    form.classList.remove('was-validated');
                }
            });
        });
    });
});

function validateForm(form) {
    let isValid = true;

    const name = form.querySelector('.name');
    const phone = form.querySelector('.phone');
    const email = form.querySelector('.email');

    if (!validateInput(name)) isValid = false;
    if (!validateInput(phone)) isValid = false;
    if (!validateInput(email)) isValid = false;

    return isValid;
}

function validateInput(input) {
    let isValid = true;

    if (input.classList.contains('name')) {
        if (input.value.trim() === '') {
            input.classList.add('is-invalid');
            input.classList.remove('is-valid');
            isValid = false;
        } else {
            input.classList.remove('is-invalid');
            input.classList.add('is-valid');
        }
    }

    if (input.classList.contains('phone')) {
        const phonePattern = /^[\d()+\- ]{7,20}$/;
        if (!phonePattern.test(input.value)) {
            input.classList.add('is-invalid');
            input.classList.remove('is-valid');
            isValid = false;
        } else {
            input.classList.remove('is-invalid');
            input.classList.add('is-valid');
        }
    }

    if (input.classList.contains('email')) {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(input.value)) {
            input.classList.add('is-invalid');
            input.classList.remove('is-valid');
            isValid = false;
        } else {
            input.classList.remove('is-invalid');
            input.classList.add('is-valid');
        }
    }

    return isValid;
}

function processFeedbackForm(e, form) {
    const csrftoken = getCookie('csrftoken');

    fetch("/send_email", {
        method: "POST",
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-type': 'application/json'
        },
        body: JSON.stringify({
            name: form.querySelector('.name').value,
            email: form.querySelector('.email').value,
            phone: form.querySelector('.phone').value,
            page: document.URL,
            form_id: form.id
        })
    }).then(
        response => response.text()
    ).then(
        html => console.log(html)
    );

    const alert = form.querySelector('.alert-success');
    alert.classList.remove("d-none");
    alert.classList.add("d-flex");
    setTimeout(function(){
        alert.classList.remove("d-flex");
        alert.classList.add("d-none");
    }, 5000);
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
