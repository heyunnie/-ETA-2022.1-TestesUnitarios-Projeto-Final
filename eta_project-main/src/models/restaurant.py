class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    # Refatorado
    # Bug encontrado: Frase incorreta, tendo o nome e o tipo "trocados"
    # Melhoria aplicada: trocar o método para retornar uma lista contendo as linhas da mensagem ao invés de printar individualmente
    def describe_restaurant(self):
        """Retorne em uma lista uma descrição simples da instância do restaurante."""
        mensagem = []
        mensagem.append(f"Esse restaurante se chama {self.restaurant_name} and serve {self.cuisine_type}.")
        mensagem.append(f"Esse restaturante está servindo {self.number_served} consumidores desde que está aberto.")
        return mensagem

    #Refatorado
    #Bug encontrado: Conteudo do if se encontra incorreto. Ele não sinaliza a abertura do restaurante na variavel self.open e decrementa o número de servidos
    # Melhoria aplicada: retornar a mensagem ao inves de printar
    # Correção:
    #   De self.open = False PARA self.open = True
    #   De self.number_served = -2 PARA delete line
    def open_restaurant(self):
        """Retorne uma mensagem indicando que o restaurante está aberto para negócios."""
        if not self.open:
            self.open = True
            return f"{self.restaurant_name} agora está aberto!"
        else:
            return f"{self.restaurant_name} já está aberto!"

    # Refatorado
    # Melhoria aplicada: retornar a mensagem ao inves de printar
    def close_restaurant(self):
        """Retorne uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open:
            self.open = False
            self.number_served = 0
            return f"{self.restaurant_name} agora está fechado!"
        else:
            return f"{self.restaurant_name} já está fechado!"

    # Refatorado
    # Melhoria aplicada: retornar a mensagem ao inves de printar e adição de uma verificação se o valor informado é valido
    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        if self.open:
            if type(total_customers) == int:
                self.number_served = total_customers
                return "Número de pessoas atendidas atualizado com sucesso!"
            else:
                return "Valor informado invalido!"
        else:
            return f"{self.restaurant_name} está fechado!"

    # Refatorado
    # Melhoria aplicada: retornar a mensagem ao inves de printar, adição de uma verificação se o valor informado é valido e adição de mensagem para o cenário de sucesso
    # Bug encontrado: o more_customers sobrepõe o valor de number_served
    # Correção:
    #      De self.number_served = more_customers para self.number_served += more_customers
    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        if self.open:
            if type(more_customers) == int:
                self.number_served += more_customers
                return "Total de clientes atendidos atualizado com sucesso!"
            else:
                return "Valor informado invalido!"
        else:
            return f"{self.restaurant_name} está fechado!"