# Módulo de Atenticação

Sistema full stack para autenticação e gerenciamento de usuários utilizando FastAPI no backend e Nuxt 4 no frontend, com autenticação JWT, integração com Supabase e arquitetura moderna baseada em APIs.

---

## Tecnologias Utilizadas

### Backend
- Python 3.13
- FastAPI
- FastAPI Users
- SQLAlchemy
- JWT Authentication
- Async/Await
- PostgreSQL
- Supabase
- Resend
- Pydantic 

### Frontend
- Nuxt 4.4.4
- Nuxt UI 4.7.1
- Zod 4.4.3
- TypeScript

---

# Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de fornecer uma estrutura moderna e escalável para autenticação e gerenciamento de usuários.

A aplicação implementa:

- Gerenciamento de usuários
- Login com JWT
- Autenticação baseada em tokens
- Recuperação de senha
- Verificação de e-mail
- Integração entre frontend e backend
- API assíncrona utilizando FastAPI
- Persistência de dados com Supabase/PostgreSQL

O sistema foi construído seguindo boas práticas de arquitetura backend e frontend, utilizando validação tipada, autenticação segura e comunicação desacoplada via API REST.

---

# Arquitetura

```mermaid
flowchart LR

    %% Frontend
    subgraph Frontend
        NUXT["Nuxt 4"]
        UI["Nuxt UI"]
        ZOD["Zod"]
    end

    %% Backend
    subgraph Backend
        FASTAPI["FastAPI"]
        USERS["FastAPI Users"]
        JWT["JWT Auth"]
        PYDANTIC["Pydantic"]
    end

    %% Persistence
    subgraph Persistência
        SQLA["SQLAlchemy ORM"]
    end

    %% Database
    subgraph Banco de Dados
        SUPABASE["Supabase PostgreSQL"]
    end

    %% Flow
    NUXT --> FASTAPI
    UI --> NUXT
    ZOD --> NUXT

    FASTAPI --> USERS
    FASTAPI --> JWT
    FASTAPI --> PYDANTIC
    FASTAPI --> SQLA

    SQLA --> SUPABASE
```

---

# Diagrama de Sequência do login e do acesso às rotas protegidas.

```mermaid
sequenceDiagram
    autonumber

    actor User as User
    participant Frontend as Nuxt Frontend
    participant API as FastAPI Backend
    participant Auth as FastAPI Users / JWT
    participant Validation as Pydantic
    participant ORM as SQLAlchemy ORM
    participant DB as Supabase PostgreSQL

    %% =========================
    %% USER LOGIN FLOW
    %% =========================

    User->>Frontend: Página de Login
    Frontend->>Frontend: Validação do Formulário com Zod

    Frontend->>API: POST /auth/jwt/login

    API->>Validation: Schema de Validação da Requisição
    Validation-->>API: Dado Validado

    API->>Auth: Credenciais para Autenticação do Usuário

    Auth->>ORM: Buscar Usuário
    ORM->>DB: SELECT user by email
    DB-->>ORM: Dados do Usuário
    ORM-->>Auth: User Entity

    Auth->>Auth: Verificar Senha
    Auth->>Auth: Gerar JWT Token

    Auth-->>API: Usuário autenticado + JWT
    API-->>Frontend: Retorna Access Token

    Frontend->>Frontend: Armazena JWT Token

    %% =========================
    %% AUTHENTICATED REQUEST
    %% =========================

    User->>Frontend:Acesso à rota protegida

    Frontend->>API: GET /users/me (JWT)

    API->>Auth: Validar JWT Token
    Auth-->>API: Usuário Autenticado

    API->>ORM: Busca Dados do Usuário
    ORM->>DB: SELECT user
    DB-->>ORM: Registro do Usuário
    ORM-->>API: Objeto Usuario(User)

    API-->>Frontend: Retorna os Dados do Usuário
    Frontend-->>User: Renderiza Página
```

---

# Funcionalidades

## Autenticação
- Login
- Logout
- Autenticação JWT
- Refresh Token
- Proteção de rotas

## Usuários
- Cadastro de usuários
- Edição de perfil
- Exclusão de perfil
- Consulta de perfil


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
| Pydantic | Schemas para validação de dados da requisição|
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
auth/
│
├── backend/
│   │
│   ├── .venv/                 # Virtual environment
│   ├── app/                   # FastAPI application
│   │   ├── routes/            # API routes
│   │   │   ├── auth.py        # Rotas para autenticação.
│   │   │   ├── user.py        # Rotas para regrenciamento do usuário.
│   │   ├── schemas/           # Pydantic schemas
│   │   │   ├── user.py        # Schema pydantic do usuário.
│   │   ├── models/            # Modelos do SQLAlchemy
│   │   │   ├── base.py        # Modelo base a ser importado por todos os modelos.
│   │   │   ├── user.py        # Modelo do usuário criado pelo FastApi Users com algumas modificações.
│   │   ├── services/          # Regra de negócio e serviços
│   │   │   ├── email.py       # Código para tratamento de emails de confirmação com resend.
│   │   ├── auth/              # Configuração do sistema de autenticação.
│   │   │   ├── user.py        # Configuração central do sistema de autenticação e gerenciamento de usuários utilizando FastAPI Users, JWT, SQLAlchemy assíncrono e PostgreSQL.
│   │   ├── static/            # Imagens e etc.
│   │   ├── db.py              # Configuração do Banco de Dados
│   │   ├── create_db.py       # Criação do Banco de Dados
│   │   ├── config.py          # Schema pydantic para as variáveis de ambiente
│   │   └── main.py            # FastAPI entrypoint
│   │
│   ├── requirements.txt       # Python dependencies
│   └── README.md
│
├── frontend/
│   │
│   ├── pages/                 # Application pages
│   ├── components/            # Reusable UI components
│   ├── composables/           # Vue/Nuxt composables
│   ├── middleware/            # Route middleware
│   ├── public/                # Static assets
│   ├── app.vue                # Root component
│   ├── nuxt.config.ts         # Nuxt configuration
│   └── package.json           # Node dependencies
│
├── .gitignore
└── README.md
```

---

# Como Executar o Projeto

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

# Variáveis de Ambiente

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

# Endpoints Principais

## Auth

```http
POST /auth/register                # Rota para cadastro de usuários
POST /auth/jwt/login               # Rota para login
POST /auth/jwt/logout              # Rota para logout
POST /auth/forgot-password         # Inicia o processo de recuperação de senha enviando um token de redefinição para o e-mail do usuário.
POST /auth/reset-password          # Valida o token de recuperação recebido e define uma nova senha para o usuário.
POST /auth/verify-request-token    # Solicita o envio do token de verificação de e-mail para confirmação da conta do usuário após o cadastro.
POST /auth/verify                  # Valida o token de verificação e confirma o e-mail do usuário, marcando a conta como verificada.
```
## Users

```http
PATCH /users/me                    # Atualiza os dados do usuário atualmente autenticado.
GET /users/{id}                    # Retorna os dados de um usuário específico através do ID.
PATCH /users/{id}                  # Atualiza os dados de um usuário específico através do ID.
DELETE /users/{id}                 # Remove um usuário específico do sistema através do ID.

```
## Default (Customizada)

```http
GET /users/me                      # Retorna os dados completos do usuário autenticado atualmente.
GET /users/by-email/{email}        # Busca e retorna um usuário específico através do endereço de e-mail.
DELETE /users/by-email/{email}     # Remove um usuário do sistema utilizando o endereço de e-mail.
```
---

# Objetivos do Projeto

- Estudo de arquitetura full stack moderna
- Implementação de autenticação segura
- Integração entre FastAPI e Nuxt
- Utilização de APIs assíncronas
- Aplicação de boas práticas de desenvolvimento

---

# Melhorias Futuras

- Refresh token seguro com cookies HTTPOnly
- Controle de permissões (RBAC)
- Dockerização
- Deploy em cloud
- Testes automatizados
- OAuth2 (Google/GitHub)
- Painel administrativo

---

# Conceitos Aplicados

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

GitHub: https://github.com/rmcfdma
