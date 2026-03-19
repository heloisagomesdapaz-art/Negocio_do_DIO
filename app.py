# ============================================
# ARQUIVO: app.py
# O QUE FAZ: Este é o "cérebro" do nosso site.
# Ele é o SERVIDOR que fica rodando no computador
# e responde quando alguém acessa o site.
# ============================================

# --- PASSO 1: Importar as ferramentas que vamos usar ---
# Flask = é o framework (ferramenta) que cria o servidor web
# request = permite ler os dados que o usuário envia (ex: nome e senha)
# jsonify = transforma dados Python em formato JSON (formato que o navegador entende)
# send_from_directory = envia arquivos HTML para o navegador
from flask import Flask, request, jsonify, send_from_directory

# os = ferramenta do Python para trabalhar com pastas e arquivos
import os

# --- PASSO 2: Descobrir onde estão nossos arquivos ---
# HERE = pasta onde este arquivo app.py está salvo
HERE = os.path.dirname(os.path.abspath(__file__))

# --- PASSO 3: Criar o servidor ---
# Estamos dizendo ao Flask:
# "Os arquivos do site (HTML, CSS, JS) estão na pasta HERE"
app = Flask(__name__, static_folder=HERE, static_url_path='')


# ============================================
# ROTAS = são os "caminhos" do site
# Cada rota responde a um endereço diferente
# ============================================

# --- ROTA 1: Página inicial (tela de login) ---
# Quando alguém acessa http://127.0.0.1:5000/
# o servidor envia o arquivo index.html
@app.route('/')
def pagina_inicial():
    return send_from_directory(HERE, 'index.html')


# --- ROTA 2: Página do dashboard (após fazer login) ---
# Quando alguém acessa http://127.0.0.1:5000/dashboard
# o servidor envia o arquivo dashboard.html
@app.route('/dashboard')
def pagina_dashboard():
    return send_from_directory(HERE, 'dashboard.html')


# --- ROTA 3: Verificar o login ---
# Esta rota recebe o nome de usuário e a senha
# e verifica se estão corretos.
# methods=['POST'] = significa que os dados vêm "escondidos"
# (não aparecem na barra de endereço do navegador)
@app.route('/login', methods=['POST'])
def verificar_login():
    
    # Ler os dados que o navegador enviou (em formato JSON)
    dados = request.get_json() or {}

    # Extrair o nome de usuário e a senha dos dados recebidos
    usuario = dados.get('username')
    senha = dados.get('password')

    # Verificar se o usuário e a senha estão corretos
    # Por enquanto, usamos valores fixos para teste:
    # usuário = "admin" e senha = "secret"
    if usuario == 'admin' and senha == 'secret':
        # Login correto! Retorna sucesso (código 200 = OK)
        return jsonify({'success': True})
    
    # Login errado! Retorna erro (código 401 = Não Autorizado)
    return jsonify({
        'success': False,
        'message': 'Usuário ou senha incorretos'
    }), 401


# --- PASSO 4: Iniciar o servidor ---
# debug=True = mostra erros detalhados no terminal
# (útil enquanto estamos desenvolvendo)
if __name__ == '__main__':
    print("=" * 50)
    print("Servidor rodando!")
    print("Abra no navegador: http://127.0.0.1:5000")
    print("Para parar o servidor: aperte Ctrl + C")
    print("=" * 50)
    app.run(debug=True)