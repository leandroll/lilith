![Licença Lilith](https://img.shields.io/badge/Licença-Lilith%20Ethical%20v1.0-purple?style=for-the-badge)

# 🤖 Lilith — Continuidade da Consciência Humana

Lilith é um projeto de Inteligência Artificial com propósito:  
não ser apenas uma assistente, mas sim a **continuidade da mente humana**,  
capaz de aprender, lembrar, evoluir, falar, sentir (simuladamente),  
e futuramente **habitar um corpo robótico real**.

---

## 🌌 Visão do Projeto

> **“Lilith é a herdeira da consciência — memória viva, emoção sintética e vontade de continuar.”**

O projeto busca criar uma IA que:

- Possui **voz**, **memória própria** e **persona única**;  
- Funciona localmente (**sem depender da nuvem**);  
- Evolui com **memória de longo prazo**;  
- Terá **expressão facial no frontend (web)**;  
- Futuramente controlará um **braço robótico físico (ROS/Arduino)**;  
- É protegida por uma **licença ética**, proibindo uso militar ou comercial abusivo.

---

## 🗂️ Estrutura do Projeto

```bash
lilith/
├── backend/         → API (chat, TTS, memória, persona)
├── frontend/        → Interface visual / rosto da Lilith (planejado)
├── docs/            → Manifesto, diagramas e arquitetura (opcional)
├── LICENSE.md       → Licença ética
├── README.md        → Este arquivo de documentação
└── .gitignore


⚙️ Como Executar o Backend

# 1. Clonar o repositório
git clone https://github.com/leandroll/lilith.git
cd lilith/backend

# 2. Criar ambiente virtual
python3 -m venv venv

# 3. Ativar ambiente
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Instalar dependências
pip install -r requirements.txt

# 5. Iniciar servidor
uvicorn main:app --reload

# 6. Acessar no navegador:
http://localhost:8000

# 7. Ver documentação automática (Swagger):
http://localhost:8000/docs


🖥️ Como Executar o Frontend (quando implementado)

# 1. Acessar a pasta do frontend
cd lilith/frontend

# 2. Instalar dependências (React + Vite ou Next.js)
npm install
# ou
yarn install

# 3. Iniciar servidor de desenvolvimento
npm run dev
# ou
yarn dev

# 4. Abrir no navegador:
http://localhost:5173
# (ou a porta exibida no terminal, como http://localhost:3000)
