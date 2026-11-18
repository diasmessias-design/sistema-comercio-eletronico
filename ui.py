from service import Service

class UI:
    @staticmethod
    def menu():
        print("\n==== Comércio Eletrônico ====")
        print("1 - Inserir Cliente")
        print("2 - Listar Clientes")
        print("3 - Atualizar Cliente")
        print("4 - Excluir Cliente")
        print("5 - Inserir Categoria")
        print("6 - Listar Categorias")
        print("7 - Atualizar Categoria")
        print("8 - Excluir Categoria")
        print("9 - Inserir produto")
        print("10 - Listar Produtos")
        print("11 - Atualizar Produto")
        print("12 - Excluir Produto")
        print("13 - Reajustar Preços")
        print("0 - Finalizar")

        return input("Escolha uma opção: ")
## Cliente
    @staticmethod
    def cliente_inserir():
        nome = input("Nome: ")
        email = input("Email: ")
        fone = input("Telefone: ")
        Service.cliente_inserir(nome, email, fone)
        print("Cliente Cadastrado!")

    @staticmethod
    def cliente_listar():
        for c in Service.cliente_listar():
            print(c.id, c.nome, c.email, c.fone)

    @staticmethod
    def cliente_atualizar():
        id = int(input("ID do Cliente: "))
        if Service.cliente_listar_id(id) is None:
            print("Cliente não encontrado!")
            return
        nome = input("Nome: ")
        email = input("Email: ")
        fone = input("Telefone: ")
        Service.cliente_atualizar(id, nome, email, fone)
        print("Cliente atualizado!")

    @staticmethod
    def cliente_excluir():
        id = int(input("ID do cliente: "))
        if Service.cliente_listar_id(id) is None:
            print("Cliente não encontrado")
            return
        Service.cliente_excluir(id)
        print("Cliente Excluído!")
#categoria
    @staticmethod
    def categoria_inserir():
        descricao = input("Descrição: ")
        Service.categoria_inserir(descricao)
        print("Categoria Cadastrada!")

    @staticmethod
    def categoria_listar():
        for c in Service.categoria_listar():
            print(c.id, c.descricao)

    @staticmethod
    def categoria_atualizar():
        id = int(input("ID da categoria: "))
        if Service.categoria_listar_id(id) is None:
            print("Categoria não encontrada!")
            return
        descricao = input("Nova descrição: ")
        Service.categoria_atualizar(id, descricao)
        print("Categoria atualizada!")

    @staticmethod
    def categoria_excluir():
        id = int(input("ID da categoria: "))
        if Service.categoria_listar_id(id) is None:
            print("Categoria não encontrada!")
            return
        Service.categoria_excluir(id)
        print("Categoria excluída!")

    @staticmethod
    def produto_inserir():
        descricao = input("Descrição: ")
        preco = float(input("Preço: "))
        estoque = int(input("Estoque: "))
        idCategoria = int(input("ID da categoria: "))

        if Service.categoria_listar_id(idCategoria) is None:
            print("Categoria não encontrada!")
            return
        Service.produto_inserir(descricao, preco, estoque, idCategoria)
        print("Produto cadastrado!")

    @staticmethod
    def produto_listar():
        for p in Service.produto_listar():
            print(p.id, p.descricao, p.preco, p.estoque, p.idCategoria)

    @staticmethod
    def produto_atualizar():
        id = int(input("ID do produto: "))
        if Service.produto_listar_id(id) is None:
            print("Produto não encontrado!")
            return

        descricao = input("Nova descrição: ")
        preco = float(input("Novo preço: "))
        estoque = int(input("Novo estoque: "))
        idCategoria = int(input("ID da categoria: "))

        if Service.categoria_listar_id(idCategoria) is None:
            print("Categoria não encontrada!")
            return
        Service.produto_atualizar(id, descricao, preco, estoque, idCategoria)
        print("Produto atualizado")

    @staticmethod
    def produto_excluir():
        id = int(input("ID do produto: "))
        if Service.produto_listar_id(id) is None:
            print("Produto não encontrado!")
            return
        Service.produto_excluir(id)
        print("Produto excluído!")

    @staticmethod
    def produto_reajustar():
        percentual = float(input("Percentual de reajustes: "))
        if percentual < -100:
            print("Percentual inválido!")
            return
        Service.produto_reajustar(percentual)
        print("Preços reajustados!")

    @staticmethod
    def main():
        while True:
            opcao = UI.menu()

            if opcao == "0":
                print("Sistema finalizado!")
                break

            operacoes = {
                "1": UI.cliente_inserir,
                "2": UI.cliente_listar,
                "3": UI.cliente_atualizar,
                "4": UI.cliente_excluir,
                "5": UI.categoria_inserir,
                "6": UI.categoria_listar,
                "7": UI.categoria_atualizar,
                "8": UI.categoria_excluir,
                "9": UI.produto_inserir,
                "10": UI.produto_listar,
                "11": UI.produto_atualizar,
                "12": UI.produto_excluir,
                "13": UI.produto_reajustar
            }

            if opcao in operacoes:
                try:
                    operacoes[opcao]()
                except ValueError:
                    print("Valor inválido! Tente novamente.")
            else:
                print("Opção inválida!")









