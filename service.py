from model import Cliente, Categoria, Produto
from model import ClienteDAO, CategoriaDAO, ProdutoDAO

class Service:

    @staticmethod
    def cliente_inserir(nome, email, fone):
        cliente = Cliente(0, nome, email,  fone)
        ClienteDAO.inserir(cliente)

    @staticmethod
    def cliente_listar():
        return ClienteDAO.listar()

    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        cliente = ClienteDAO.listar_id(id)

        if cliente is not None:
            cliente_atualizado = Cliente(id, nome, email, fone)
            ClienteDAO.atualizar(cliente_atualizado)

    @staticmethod
    def cliente_excluir(id):
        ClienteDAO.excluir(id)

    @staticmethod
    def categoria_inserir(descricao):
        categoria = Categoria(0, descricao)
        CategoriaDAO.inserir(categoria)

    @staticmethod
    def categoria_listar():
        return CategoriaDAO.listar()

    @staticmethod
    def categoria_listar_id(id):
        return CategoriaDAO.listar_id(id)

    @staticmethod
    def categoria_atualizar(id, descricao):
        categoria = CategoriaDAO.listar_id(id)

        if categoria is not None:
            categoria_atualizada = Categoria(id, descricao)
            CategoriaDAO.atualizar(categoria_atualizada)

    @staticmethod
    def categoria_excluir(id):
        CategoriaDAO.excluir(id)

    @staticmethod
    def produto_inserir(descricao, preco, estoque, idCategoria):
        produto = Produto(0, descricao, preco, estoque, idCategoria)
        ProdutoDAO.inserir(produto)

    @staticmethod
    def produto_listar():
        return ProdutoDAO.listar()

    @staticmethod
    def produto_listar_id(id):
        return ProdutoDAO.listar_id(id)

    @staticmethod
    def produto_atualizar(id, descricao, preco, estoque, idCategoria):
        produto = ProdutoDAO.listar_id(id)

        if produto is not None:
            produto_atualizado = Produto(id, descricao, preco, estoque, idCategoria)
            ProdutoDAO.atualizar(produto_atualizado)

    @staticmethod
    def produto_excluir(id):
        ProdutoDAO.excluir(id)

    @staticmethod
    def produto_reajustar(percentual):
        if percentual < -100:
            return

        produtos = ProdutoDAO.listar()

        for produto in produtos:
            produto.preco = round(produto.preco * (1 + percentual / 100), 2)
            ProdutoDAO.atualizar(produto)
