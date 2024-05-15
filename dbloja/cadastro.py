import pymysql
from chaves import USER, PASS


conexao = pymysql.connect(
    host='localhost',
    user= USER,
    password= PASS,
    database='dbloja'
)

with conexao:
    with conexao.cursor() as cursor:
        TABLE_NAME = 'produto'

        #criação da tabela
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}('
                'id INT AUTO_INCREMENT PRIMARY KEY, '
                'nome VARCHAR(255) NOT NULL,'
                'valor DOUBLE(10, 2) NOT NULL,'
                'preco INT NOT NULL'
            ')'
        )

    conexao.commit()

    with conexao.cursor() as cursor:
        TABLE_NAME = 'cliente'

        #criação da tabela
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}('
                'id INT AUTO_INCREMENT PRIMARY KEY, '
                'nome VARCHAR(255) NOT NULL,'
                'cpf VARCHAR(11) NOT NULL,'
                'telefone VARCHAR(20),'
                'email VARCHAR(50)'
            ')'
        )
    conexao.commit()

    with conexao.cursor() as cursor:

        #LISTANDO TUDO
        TABLE_NAME = input("\nDigite o nome da tabela: ").lower()

        query = f'SELECT * FROM {TABLE_NAME}'
        cursor.execute(query)
        resposta = cursor.fetchall()
        print(resposta)
        
        #INSERINDO DADOS EM PRODUTO
        nome = input("Digite o nome do produto: ").upper()
        valor = float(input("Digite o nome do produto: ")).upper()
        quantidade = int(input("Digite o nome do produto: ")).upper()
        query = f'INSERT INTO {TABLE_NAME} (nome, valor, quantidade) VALUES(%s, %s, %s)'
        cursor.execute(query)
        resposta = cursor.fetchall()
        print(resposta)
    conexao.commit()


    
        