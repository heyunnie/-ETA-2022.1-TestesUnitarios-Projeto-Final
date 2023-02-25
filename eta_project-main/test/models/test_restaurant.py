from src.models.restaurant import Restaurant

class TestRestaurant:

    def test_describe_restaurant(self):
        #Setup
        restaurant_name = "Restaurante Lixo"
        cuisine_type = "Lixo"
        number_served = "0"
        restaurant = Restaurant(restaurant_name, cuisine_type)
        expected_message1 = f"Esse restaurante se chama {restaurant_name} and serve {cuisine_type}."
        expected_message2 = f"Esse restaturante está servindo {number_served} consumidores desde que está aberto."

        #Act
        result = restaurant.describe_restaurant()

        #Assert
        assert result[0] == expected_message1, "Mensagem experada não condiz com a mensagem retornada"
        assert result[1] == expected_message2, "Mensagem experada não condiz com a mensagem retornada"


    def test_open_restaurant(self):
        # Setup
        restaurant_name = "Restaurante Lixo"
        cuisine_type = "Lixo"
        restaurant = Restaurant(restaurant_name, cuisine_type)
        expected_message = f"{restaurant_name} agora está aberto!"

        # Act
        result = restaurant.open_restaurant()

        # Assert
        assert result == expected_message, "Mensagem de sucesso experada não condiz com a mensagem retornada"
        assert restaurant.open == True, "Valor da variavel open não foi modificada com sucesso"

    def test_already_open_restaurant(self):
        # Setup
        restaurant_name = "Restaurante Lixo"
        cuisine_type = "Lixo"
        restaurant = Restaurant(restaurant_name, cuisine_type)
        expected_message = f"{restaurant_name} já está aberto!"
        restaurant.open_restaurant()

        # Act
        result = restaurant.open_restaurant()

        # Assert
        assert result == expected_message, "Mensagem de erro experada não condiz com mensagem de erro retornada"
        assert restaurant.open == True, "Valor da variavel restaurant.ope foi modificada para False"

    def test_close_restaurant(self):
        # Setup
        restaurant_name = "Restaurante Lixo"
        cuisine_type = "Lixo"
        restaurant = Restaurant(restaurant_name, cuisine_type)
        expected_message = f"{restaurant_name} agora está fechado!"
        restaurant.open_restaurant()

        # Act
        result = restaurant.close_restaurant()

        # Assert
        assert result == expected_message, "Mensagem experada não condiz com a mensagem retornada"
        assert restaurant.open == False, "O valor da variavel open não foi modificada para False"
        assert restaurant.number_served == 0, "O valor da variavel number_Served não foi modificada para 0"

    def test_already_close_restaurant(self):
        # Setup
        restaurant_name = "Restaurante Lixo"
        cuisine_type = "Lixo"
        restaurant = Restaurant(restaurant_name, cuisine_type)
        expected_message = f"{restaurant_name} já está fechado!"

        # Act
        result = restaurant.close_restaurant()

        # Assert
        assert result == expected_message, "Mensagem de erro esperado não condiz com mensagem de erro retornada"
        assert restaurant.open == False, "O valor da variavel open não se manteve como False"
        assert restaurant.number_served == 0, "O valor da variavel number_Served não se manteve como 0"

    def test_set_number_served(self):
        # Setup
        restaurant_name = "Restaurante Lixo"
        cuisine_type = "Lixo"
        restaurant = Restaurant(restaurant_name, cuisine_type)
        restaurant.open_restaurant()
        new_total_number_served = 50
        expected_message = "Número de pessoas atendidas atualizado com sucesso!"

        # Act
        result = restaurant.set_number_served(new_total_number_served)

        # Assert
        assert expected_message == result, "Mensagem experada não condiz com mensagem retornada"
        assert restaurant.number_served == new_total_number_served, "O valor informado não foi inserido na variavel number_served"

    def test_set_number_served_with_invalid_number(self):
        # Setup
        restaurant_name = "Restaurante Lixo"
        cuisine_type = "Lixo"
        restaurant = Restaurant(restaurant_name, cuisine_type)
        restaurant.open_restaurant()
        new_total_number_served = None
        expected_total_number_Served = 0
        expected_message = "Valor informado invalido!"

        # Act
        result = restaurant.set_number_served(new_total_number_served)

        # Assert
        assert expected_message == result, "Mensagem de erro experada não condiz com mensagem de erro retornada"
        assert expected_total_number_Served == restaurant.number_served, "O valor da variavel number_served foi modificado"

    def test_set_number_served_with_restaurant_close(self):
        # Setup
        restaurant_name = "Restaurante Lixo"
        cuisine_type = "Lixo"
        restaurant = Restaurant(restaurant_name, cuisine_type)
        new_total_number_served = 50
        expected_result = f"{restaurant_name} está fechado!"
        expected_number_served = 0

        # Act
        result = restaurant.set_number_served(new_total_number_served)

        # Assert
        assert result == expected_result, "Mensagem de erro experada não condiz com mensagem de erro retornada"
        assert restaurant.number_served == expected_number_served, "O valor da variavel number_served foi modificado"

    def test_increment_number_served(self):
        # Setup
        restaurant_name = "Restaurante Lixo"
        cuisine_type = "Lixo"
        restaurant = Restaurant(restaurant_name, cuisine_type)
        restaurant.open_restaurant()
        new_increment_number_served = 5
        expected_message = "Total de clientes atendidos atualizado com sucesso!"

        # Act
        result = restaurant.increment_number_served(new_increment_number_served)

        # Assert
        assert expected_message == result, "Mensagem experada não condiz com mensagem retornada"
        assert restaurant.number_served == new_increment_number_served, "O valor da variavel number_served não foi incrementada"

    def test_increment_number_served_with_invalid_number(self):
        # Setup
        restaurant_name = "Restaurante Lixo"
        cuisine_type = "Lixo"
        restaurant = Restaurant(restaurant_name, cuisine_type)
        restaurant.open_restaurant()
        new_increment_number_served = None
        expected_message = "Valor informado invalido!"
        expected_number_served = 0

        # Act
        result = restaurant.increment_number_served(new_increment_number_served)

        # Assert
        assert expected_message == result, "Mensagem de erro experada não condiz com a mensagem de erro retornada"
        assert restaurant.number_served == expected_number_served, "O número de servidos foi incrementado"

    def test_increment_number_served_with_restaurant_close(self):
        # Setup
        restaurant_name = "Restaurante Lixo"
        cuisine_type = "Lixo"
        restaurant = Restaurant(restaurant_name, cuisine_type)
        new_increment_number_served = 5
        expected_result = f"{restaurant_name} está fechado!"
        expected_number_served = 0

        # Act
        result = restaurant.increment_number_served(new_increment_number_served)

        # Assert
        assert result == expected_result, "Mensagem de erro experada não condiz com a mensagem de erro retornada"
        assert restaurant.number_served == expected_number_served, "O número de servidos foi incrementado"