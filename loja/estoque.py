import time
import loja.funcoes as funcoes
# print(produtos)

produtos = [{
      'nome': 'mouse',
      "valor": 200,
      'descricao': 'mouse'
}, {
      'nome': 'teclado',
      "valor": 400,
      'descricao': 'teclado'
},{
      'nome': 'mousepad',
      "valor": 6000,
      'descricao': 'mousepad'
} 
]




nome = input("informe o nome do produto: ")
valor = float(input("informe o valor do produto: "))
descricao = input("informe a descricao do produto: ")
   

produtos.append({
        "nome": nome,
        "valor": valor,
        "descricao": descricao,
        "estoque": 10
    })

funcoes.excluir_produto()

funcoes.listar_produtos(produtos)
            