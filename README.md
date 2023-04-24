# desafio-tins
Desafio para vaga de dev Python Pleno na TINS


```
Considerando o sql em anexo, temos o seguinte levantamento de requisitos para um dos nossos clientes:

    Ele precisa cadastrar os clientes e quantos endereços ele tiver;
    Um, e somente um dos endereços será o endereço padrão;
    O cadastro do endereço deverá consumir a API do viacep (https://viacep.com.br/) para preencher os campos após informar o CEP, de forma que somente o CEP (por exemplo, "77001-572"), o titulo (por exemplo, "Casa da sogra") e o número (por exemplo, "25") serão preenchidos de fato pelo cliente;
    O cadastro de produto deverá ter um código de 6 dígitos;
    Por fim teremos uma tela de pedido, onde pesquisamos o cliente pelo CPF ou pelo nome, e mostramos todas as informações cadastradas dele. Temos um campo com o endereço padrão do usuário já selecionado, mostrando todas as informações desse endereço, mas com a possibilidade de selecionar um outro endereço do cliente. e também um campo de pesquisa de produtos para adicionar ao pedido tanto pelo código, como pela descrição, que ao adicionar, será mostrado numa tabela abaixo. Abaixo da tabela, mostrar o valor do pedido naquele instante. Importante que o código do pedido tenha sempre 11 dígitos;
    No final dessa tela, um botão para "enviar" pedido, que será enviado para o e-mail cadastrado do cliente. As informações de SMTP deverá constar no arquivo de configuração.
    Para todos esses cadastros, é necessário o CRUD completo. sendo que na listagem de produtos e clientes é necessário um filtro sendo para produto por código e descrição e para o cliente por CPF e nome;

Como já está nos requisitos da vaga, essa aplicação de ser feita em django, utilizando qualquer template desde que não seja o padrão.

Será considerado um PLUS se conseguir entregar o sistema rodando em docker.

```

# Configurando projeto
## Configurando as variáveis de ambiente.
- Clone o arquivo ```.env.example``` com o nome de ```.env```
- Preencha todas as variáveis
- - A variável ```SECRET_KEY``` pode ser gerada em [djecrety](https://djecrety.ir/).
- - A variável ```DEBUG``` pode ser inicializada como ```TRUE``` para ver os relatórios de erros, ou ```FALSE``` para ignorar.
- - A variável ```ALLOWED_HOSTS``` é uma lista de hosts autorizados e pode ser inicializada com ``localhost,127.0.0.1,0.0.0.0``.
- - Banco de dados:
- - - Banco Local:
- - - - A variável ```SQLITE_URL``` pode ser deixado como padrão ```sqlite:///local-dev-sqlite.db```.
- - - - A variável ```DATABASE_URL``` pode ser inicializada com ```SQLITE_URL``` caso for usar banco local.
- - - Se for usar PostgreSQL:
- - - - A variável ```MYSQL_HOST``` pode ser inicializada com ```db```, caso esteja conectando a um banco externo, insira o ip de acesso.
- - - - A variável ```MYSQL_ROOT_PASSWORD``` pode ser inicializada com a senha root padrão do banco.
- - - - A variável ```MYSQL_USER``` pode ser inicializada com o usuario do banco.
- - - - A variável ```MYSQL_PASSWORD``` pode ser inicializada com a senha do banco.
- - - - A variável ```MYSQL_DATABASE``` pode ser inicializada com o nome do banco.
- - - - A variável ```PGADMIN_DEFAULT_PASSWORD``` pode ser inicializada com a senha de acesso ao PgAdmin.
- - - - A variável ```MYSQL_PORT``` pode ser inicializada com a porta para acessar o PgAdmin.
- - - - A variável ```DATABASE_URL``` pode ser inicializada com ```mysql://user:password@host:port/dbname``` ou ```mysql://$MYSQL_USER:$MYSQL_PASSWORD@$MYSQL_HOST:$MYSQL_PORT/$MYSQL_DATABASE```.
- - A variável ```APP_PORT``` pode ser inicializada com a porta para acessar a aplicação, o padrão é ```8000```.
- - A variável ```RABBITMQ_HOST``` pode ser inicializada com ```rabbitmq```, caso esteja conectando a um rabbitmq externo, insira o ip de acesso.
- - A variável ```RABBITMQ_USER``` pode ser inicializada com o usuario do rabbitmq.
- - A variável ```RABBITMQ_PASSWORD``` pode ser inicializada com a senha do rabbitmq.
- - A variável ```RABBITMQ_PORT_1``` pode ser inicializada com uma das portas para acessar o RabbitMQ, o padrão é ```5672```.
- - A variável ```RABBITMQ_PORT_2``` pode ser inicializada com uma das portas para acessar o RabbitMQ, o padrão é ```15672```.
- - A variável ```EMAIL_HOST``` pode ser inicializada com o host do provedor de email, exemplo ```smtp.gmail.com```.
- - A variável ```EMAIL_HOST_USER``` pode ser inicializada com o usuário do provedor de email.
- - A variável ```EMAIL_HOST_PASSWORD``` pode ser inicializada com a senha do provedor de email.


### Utilizando o Docker
- Instale o [Docker](https://www.docker.com/).
- Caso queira criar um usuário administrador, execute o seguinte comando ```docker compose run app python manage.py createsuperuser```
- Agora para iniciar a aplicação execute ```docker compose up -d```
- Acesse [localhost:8000](http://0.0.0.0:8000)


### Manualmente
- Instale o [Python](https://www.python.org/) versão ^3.10 ou superiore, em seguida, instale o [Poetry](https://python-poetry.org/).
- Acesse a pasta do projeto e execute o comando ```poetry install```
- Em seguida, acesse o ambiente virtual com ```poetry shell```
- Em seguida, execute o comando ```./manage.py migrate``` para realizar todas as migrações em banco de dados.
- Caso queira criar um usuário administrador, execute o seguinte comando ```./manage.py createsuperuser```
- Agora para iniciar a aplicação execute ```./manage.py runserver```
- Acesse [localhost:8000](http://127.0.0.1:8000)


# ADMIN COM JAZZMIN TEMPLATE
- Crie o usuário administrador
- Acesse [admin-site](0.0.0.0:8000/)

## Tela de Login
![Tela de login](docs/images/login.jpeg)
## Cadastro de Cliente
![Tela de login](docs/images/cadastro_cliente.jpeg)
- O cliente pode pesquisar o cep inserido e ter as informações coletadas da api viacep
- Apenas um endereço pode ser marcado como default
## Cadastro de Produto
![Tela de login](docs/images/cadastro_produto.jpeg)
## Cadastro de Pedido
![Tela de login](docs/images/cadastro_pedido.jpeg)
- O campo ``Cod Cliente`` pode ser pesquisado por cpf ou nome.
## Email enviado apos cadastro de pedido
![Tela de login](docs/images/email_pedido.jpeg)