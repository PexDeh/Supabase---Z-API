# Supabase Z-API Broadcast

Projeto para o desafio de estágio da b2bflow.

## O que faz

Lê contatos do Supabase e tenta enviar mensagem personalizada via Z-API.

## Setup

1. Criar tabela `contacts` no Supabase com os campos:

- `name` (string)
- `phone` (string)

2. Criar arquivo `.env` na raiz do projeto com as variáveis:

SUPABASE_URL=https://fahuqxbuvnstnqvqxtzi.supabase.co

SUPABASE_ANON_KEY= eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZhaHVxeGJ1dm5zdG5xdnF4dHppIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTUwMDgxNzAsImV4cCI6MjA3MDU4NDE3MH0.dzZ1muUWON4ihvJtPwFXG8nJ2a3-SEyUaHBZbc1d8kI


ZAPI_BASE_URL=https://api.z-api.io/instances/3E59DA8CA819306A6A17DE1025393F89/token/EE51D6A5394C45BB109B5087/send-text


ZAPI_INSTANCE_ID= 3E59DA8CA819306A6A17DE1025393F89

ZAPI_TOKEN= EE51D6A5394C45BB109B5087

DRY_RUN=false
MAX_MESSAGES=3



## Como rodar

No terminal, estando na pasta do projeto, rode:

```bash
python src/main.py


Observação importante
O envio via Z-API está retornando erro NOT_FOUND — estou investigando.

Atualmente o envio de mensagens está sendo feito em modo dry run (apenas simulação)
