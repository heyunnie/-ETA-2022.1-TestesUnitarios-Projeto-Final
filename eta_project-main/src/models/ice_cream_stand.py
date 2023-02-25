from src.models.restaurant import Restaurant

class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    #Refatorado
    #Melhoria aplicada: Retornar a mensagem em uma lista ao invés de printar diretamente
    # Bug encontrado: Lógica do if incorreta
    # Correção aplicada:
    #   if self.flavors: PARA if self.flavors.__len__() != 0:
    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""
        menssage = []
        if self.flavors.__len__() != 0:
            menssage.append("No momento temos os seguintes sabores de sorvete disponíveis:")
            for flavor in self.flavors:
                menssage.append(flavor)
            return menssage
        else:
            return "Estamos sem estoque atualmente!"

    #Refatorado
    #Melhoria aplicada: Retornar a mensagem ao invés de printar diretamente e melhoria em algumas mensagens
    # Bug encontrado: Lógica do if incorreta e parametro incorreto nas mensagens
    # Correção aplicada:
    #   if self.flavors: PARA if self.flavors.__len__() != 0:
    #   {self.flavors} PARA {flavors}
    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        if self.flavors.__len__() != 0:
            if flavor in self.flavors:
                return f"O sabor de {flavor} está disponível!"
            else:
                return f"Não temos no momento o sabor de {flavor}!"
        else:
            return "Estamos sem estoque atualmente!"

    #Refatorado
    #Melhoria aplicada: Retornar a mensagem ao invés de printar diretamente e melhoria em algumas mensagens
    #Melhoria aplicada 2: Adição de uma verificação para saber se o valor informado é valido
    # Bug encontrado: if desnecessario
    # Correção aplicada:
    #   if self.flavors: PARA removido:
    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""
        if flavor != None and flavor != "" and type(flavor) == str:
            if flavor in self.flavors:
                return "Sabor já disponivel!"
            else:
                self.flavors.append(flavor)
                return f"{flavor} adicionado ao estoque!"
        else:
            return "Sabor informado invalido!"