const form = document.querySelector('#sensei');
const input = document.querySelector('#inputContador');

form.addEventListener('submit', (e) => {
    if (parseInt(input.value) >= 0) {
        return true;
    } else {
        e.preventDefault();
        alert('Ingrese un número positivo')
    }
});