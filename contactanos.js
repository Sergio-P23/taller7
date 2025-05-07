function enviar() {

        event.preventDefault(); // Prevenir el comportamiento predeterminado del formulario
        const email = document.getElementById('email').value;
        const msg = document.getElementById('msg').value;
        alert("Gracias por contactarnos " + email);
        document.getElementById('output').textContent = "Tu mensaje fue: " + msg;
}