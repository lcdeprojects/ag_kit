# Guia de Deploy - Aliada 🚀

Este documento descreve como realizar o deploy do sistema Aliada em produção.

## 1. Preparação do Servidor

Requisitos:
- Servidor Linux (Ubuntu 22.04+ recomendado)
- Docker e Docker Compose instalados

## 2. Configuração do Ambiente

Crie o arquivo `.env` no servidor baseado no `.env.example`:

```bash
cp .env.example .env
```

**Importante**: Ajuste as seguintes variáveis no `.env`:
- `DEBUG=0`
- `SECRET_KEY`: Gere uma chave aleatória forte.
- `ALLOWED_HOSTS`: O seu domínio ou IP do servidor.
- `CSRF_TRUSTED_ORIGINS`: `https://seu-dominio.com` ou `http://IP-DO-SERVIDOR`.

## 3. Comandos de Deploy

Para subir o sistema em produção:

```bash
# Constrói a imagem e inicia os containers em background
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build -d
```

O comando acima irá:
1. Instalar as dependências de produção.
2. Coletar os arquivos estáticos (CSS/JS) via WhiteNoise.
3. Aplicar as migrações do banco de dados automaticamente.
4. Iniciar o servidor Gunicorn com 3 workers.

## 4. Manutenção Útil

### Ver Logs
```bash
docker-compose logs -f web
```

### Criar Super Usuário (Admin)
```bash
docker-compose exec web python manage.py createsuperuser
```

### Backup do Banco (Se usar Postgres)
```bash
docker-compose exec db pg_dump -U aliada_user aliada_db > backup.sql
```

## 5. SSL (HTTPS)
Recomendamos o uso de um Proxy Reverso como **Nginx + Certbot** à frente do container Docker para gerenciar o certificado SSL gratuitamente.
