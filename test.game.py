# test random1
import unittest
from unittest.mock import patch
from io import StringIO
from random import seed
from game import request_number, user_turn, pc_turn, play_again

# test for the request_number function


class TestRequestNumber(unittest.TestCase):
    @patch('builtins.input', side_effect=["abc", "-1", "0", "101", "50"])
    def test_request_number_invalid_input(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertEqual(request_number(), 50)
            expected_output = "Por favor, ingresa un número entero válido entre 1 y 100.\n" * 4
            self.assertEqual(fake_out.getvalue(), expected_output)


class TestUserTurn(unittest.TestCase):
    @patch('builtins.input', side_effect=["50"])  # simula
    def test_user_turn_correct_guess(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(user_turn(50))
            expected_output = "¡Felicidades! Has acertado.\n"
            self.assertEqual(fake_out.getvalue(), expected_output)

    @patch('builtins.input', side_effect=["40"])
    def test_user_turn_guess_higher(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertFalse(user_turn(50))
            expected_output = "Esta vez no lo has logrado. El número es mayor\n\n"
            self.assertEqual(fake_out.getvalue(), expected_output)

    @patch('builtins.input', side_effect=["60"])
    def test_user_turn_guess_lower(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertFalse(user_turn(50))
            expected_output = "Esta vez no lo has logrado. El número es menor\n\n"
            self.assertEqual(fake_out.getvalue(), expected_output)


class TestPcTurn(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    # Mock randint para que siempre devuelva 50
    @patch('game.randint', return_value=50)
    def test_pc_turn_correct_guess(self, mock_randint, mock_stdout):
        secret_num = 50
        self.assertTrue(pc_turn(secret_num))
        expected_output = "El número que la computadora ha ingresado es: 50\n¡La pc ha acertado!\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    # Mock randint para que siempre devuelva 70
    @patch('game.randint', return_value=70)
    def test_pc_turn_incorrect_guess_less(self, mock_randint, mock_stdout):
        secret_num = 50
        # La pc no ha adivinado el número secreto
        self.assertFalse(pc_turn(secret_num))
        expected_output = "El número que la computadora ha ingresado es: 70\nLa pc no lo ha conseguido. El número secreto es menor.\n\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    # Mock randint para que siempre devuelva 30
    @patch('game.randint', return_value=30)
    def test_pc_turn_incorrect_guess_high(self, mock_randint, mock_stdout):
        secret_num = 50
        # La pc no ha adivinado el número secreto
        self.assertFalse(pc_turn(secret_num))
        expected_output = "El número que la computadora ha ingresado es: 30\nLa pc no lo ha conseguido. El número secreto es mayor.\n\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
