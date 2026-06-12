produtos = [
    {"nome": "leite", "quantidade": 12, "preco": 5.50},
    {"nome": "cafe", "quantidade": 10, "preco": 30.00},
    {"nome": "feijao", "quantidade": 8, "preco": 4.85}
]

while True:
    print("### SISTEMA DE ESTOQUE ###")
    print("1 - Visualizar Estoque Atual")
    print("2 - Registrar Entrada de Produto")
    print("3 - Registrar Saída de Produto")
    print("4 - Sair do Sistema")

    opcao = int(input("Digite uma opcao: "))

    if opcao == 1:
        print("Estoque atual")

        for produto in produtos:
            print(produto["nome"], produto["quantidade"], produto["preco"])

    elif opcao == 2:
        print("Entrada de produto")

        nome_do_produto = input("Escreva o nome do produto: ")
        quantidade = int(input("Digite a quantidade a adicionar: "))

        encontrado = False

        for produto in produtos:
            if produto["nome"] == nome_do_produto:
                produto["quantidade"] += quantidade
                print("foi adicionado o produto com sucesso")
                encontrado = True
                break

        if encontrado == False:
            print("Produto não encontrado.")

    elif opcao == 3:
        print("Saida do produto")

        nome_do_produto = input("Escreva o nome do produto: ")
        quantidade = int(input("Digite a quantidade a sair: "))

        encontrado = False

        for produto in produtos:
            if produto["nome"] == nome_do_produto:
                encontrado = True

                if produto["quantidade"] >= quantidade:
                    produto["quantidade"] -= quantidade
                    print("foi retirado o produto com sucesso!!!")
                else:
                    print("Estoque insuficiente")

                break

        if encontrado == False:
            print("Produto nao encontrado.")

    elif opcao == 4:
        print("Saindo do sistema!!!")
        break

    else:
        print("opcao invalida, use outra opcao de 1 a 4")