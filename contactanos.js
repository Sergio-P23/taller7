function enviar() {
    let nombre = document.getElementById('name').value;
    let email = document.getElementById('email').value;
    let mensaje = document.getElementById('msg').value;

    Swal.fire({
        title: 'Mensaje Enviado',
        html: `<b>Gracias ${nombre}</b><br>Te responderemos a <i>${email}</i>.`,
        icon: 'success',
        confirmButtonText: 'OK'
    });
}