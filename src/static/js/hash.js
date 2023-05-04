const form = document.getElementById('form');
const passwordInput = document.getElementById('password');
const passwordHashInput = document.getElementById('password-hash');

async function generatePasswordHash(password) {
    if(password == "") {
      return "0";
    }
    if(password.length < 6) {
      return "1";
    }

    const encoder = new TextEncoder();
    const data = encoder.encode(password);
    const hashBuffer = await crypto.subtle.digest('SHA-256', data);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
    return hashHex;
  }
  

form.addEventListener('submit', async (event) => {
  const password = passwordInput.value;
  const passwordHash = await generatePasswordHash(password);
  passwordHashInput.value = passwordHash;

  // Envia o formulário
  form.submit();
});