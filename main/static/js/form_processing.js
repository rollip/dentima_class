function process_form(e)
{
    e.preventDefault();
    const submit = document.getElementById('submit')
    const name = document.getElementById('name').value
    const email = document.getElementById('email').value
    const phone = document.getElementById('phone').value
    const application_form = {
        name : name,
        email: email,
        phone: phone
    }

    submit.classList.add("success");
    let xhr = new XMLHttpRequest();

    let application_form_json = JSON.stringify(application_form);

    xhr.open("POST", '/seminar/send_email');
    xhr.send(application_form_json);
}