from src.models.ice_cream_stand import IceCreamStand

class TestIceCreamStand:

    def test_flavors_available(self):
        #Setup
        restaurant_name = "Sorveteria Lixo"
        restaurant_cuisine_type = "Sorveteria"
        flavors_list = ['Chocolate', 'Morango', 'Baunilha', 'Laranja', 'Limão']
        restaurant = IceCreamStand(restaurant_name, restaurant_cuisine_type, flavors_list)
        exptected_message = "No momento temos os seguintes sabores de sorvete disponíveis:"

        #Act
        result = restaurant.flavors_available()

        #Asserts
        assert exptected_message == result[0], "Mensagem experada não condiz com mensagem retornada"
        for index in range(1, result.__len__()):
            assert flavors_list.__contains__(result[index]), "O sabor não foi encontrado na lista"

    def test_flavors_not_available(self):
        #Setup
        restaurant_name = "Sorveteria Lixo"
        restaurant_cuisine_type = "Sorveteria"
        flavors_list = []
        restaurant = IceCreamStand(restaurant_name, restaurant_cuisine_type, flavors_list)
        exptected_message = "Estamos sem estoque atualmente!"

        #Act
        result = restaurant.flavors_available()

        #Asserts
        assert exptected_message == result, "Mensagem de erro experada para quando estiver sem estoque não condiz com mensagem de erro retornada"
        assert restaurant.flavors == flavors_list, "A flavors_list não está vazia"

    def test_find_flavor(self):
        # Setup
        restaurant_name = "Sorveteria Lixo"
        restaurant_cuisine_type = "Sorveteria"
        flavors_list = ['Chocolate', 'Morango', 'Baunilha', 'Laranja', 'Limão']
        restaurant = IceCreamStand(restaurant_name, restaurant_cuisine_type, flavors_list)
        expected_flavor = flavors_list[4]
        exptected_message = f"O sabor de {expected_flavor} está disponível!"

        # Act
        result = restaurant.find_flavor(expected_flavor)

        # Asserts
        assert result == exptected_message, "Mensagem experada para quando houver sabor disponivel não condiz com mensagem retornada"

    def test_not_find_flavor(self):
        # Setup
        restaurant_name = "Sorveteria Lixo"
        restaurant_cuisine_type = "Sorveteria"
        flavors_list = ['Chocolate', 'Morango', 'Baunilha', 'Laranja', 'Limão']
        restaurant = IceCreamStand(restaurant_name, restaurant_cuisine_type, flavors_list)
        find_flavor = "Tamarindo"
        exptected_message = f"Não temos no momento o sabor de {find_flavor}!"

        # Act
        result = restaurant.find_flavor(find_flavor)

        # Asserts
        assert result == exptected_message, "Mensagem de erro experada para quando não houver sabor no estoque não condiz com mensagem de erro retornada"

    def test_find_flavor_no_stock(self):
            # Setup
            restaurant_name = "Sorveteria Lixo"
            restaurant_cuisine_type = "Sorveteria"
            flavors_list = []
            restaurant = IceCreamStand(restaurant_name, restaurant_cuisine_type, flavors_list)
            find_flavor = "Tamarindo"
            exptected_message = "Estamos sem estoque atualmente!"

            # Act
            result = restaurant.find_flavor(find_flavor)

            # Asserts
            assert result == exptected_message, "Mensagem de erro experado para quando não houver estoque não condiz com mensagem de erro retornada"

    def test_add_flavor(self):
        # Setup
        restaurant_name = "Sorveteria Lixo"
        restaurant_cuisine_type = "Sorveteria"
        flavors_list = ['Chocolate']
        restaurant = IceCreamStand(restaurant_name, restaurant_cuisine_type, flavors_list)
        new_flavor = "Tamarindo"
        exptected_message = f"{new_flavor} adicionado ao estoque!"

        # Act
        result = restaurant.add_flavor(new_flavor)

        # Asserts
        assert result == exptected_message, "Mensagem de erro experado para quando o sabor é adicionado no estoque não condiz com a mensagem retornada"
        assert restaurant.flavors.__contains__(new_flavor), "O sabor adicionado não está contido na lista de sabores"

    def test_add_already_flavor(self):
        # Setup
        restaurant_name = "Sorveteria Lixo"
        restaurant_cuisine_type = "Sorveteria"
        flavors_list = ['Chocolate']
        restaurant = IceCreamStand(restaurant_name, restaurant_cuisine_type, flavors_list)
        new_flavor = "Chocolate"
        expected_flavors_list_len = len(flavors_list)
        exptected_message = "Sabor já disponivel!"

        # Act
        result = restaurant.add_flavor(new_flavor)

        # Asserts
        assert result == exptected_message, "Mensagem de erro experado para quando o sabor já está disponível não condiz com mensagem de erro retornada"
        assert len(restaurant.flavors) == expected_flavors_list_len, "O sabor foi adicionado a lista"

    def test_add_None_flavor(self):
        # Setup
        restaurant_name = "Sorveteria Lixo"
        restaurant_cuisine_type = "Sorveteria"
        flavors_list = ['Chocolate']
        restaurant = IceCreamStand(restaurant_name, restaurant_cuisine_type, flavors_list)
        new_flavor = None
        expected_flavors_list_len = len(flavors_list)
        exptected_message = "Sabor informado invalido!"

        # Act
        result = restaurant.add_flavor(new_flavor)

        # Asserts
        assert result == exptected_message, "Mensagem de erro experado para quando o sabor informado for 'None' não condiz com mensagem de erro retornada"
        assert len(restaurant.flavors) == expected_flavors_list_len, "O sabor 'None' foi adicionado a lista"

    def test_add_empty_flavor(self):
        # Setup
        restaurant_name = "Sorveteria Lixo"
        restaurant_cuisine_type = "Sorveteria"
        flavors_list = ['Chocolate']
        restaurant = IceCreamStand(restaurant_name, restaurant_cuisine_type, flavors_list)
        new_flavor = ""
        expected_flavors_list_len = len(flavors_list)
        exptected_message = "Sabor informado invalido!"

        # Act
        result = restaurant.add_flavor(new_flavor)

        # Asserts
        assert result == exptected_message, "Mensagem de erro experado para quando o sabor informado for uma string vazia não condiz com mensagem de erro retornada"
        assert len(restaurant.flavors) == expected_flavors_list_len, "A string vazia foi adicionada a lista"

    def test_add_flavor_invalid_type(self):
        # Setup
        restaurant_name = "Sorveteria Lixo"
        restaurant_cuisine_type = "Sorveteria"
        flavors_list = ['Chocolate']
        restaurant = IceCreamStand(restaurant_name, restaurant_cuisine_type, flavors_list)
        new_flavor = 13246
        expected_flavors_list_len = len(flavors_list)
        exptected_message = "Sabor informado invalido!"

        # Act
        result = restaurant.add_flavor(new_flavor)

        # Asserts
        assert result == exptected_message, "Mensagem de erro experado para quando o sabor informado for um numero não condiz com mensagem de erro retornada"
        assert len(restaurant.flavors) == expected_flavors_list_len, "O numero foi adicionado a lista"