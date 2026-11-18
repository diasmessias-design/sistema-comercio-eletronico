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
    clientes = []
    proximo_id = 1

    @staticmethod
    def inserir(cliente):
        cliente.id = ClienteDAO.proximo_id
        ClienteDAO.clientes.append(cliente)
        ClienteDAO.proximo_id += 1

    @staticmethod
    def listar():
        return ClienteDAO.clientes

    @staticmethod
    def listar_id(id):
        for cliente in ClienteDAO.clientes:
            if cliente.id == id:
                return cliente
        return None

    @staticmethod
    def atualizar(cliente):
        for i, c in enumerate(ClienteDAO.clientes):
            if c.id == cliente.id:
                ClienteDAO.clientes[i] = cliente
                return

    @staticmethod
    def excluir(id):
        cliente = ClienteDAO.listar_id(id)
        if cliente is not None:
            ClienteDAO.clientes.remove(cliente)

class CategoriaDAO:
    categorias = []
    proximo_id = 1

    @staticmethod
    def inserir(categoria):
        categoria.id = CategoriaDAO.proximo_id
        CategoriaDAO.categorias.append(categoria)
        CategoriaDAO.proximo_id += 1

    @staticmethod
    def listar():
        return CategoriaDAO.categorias

    @staticmethod
    def listar_id(id):
        for categoria in CategoriaDAO.categorias:
            if categoria.id == id:
                return categoria
        return None

    @staticmethod
    def atualizar(categoria):
        for i, c in enumerate(CategoriaDAO.categorias):
            if c.id == categoria.id:
                CategoriaDAO.categorias[i] = categoria
                return

    @staticmethod
    def excluir(id):
        Categoria = CategoriaDAO.listar_id(id)
        if Categoria is not None:
            CategoriaDAO.categorias.remove(Categoria)


class ProdutoDAO:
    produtos = []
    proximo_id = 1

    @staticmethod
    def inserir(produto):
        produto.id = ProdutoDAO.proximo_id
        ProdutoDAO.produtos.append(produto)
        ProdutoDAO.proximo_id += 1

    @staticmethod
    def listar():
        return ProdutoDAO.produtos

    @staticmethod
    def listar_id(id):
        for produto in ProdutoDAO.produtos:
            if produto.id == id:
                return produto
        return None

    @staticmethod
    def atualizar(produto):
        for i, p in enumerate(ProdutoDAO.produtos):
            if p.id == produto.id:
                ProdutoDAO.produtos[i] = produto
                return

    @staticmethod
    def excluir(id):
        produto = ProdutoDAO.listar_id(id)
        if produto is not None:
            ProdutoDAO.produtos.remove(produto)




