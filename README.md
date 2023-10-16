# Descrição

Um projeto em Django para construir uma estrutura ágil Kanban capaz de criar, autalizar, deletar e mostrar tarefas; transpassar a tarefa entre diferentes status e mostrar um Dashboard com dados sobre as tarefas.

# Requerimentos:

* Django 4.2.6
* Python 3
* Javascript
* Postgresql 15

# Para executar o projeto

* Crie uma pasta para o projeto
* Na pasta, execute o comando git clone https://github.com/Alex-dev-if/kanban_django.git
* Crie o ambiente virtual na primeira pasta que criou para o projeto com o comando: python -m venv nome_da_venv
* Ative seu ambiente virtual com o comando: nome_da_venv\Scripts\activate.bat
* No cmd, digite o comando pip install psycopg2
* Digite o comando: pip install django
* Crie um banco de dados no postgresql para usar na aplicação, você pode usar o código sql que estará disponibilizado na pasta "SQLS".
* No seu editor de código, entre na pasta "kanban_django" que foi criada (no vscode basta entra na pasta, no cmd, e digitar code .)
* Abra o arquivo "settings.py" na pasta kanban3.
* Na seção DATABASES nas linhas de NAME, USER, PASSWORD, HOST e PORT, mude para seus respectivos nome do banco de dados(onde tiver escrito "kanban3"), nome de usuário do postgresql (onde tiver escrito "postgres"), senha do usuário (Onde tiver escrito "1234"), host e porta desejados.
* Agora, no cmd, na pasta "kanban_django" digite o comando "python manage.py migrate"
* O projeto já está pronto para executar, para fazer isso, na pasta do projeto(é a pasta que contenha o arquivo manage.py) digite "python manage.py runserver" e no navegador abra no host que foi definido no arquivo "settings.py". Por padrão está em localhost com a porta 8000 (127.0.0.1:8000)

  # Como ultilizar o aplicativo

* Para criar uma nova tarefa, clique no botão "nova tarefa" e adicione um nome, uma descrição e um status para essa tarefa. Em seguida, aperte em "salvar".
* Você pode mudar o status da tarefa alternando ela entre as colunas: a fazer, em progresso e concluídas.
* Para editar uma tarefa, clique no botão "mostrar tarefa" e em seguida no botão "editar a tarefa"
* Para deletar uma tarefa, clique no botão "mostrar tarefa" e em seguida no botão "apagar"
* Para acessar o dashboard, clique no botão "dashboard"
 
  # Diagrama UML
  
![Diagrama UML](https://github.com/Alex-dev-if/kanban_django/assets/91799263/c3a0880a-7a8b-45e3-91ab-96c4b92150d3)
