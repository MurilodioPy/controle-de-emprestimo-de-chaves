# Projeto Flask - Controle de empréstimo de chaves

## Passo a passo para executar o aplicação 
## Dentro do LINUX ou WSL
```
git clone --branch dockertest https://github.com/MurilodioPy/controle-de-emprestimo-de-chaves.git
```
## Entrar na pasta do projeto
```
cd controle-de-emprestimo-de-chaves/
```
## Dentro da pasta do projeto
## Instale o docker
```
sudo apt update 
```
```
sudo pip install docker
```
```
sudo apt install docker-ce docker-ce-cli containerd.io 
```
## Inicie o docker
```
sudo service docker start
```
## Inicie a aplicação
```
sudo docker compose up --build 
```
## Abra o browser 
```
localhost:8080
```

## Estrutura do Projeto
- `app/`: Pasta principal do aplicativo
  - `__init__.py`: Configuração do aplicativo Flask
  - `database.py`: Configuração do banco de dados SQLAlchemy
  - `views/`: Pacote para as visões (rotas) do aplicativo
    - `chave.py`: Visões relacionadas às chaves
    - `servidor.py`: Visões relacionadas aos servidores
    - `emprestimo.py`: Visões relacionadas aos empréstimos
    - `aplicativo.py`: Visões gerais do aplicativo

## Configuração do Flask

- `create_app()`: Função para criar uma instância do aplicativo Flask
- Configurações do banco de dados
  - `SQLALCHEMY_DATABASE_URI`: URI do banco de dados MySQL
  - `SQLALCHEMY_TRACK_MODIFICATIONS`: Configuração para rastrear modificações
  - `SQLALCHEMY_ECHO`: Ativa a saída de depuração para consultas SQL

## Blueprints

- `chave_bp`: Blueprint para visões relacionadas a chaves
- `servidor_bp`: Blueprint para visões relacionadas a servidores
- `emprestimo_bp`: Blueprint para visões relacionadas a empréstimos
- `aplicativo_bp`: Blueprint para visões gerais do aplicativo

## Rotas e Visões

### Chaves

- Listar chaves
- Inserir nova chave
- Atualizar chave
- Deletar chave

### Servidores

- Listar servidores
- Inserir novo servidor
- Atualizar servidor
- Deletar servidor

### Empréstimos

- Listar empréstimos
- Inserir novo empréstimo
- Atualizar empréstimo
- Deletar empréstimo

## Tratamento de Erros

- Página de erro 404 para rotas não encontradas

## Configuração do MySQL

- URI de conexão com o MySQL


## Jinja2

- Templates com Jinja2

