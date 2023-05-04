// Função responsável por alterar a visibilidade da senha.
const togglePassword = document.querySelector('#toggle-password');
  const password = document.querySelector('#password');

  togglePassword.addEventListener('click', function (e) {
    // Altera o tipo de input. Possibilita tornar visível/invisível a senha
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
    // Altera o ícone com o olho/olho cortado
    this.classList.toggle('fa-eye-slash');
});