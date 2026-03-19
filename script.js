document.getElementById('loginForm').addEventListener('submit', async function(e){
  e.preventDefault();
  const user = document.getElementById('username').value.trim();
  const pass = document.getElementById('password').value;
  const err = document.getElementById('error');
  err.textContent = '';
  if(!user || !pass){ err.textContent = 'Preencha usuário e senha.'; return }

  try{
    const res = await fetch('/login', {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:user,password:pass})});
    const data = await res.json();
    if(res.ok && data.success){ window.location.href = '/dashboard' }
    else{ err.textContent = data.message || 'Credenciais inválidas' }
  }catch(err){ err.textContent = 'Erro de conexão.' }
});
