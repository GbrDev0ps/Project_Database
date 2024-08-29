# Project_Database
Projeto para consulta de dados.

Passo a passo para rodar a solução localmente:
Pré Requisitos -
Antes de começar, certifique-se de ter instalado as seguintes ferramentas:

Python 3.7+
Biblioteca SQLite3 (já incluída com Python)
Biblioteca Tkinter (já incluída com Python)
Biblioteca CSV (já incluída com Python)
Biblioteca Datetime (já incluída com Python)

2 - Você deve possuir a pasta do projeto com: 
Os scripts, sendo eles "create_db.py", "insert_data.py" e "sql_models.py".
E o arquivo CSV "database-companies.csv" a ser lido em uma pasta chamada "database"

3 - O conteudo dos arquivos é;
A - create_db.py
Cria o banco de dados SQLite e a tabela necessária

B - insert_data.py
Insere os dados do arquivo CSV no banco de dados

C - sql_models.py
Fornece uma interface gráfica com possibilidades de consultas entre datas dos dados.

4 - Como rodar os scripts:
A - No terminal, execute o script 'create_db.py' para criar o banco de dados e a tabela.
B - Após isso, execute o sctipt 'insert_data.py' para inserir os dados do arquivo CSV no banco de dados
C - Você irá iniciar a interface gráfica e fazer as consultas, sendo as maneiras de consultar:
    TODAS AS DATAS DEVEM IR COM O MODO DE : DD/MM/AA
    Colocando apenas a data inicial você irá trazer todas as informações A PARTIR daquela data
    Colocando duas datas (inicial e final diferentes) você irá trazer as informações contidas ENTRE aquelas data
    colocando duas datas iguai trará apenas informações daquela data especifica.
    A visualização da interface gráfica pode ser feita em tela cheia e pode conter mais informações ao longo da página, sendo assim, possivel rolar para baixo.

Durante o projeto as decisões foram:

Como foi pedido um banco de dados SQL, decidi usar um SQLite por já ter estudado sobre e ter conhecimentos de que é mais leve e facil para projetos pequenos/prototipos
Dividi o projeto em três scripts para facilitar uma possivel manutenção do código e a execução SEQUENCIAL das etapas, sendo elas citadas acima.
Como uma consulta deve ser visual, decidi utilizar a biblioteca TKinter para a visualização dos dados com uma interface gráfica.
