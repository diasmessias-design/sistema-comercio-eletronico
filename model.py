import json

class Cliente:
    def __init__(self, id, nome, email, fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone


class Categoria:
    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao

class Produto:
    def __init__(self, id, descricao, preco, estoque, idCategoria):
        self.id = id
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.idCategoria = idCategoria


class ClienteDAO:
    arquivo = "clientes.json"

    @staticmethod
    def listar():
        try:
            with open(ClienteDAO.arquivo, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            return [
                Cliente(c["id"], c["nome"], c["email"], c["fone"])
                for c in dados
            ]

        except FileNotFoundError:
            return []

    @staticmethod
    def salvar(clientes):
        dados = []

        for cliente in clientes:
            dados.append({
                "id": cliente.id,
                "nome": cliente.nome,
                "email": cliente.email,
                "fone": cliente.fone
            })

        with open(ClienteDAO.arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    @staticmethod
    def inserir(cliente):
        clientes = ClienteDAO.listar()

        cliente.id = max(
            (c.id for c in clientes), default=0
        ) + 1

        clientes.append(cliente)
        ClienteDAO.salvar(clientes)

    @staticmethod
    def listar_id(id):
        for cliente in ClienteDAO.listar():
            if cliente.id == id:
                return cliente

        return None

    @staticmethod
    def atualizar(cliente):
        clientes = ClienteDAO.listar()

        for i, c in enumerate(clientes):
            if c.id == cliente.id:
                clientes[i] = cliente
                ClienteDAO.salvar(clientes)
                return

    @staticmethod
    def excluir(id):
        clientes = ClienteDAO.listar()

        for cliente in clientes:
            if cliente.id == id:
                clientes.remove(cliente)
                ClienteDAO.salvar(clientes)
                return


class CategoriaDAO:
    arquivo = "categorias.json"

    @staticmethod
    def listar():
        try:
            with open(CategoriaDAO.arquivo, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            return [
                Categoria(c["id"], c["descricao"])
                for c in dados
            ]

        except FileNotFoundError:
            return []

    @staticmethod
    def salvar(categorias):
        dados = []

        for categoria in categorias:
            dados.append({
                "id": categoria.id,
                "descricao": categoria.descricao
            })

        with open(CategoriaDAO.arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    @staticmethod
    def inserir(categoria):
        categorias = CategoriaDAO.listar()

        categoria.id = max(
            (c.id for c in categorias), default=0
        ) + 1

        categorias.append(categoria)
        CategoriaDAO.salvar(categorias)

    @staticmethod
    def listar_id(id):
        for categoria in CategoriaDAO.listar():
            if categoria.id == id:
                return categoria

        return None

    @staticmethod
    def atualizar(categoria):
        categorias = CategoriaDAO.listar()

        for i, c in enumerate(categorias):
            if c.id == categoria.id:
                categorias[i] = categoria
                CategoriaDAO.salvar(categorias)
                return

    @staticmethod
    def excluir(id):
        categorias = CategoriaDAO.listar()

        for categoria in categorias:
            if categoria.id == id:
                categorias.remove(categoria)
                CategoriaDAO.salvar(categorias)
                return




class ProdutoDAO:
    arquivo = "produtos.json"

    @staticmethod
    def listar():
        try:
            with open(ProdutoDAO.arquivo, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            return [
                Produto(
                    p["id"],
                    p["descricao"],
                    p["preco"],
                    p["estoque"],
                    p["idCategoria"]
                )
                for p in dados
            ]

        except FileNotFoundError:
            return []

    @staticmethod
    def salvar(produtos):
        dados = []

        for produto in produtos:
            dados.append({
                "id": produto.id,
                "descricao": produto.descricao,
                "preco": produto.preco,
                "estoque": produto.estoque,
                "idCategoria": produto.idCategoria
            })

        with open(ProdutoDAO.arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    @staticmethod
    def inserir(produto):
        produtos = ProdutoDAO.listar()

        produto.id = max(
            (p.id for p in produtos), default=0
        ) + 1

        produtos.append(produto)
        ProdutoDAO.salvar(produtos)

    @staticmethod
    def listar_id(id):
        for produto in ProdutoDAO.listar():
            if produto.id == id:
                return produto

        return None

    @staticmethod
    def atualizar(produto):
        produtos = ProdutoDAO.listar()

        for i, p in enumerate(produtos):
            if p.id == produto.id:
                produtos[i] = produto
                ProdutoDAO.salvar(produtos)
                return

    @staticmethod
    def excluir(id):
        produtos = ProdutoDAO.listar()

        for produto in produtos:
            if produto.id == id:
                produtos.remove(produto)
                ProdutoDAO.salvar(produtos)
                return
