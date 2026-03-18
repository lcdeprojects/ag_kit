# Ambiente de Desenvolvimento (Setup)

Este guia descreve como configurar o ambiente de desenvolvimento local para o projeto **Aliada**.

## Pré-requisitos

- [Docker](https://www.docker.com/products/docker-desktop/) instalado e rodando.
- [Docker Compose](https://docs.docker.com/compose/install/) (geralmente incluído no Docker Desktop).
- [Python 3.12+](https://www.python.org/downloads/) (opcional, se quiser rodar fora do Docker).

## 🚀 Início Rápido (Docker)

A maneira mais fácil de rodar o projeto é via Docker Compose, que já configura o banco de dados (PostgreSQL) e o servidor web.

1. **Clonar o repositório:**
   ```bash
   git clone <repo-url>
   cd ag_kit
   ```

2. **Configurar Variáveis de Ambiente:**
   Copie o arquivo de exemplo e ajuste se necessário:
   ```bash
   cp .env.example .env
   ```

3. **Subir os containers:**
   ```bash
   docker-compose up --build
   ```

4. **Acessar a aplicação:**
   O sistema estará disponível em [http://localhost:8000](http://localhost:8000).

---

## 🐍 Configuração Manual (Sem Docker)

Se preferir rodar nativamente (útil para debugging rápido):

1. **Criar e ativar o ambiente virtual:**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   source venv/bin/activate # Linux/Mac
   ```

2. **Instalar dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Executar Migrações:**
   ```bash
   python manage.py migrate
   ```

4. **Criar Superusuário:**
   ```bash
   python manage.py createsuperuser
   ```

5. **Rodar o servidor:**
   ```bash
   python manage.py runserver
   ```

## 🛠️ Comandos Úteis

- **Resetar Banco de Dados:** `docker-compose down -v`
- **Ver Logs:** `docker-compose logs -f web`
- **Entrar no Shell do Django:** `docker-compose exec web python manage.py shell`
