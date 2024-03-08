function process_form(e)
{
    function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
    const csrftoken = getCookie('csrftoken');



    e.preventDefault();
    const url = "/send_email";
    fetch(url, {
    method : "POST",
    headers: {'X-CSRFToken': csrftoken,
               'Content-type': 'application/json'
               },
    body : JSON.stringify({
        name : document.getElementById('name').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,
        page: document.URL
    })
}).then(
    response => response.text() // .json(), etc.
    // same as function(response) {return response.text();}
).then(
    html => console.log(html)
);
    submit.classList.add("success");
    a = document.getElementById('form-success')
    a.style.display = 'block'
}