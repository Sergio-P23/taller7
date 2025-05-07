contact_js = function enviar() {
    let email = document.getElementById('email').value;
    let msg = document.getElementById('msg').value;
    alert("Gracias por contactarnos " + email);
    document.getElementById('output').textContent = "Tu mensaje fue: " + msg;
}


