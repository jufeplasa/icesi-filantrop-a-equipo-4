// custom.js
document.getElementById('edit-button').addEventListener('click', function () {
    alert('Botón "Editar" clickeado');
    document.getElementById('info-form').style.display = 'none';
    document.getElementById('edit-form').style.display = 'block';
});