# Tela de Login - Projeto Escola

## O que é este projeto?

Este é um **sistema de login simples** feito para aprender como funciona um site com:

- **Frontend** (o que o usuário vê): HTML, CSS e JavaScript
- **Backend** (o que roda no servidor): Python com Flask

Quando o usuário digita o nome e a senha corretos, ele é redirecionado para uma página de boas-vindas (dashboard).

---

## Estrutura dos arquivos

```
Negocio_do_DIO/
│
├── .gitignore          ← Arquivos que o Git deve ignorar (ex: venv/)
├── app.py              ← Servidor (cérebro do site)
├── index.html          ← Tela de login (o que o usuário vê primeiro)
├── dashboard.html      ← Página após o login
├── styles.css          ← Visual da tela de login (cores, tamanhos)
├── script.js           ← Lógica do login (o que acontece ao clicar "Entrar")
├── requirements.txt    ← Lista de bibliotecas Python necessárias
└── README.md           ← Este arquivo (instruções do projeto)
```

---

## Como rodar o projeto no seu computador

### Pré-requisitos

Você precisa ter instalado:

- **Python 3** (versão 3.8 ou superior)
- **pip** (gerenciador de pacotes do Python - já vem com o Python)
- **Git** (para clonar o repositório)

### Passo 1 - Clonar o repositório

Abra o terminal e digite:

```bash
git clone https://github.com/heloisagomesdapaz-art/Negocio_do_DIO.git
```

Depois entre na pasta do projeto:

```bash
cd Negocio_do_DIO
```

### Passo 2 - Criar o ambiente virtual

O ambiente virtual é uma "caixinha" separada para as bibliotecas do projeto.
Isso evita conflitos com outros projetos no seu computador.

```bash
python3 -m venv venv
```

Agora ative o ambiente virtual:

**No Linux ou Mac:**
```bash
source venv/bin/activate
```

**No Windows:**
```bash
venv\Scripts\activate
```

Quando o ambiente estiver ativo, vai aparecer `(venv)` no início da linha do terminal.

### Passo 3 - Instalar as dependências

```bash
pip install -r requirements.txt
```

Isso instala o Flask (a ferramenta que cria o servidor).

### Passo 4 - Rodar o servidor

```bash
python3 app.py
```

Você vai ver algo assim no terminal:

```
==================================================
Servidor rodando!
Abra no navegador: http://127.0.0.1:5000
Para parar o servidor: aperte Ctrl + C
==================================================
```

### Passo 5 - Abrir no navegador

Abra o navegador (Chrome, Firefox, etc.) e acesse:

```
http://127.0.0.1:5000
```

### Passo 6 - Testar o login

Use estas credenciais de teste:

| Campo   | Valor    |
|---------|----------|
| Usuário | `admin`  |
| Senha   | `secret` |

Se digitar certo, vai para a página de **Bem-vindo!**
Se digitar errado, aparece uma mensagem de erro em vermelho.

### Passo 7 - Parar o servidor

No terminal, aperte **Ctrl + C** para parar o servidor.

---

## Como contribuir (enviar suas alterações)

### Passo 1 - Criar sua branch

```bash
git checkout -b seu-nome
```

Exemplo:

```bash
git checkout -b maurizio
```

### Passo 2 - Fazer suas alterações

Edite os arquivos que precisar.

### Passo 3 - Salvar as alterações no Git

```bash
git add .
git commit -m "Descreva o que você fez aqui"
```

Exemplo:

```bash
git add .
git commit -m "Refatorei o código com comentários didáticos"
```

### Passo 4 - Enviar para o GitHub

```bash
git push origin seu-nome
```

Exemplo:

```bash
git push origin maurizio
```

### Passo 5 - Criar um Pull Request (PR)

1. Acesse o repositório no GitHub
2. Vai aparecer um botão **"Compare & pull request"**
3. Clique nele
4. Escreva uma descrição do que você fez
5. Clique em **"Create pull request"**

Pronto! Agora é só esperar a dona do repositório aceitar suas alterações.

---

## Credenciais de teste

- **Usuário:** `admin`
- **Senha:** `secret`

---

## Tecnologias usadas

- **Python 3** - linguagem de programação do backend
- **Flask** - framework web para Python
- **HTML5** - estrutura das páginas
- **CSS3** - visual e estilo das páginas
- **JavaScript** - lógica e interatividade no navegador