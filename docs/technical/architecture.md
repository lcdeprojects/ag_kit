# Arquitetura do Sistema

A **Aliada** é um sistema de gestão de clínicas construído sobre uma base moderna e extensível.

## 🏗️ Visão Geral

A arquitetura é dividida em três camadas principais:

1. **Frontend (Django Templates + Tailwind CSS):** Interface de usuário focada em performance e usabilidade, utilizando renderização no servidor para SEO e velocidade.
2. **Backend (Django Framework):** Lógica de negócios robusta, ORM para gerenciamento de dados e autenticação segura.
3. **Inteligência (Antigravity Kit):** Um ecossistema de agentes AI que auxiliam no desenvolvimento, manutenção e automação do sistema.

## 🧩 Componentes do Ag Kit (Antigravity)

O diretório `.agent/` contém a inteligência do sistema:

- **Agentes Especialistas:** 20 tipos de agentes (ex: `backend-specialist`, `documentation-writer`) que seguem regras estritas para garantir qualidade de código.
- **Skills:** Módulos de conhecimento (ex: `clean-code`, `database-design`) carregados sob demanda.
- **Workflows:** Comandos customizados (Slash Commands) para automatizar tarefas comuns como `/debug`, `/plan` e `/brainstorm`.

## 📁 Estrutura de Diretórios

```plaintext
/
├── aliada_root/      # Configurações globais do Django (settings, wsgi, urls)
├── clinic/           # Aplicação principal (Modelos, Views, Templates da clínica)
│   ├── models/       # Definições de dados (Pacientes, Agendamentos, etc)
│   ├── views/        # Lógica de interface dividida por domínio
│   └── templates/    # Arquivos HTML/Tailwind
├── .agent/           # Núcleo do Antigravity Kit (AI & Automação)
├── docs/             # Esta documentação
├── scripts/          # Scripts utilitários (Reset DB, Create Admin)
└── static/           # Arquivos estáticos (CSS, JS, Imagens)
```

## 🔄 Fluxo de Dados

O sistema segue o padrão **MVT (Model-View-Template)** do Django:
1. O usuário faz uma requisição para uma URL.
2. A **View** processa a lógica de negócio, consultando o **Model**.
3. O **Model** interage com o Banco de Dados PostgreSQL.
4. A **View** renderiza o **Template** com os dados e retorna ao usuário.
