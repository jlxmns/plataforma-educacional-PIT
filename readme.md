# Projeto Interdisciplinar · Plataforma Educacional

API RESTful construída com **Django** e **PostgreSQL** para servir o front da Plataforma Educacional.

## Sumário
- [Funcionalidades Implementadas](#funcionalidades-implementadas)
- [Stack](#stack)
- [Pré-requisitos](#pré-requisitos)
- [Como rodar](#como-rodar)
- [Credenciais de Acesso](#credenciais-de-acesso)
- [Documentação da API](#documentação-da-api)
- [Autenticação e Autorização](#autenticação-e-autorização)
- [Modelagem](#modelagem)
- [Testes Unitários](#testes-unitários)

## Funcionalidades Implementadas

### Func 1
- Blablabla
- Blablabla
- Blablabla

### Func 2
- Bleblebl
- Blebleb
- Blebleb

## Stack

- **Linguagem:** Python 3.13
- **Framework:** Django 5.2 + Django Ninja
- **Banco de Dados:** PostgreSQL 16
- **Containerização:** Docker + Docker Compose
- **Documentação:** Swagger
- **Gerenciamento de Dependências:** Poetry

## Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Como rodar

- Clone o repositório
- Crie um arquivo .env na root do projeto. Você pode copiar as configurações disponíveis no arquivo .env.sample.
- Inicie os containers:

```
docker-compose -f docker-compose.yml up -d
```

- Acesse a aplicação:

```
API: http://localhost:8000/api
Documentação Swagger: http://localhost:8000/api/docs
Admin Django: http://localhost:8000/admin
```

## Credenciais de Acesso

- Um usuário administrador será criado automaticamente ao iniciar o projeto. As informações de login são:

```
email: admin@admin.com
senha: admin
```

- Uma Token de autenticação também será gerada automaticamente. Você pode pegar ela através do painel de administrador, na seção de "AuthToken", ou fazendo uma requisição de login à API.
- O endpoint de login é: http://localhost:8000/api/auth/login

## Documentação da API

A documentação Swagger da API está disponível em http://localhost:8000/api/docs.

### Principais Endpoints

#### Autenticação (`/api/auth`)
- `POST /auth/login` - Fazer login e obter token
- `GET /auth/user` - Obter dados do usuário autenticado
- `GET /auth/token` - Obter token do usuário

## Autenticação e Autorização

A autenticação é feita através de tokens de autorização. Quando um usuário é criado no sistema, uma token é gerada e associada automaticamente à ele.
Essa token deve ser enviada nos requests à API, pelo header `X-API-Key`.

A autorização é atribuida durante a criação do usuário. Usuários criados pelo administrador têm permissão de cliente, e podem acessar apenas os endpoints disponíveis nas seções `auth` e `common`.
O administrador também tem acesso aos endpoints em `management`.

Quando os requests são feitos, o sistema encontra o usuário associado à Token enviada no request e verifica a permissão.

## Modelagem

Falar da modelagem

## Testes Unitários

O projeto tem testes unitários para todos os endpoints.

É possível executar os testes com o comando: `docker-compose exec web python manage.py test`
