# Auth System — Full Stack User Management

Sistema full stack para autenticação e gerenciamento de usuários utilizando FastAPI no backend e Nuxt no frontend, com autenticação JWT, integração com Supabase e arquitetura moderna baseada em APIs.

---

## 🚀 Tecnologias Utilizadas

### Backend
- Python
- FastAPI
- FastAPI Users
- SQLAlchemy
- JWT Authentication
- Async/Await
- PostgreSQL
- Supabase

### Frontend
- Nuxt 4.4.4
- Nuxt UI 4.7.1
- Zod 4.4.3
- TypeScript

---

# 📌 Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de fornecer uma estrutura moderna e escalável para autenticação e gerenciamento de usuários.

A aplicação implementa:

- Registro de usuários
- Login com JWT
- Autenticação baseada em tokens
- Gerenciamento de usuários
- Recuperação de senha
- Verificação de e-mail
- Integração entre frontend e backend
- API assíncrona utilizando FastAPI
- Persistência de dados com Supabase/PostgreSQL

O sistema foi construído seguindo boas práticas de arquitetura backend e frontend, utilizando validação tipada, autenticação segura e comunicação desacoplada via API REST.

---

# 🏗️ Arquitetura

```text
Frontend (Nuxt 4)
        ↓
 REST API
        ↓
Backend (FastAPI)
        ↓
SQLAlchemy ORM
        ↓
Supabase PostgreSQL
```

---

# 🔐 Funcionalidades

## Autenticação
- Cadastro de usuários
- Login
- Logout
- Refresh Token
- Proteção de rotas
- Autenticação JWT

## Usuários
- Consulta de perfil
- Atualização de dados
- Gerenciamento de usuários

## Segurança
- Hash de senhas
- Tokens JWT
- Validação de dados
- Verificação de e-mail
- Recuperação de senha

---

# ⚙️ Backend

## Principais Tecnologias

| Tecnologia | Função |
|---|---|
| FastAPI | API REST assíncrona |
| FastAPI Users | Sistema de autenticação |
| SQLAlchemy | ORM |
| JWT | Autenticação |
| Supabase | Banco de dados PostgreSQL |

---

# 💻 Frontend

## Principais Tecnologias

| Tecnologia | Função |
|---|---|
| Nuxt 4 | Framework frontend |
| Nuxt UI | Componentes de interface |
| Zod | Validação de schemas |
| TypeScript | Tipagem estática |

---

# 📂 Estrutura do Projeto

```text
project/
│
├── backend/
│   ├── app/
│   ├── routes/
│   ├── schemas/
│   ├── models/
│   ├── services/
│   └── main.py
│
├── frontend/
│   ├── pages/
│   ├── components/
│   ├── composables/
│   ├── middleware/
│   └── app.vue
│
└── README.md
```

---

# 🚀 Como Executar o Projeto

## Backend

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Executar servidor

```bash
uvicorn app.main:app --reload
```

---

## Frontend

### Instalar dependências

```bash
npm install
```

### Executar aplicação

```bash
npm run dev
```

---

# 🔑 Variáveis de Ambiente

## Backend

```env
DATABASE_URL=
SECRET=
SUPABASE_URL=
SUPABASE_KEY=
```

## Frontend

```env
NUXT_PUBLIC_API_URL=
```

---

# 📡 Endpoints Principais

## Auth

```http
POST /auth/register
POST /auth/jwt/login
POST /auth/forgot-password
POST /auth/reset-password
POST /auth/verify
```

## Users

```http
GET /users/me
PATCH /users/me
GET /users/{id}
```

---

# 🎯 Objetivos do Projeto

- Estudo de arquitetura full stack moderna
- Implementação de autenticação segura
- Integração entre FastAPI e Nuxt
- Utilização de APIs assíncronas
- Aplicação de boas práticas de desenvolvimento

---

# 📈 Melhorias Futuras

- Refresh token seguro com cookies HTTPOnly
- Controle de permissões (RBAC)
- Dockerização
- Deploy em cloud
- Testes automatizados
- OAuth2 (Google/GitHub)
- Painel administrativo

---

# 🛠️ Conceitos Aplicados

- Clean Architecture
- Dependency Injection
- Async Programming
- JWT Authentication
- ORM
- API REST
- Schema Validation
- Type Safety

---

# 📄 Licença

Este projeto está sob a licença MIT.

---

# 👨‍💻 Autor

Rodrigo Costa

GitHub: https://github.com/seuusuario
