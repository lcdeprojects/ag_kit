# Guia de Deploy (Produção)

O projeto **Aliada** está configurado para deploy automatizado, com foco na plataforma **Railway**.

## 🚂 Deploy na Railway

A aplicação utiliza o `Dockerfile` e `docker-compose.yml` para definir o ambiente.

### Passos para Deploy

1. **Conectar Replositório:** Na Railway, crie um novo projeto e conecte com o repositório GitHub.
2. **Variáveis de Ambiente:** Certifique-se de configurar as seguintes variáveis no painel da Railway:
   - `DEBUG`: `0` (Produção)
   - `SECRET_KEY`: Uma chave longa e aleatória.
   - `ALLOWED_HOSTS`: O domínio da sua aplicação (ex: `aliada-gestao.up.railway.app`).
   - `CSRF_TRUSTED_ORIGINS`: URLs permitidas para CSRF (ex: `https://aliada-gestao.up.railway.app`).
   - `DATABASE_URL`: Gerada automaticamente ao adicionar um serviço PostgreSQL na Railway.

### Automação de Startup

O container está configurado (`CMD` no Dockerfile) para:
1. Rodar migrações automaticamente (`migrate`).
2. Criar/garantir um usuário admin via `scripts/create_admin.py`.
3. Iniciar o servidor de produção **Gunicorn**.

---

## 🐳 Docker em Produção

Para rodar em um servidor VPS próprio:

1. Use o arquivo `docker-compose.prod.yml` (se disponível) ou ajuste o padrão para usar Nginx como Proxy Reverso.
2. Certifique-se de coletar arquivos estáticos:
   ```bash
   docker-compose exec web python manage.py collectstatic --no-input
   ```

## 🔒 Segurança

- **SSL/HTTPS:** Obrigatório. Na Railway, isso é gerenciado automaticamente.
- **Portas:** Apenas a porta 80/443 (via Proxy) e a 8000 interna devem estar envolvidas.
- **Arquivos Secretos:** Nunca suba o arquivo `.env` para o Git.
