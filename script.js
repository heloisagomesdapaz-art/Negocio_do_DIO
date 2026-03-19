// ============================================
// ARQUIVO: script.js
// O QUE FAZ: Este arquivo controla o COMPORTAMENTO
// da tela de login. Quando o usuário clica em "Entrar",
// este código envia os dados para o servidor e
// verifica se o login está correto.
// ============================================

// --- PASSO 1: Encontrar os elementos da página ---
// Usamos document.getElementById para "pegar" elementos pelo id
var formulario = document.getElementById('loginForm');
var campoUsuario = document.getElementById('username');
var campoSenha = document.getElementById('password');
var mensagemErro = document.getElementById('error');

// --- PASSO 2: Escutar o envio do formulário ---
// Quando o usuário clica em "Entrar", a função abaixo é executada
formulario.addEventListener('submit', function (evento) {

    // Impede o comportamento padrão do formulário
    // (que seria recarregar a página inteira)
    evento.preventDefault();

    // --- PASSO 3: Ler o que o usuário digitou ---
    // .value = pega o texto digitado no campo
    // .trim() = remove espaços extras no início e no fim
    var usuario = campoUsuario.value.trim();
    var senha = campoSenha.value;

    // Limpa qualquer mensagem de erro anterior
    mensagemErro.textContent = '';

    // --- PASSO 4: Verificar se os campos estão preenchidos ---
    if (!usuario || !senha) {
        mensagemErro.textContent = 'Preencha o usuário e a senha.';
        return; // Para aqui, não continua
    }

    // --- PASSO 5: Enviar os dados para o servidor ---
    // fetch = função que envia dados pela internet
    // Estamos enviando para a rota '/login' do nosso servidor (app.py)
    fetch('/login', {
        method: 'POST',                              // Método POST = dados "escondidos"
        headers: { 'Content-Type': 'application/json' }, // Dizemos que é JSON
        body: JSON.stringify({                        // Convertemos para texto JSON
            username: usuario,
            password: senha
        })
    })
    .then(function (resposta) {
        // --- PASSO 6: Ler a resposta do servidor ---
        // Transforma a resposta em um objeto JavaScript
        return resposta.json().then(function (dados) {
            // Retorna tanto a resposta original quanto os dados
            return { resposta: resposta, dados: dados };
        });
    })
    .then(function (resultado) {
        // --- PASSO 7: Verificar se o login deu certo ---
        if (resultado.resposta.ok && resultado.dados.success) {
            // Login correto! Redireciona para a página dashboard
            window.location.href = '/dashboard';
        } else {
            // Login errado! Mostra a mensagem de erro
            mensagemErro.textContent = resultado.dados.message || 'Usuário ou senha incorretos';
        }
    })
    .catch(function (erro) {
        // --- PASSO 8: Tratar erros de conexão ---
        // Se o servidor estiver fora do ar, mostra esta mensagem
        mensagemErro.textContent = 'Erro de conexão com o servidor.';
    });

});