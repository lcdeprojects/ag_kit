# Guia de Deploy - Aliada 🚀

Este documento descreve como realizar o deploy do sistema Aliada em produção.

## 1. Preparação do Servidor

Requisitos:
- Servidor Linux (Ubuntu 22.04+ recomendado) ou conta no Railway
- Docker e Docker Compose instalados

## 1.1 Railway - Linkando o Banco de Dados
Para que o sistema funcione no Railway, você **deve** ter um serviço de PostgreSQL no mesmo projeto. 
No painel do Railway:
1. Clique no seu serviço de aplicação (**web/app**).
2. Vá em **"Connect"** ou **"Data"**.
3. Certifique-se de que a variável `DATABASE_URL` está aparecendo. Se não estiver, clique em **"Create Reference"** e selecione o seu banco PostgreSQL.

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
- `DJANGO_SUPERUSER_USERNAME`: `admin` (opcional)
- `DJANGO_SUPERUSER_EMAIL`: `lcdeksb@gmail.com` (opcional)
- `DJANGO_SUPERUSER_PASSWORD`: `Aliada@admin26` (opcional)

## 3. Automação de Infraestrutura
O sistema agora cria o usuário admin automaticamente no primeiro deploy se você definir as variáveis acima.

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

### No Railway (Painel)
1. Vá no seu serviço do Aliada no Railway.
2. Clique na aba **"Terminal"**.
3. Digite: `python manage.py createsuperuser` e siga as instruções.

### No Railway (CLI)
Se você tiver a CLI do Railway instalada:
```bash
railway run python manage.py createsuperuser
```

### Backup do Banco (Se usar Postgres)
```bash
docker-compose exec db pg_dump -U aliada_user aliada_db > backup.sql
```

## 5. SSL (HTTPS)
Recomendamos o uso de um Proxy Reverso como **Nginx + Certbot** à frente do container Docker para gerenciar o certificado SSL gratuitamente.
