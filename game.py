"""game guess number"""
from random import randint

# Solicitar el número al usuario
# user_num = 0


def request_number():
    """Request the number from the user"""
    while True:
        try:
            numero = int(input("Es tu turno. Adivina el número secreto: "))
            if 1 <= numero <= 100:
                return numero
            else:
                raise ValueError
        except ValueError:
            print("Por favor, ingresa un número entero válido entre 1 y 100.")

# Verificar el número ingresado por el usuario


def user_turn(secret_num):
    """Set up the user's shift"""
    while True:
        user_num = request_number()

        if user_num == secret_num:
            print("¡Felicidades! Has acertado.")
            return True
        elif user_num > secret_num:
            print("Esta vez no lo has logrado. El número es menor\n")
        else:
            print("Esta vez no lo has logrado. El número es mayor\n")
        return False

# Turno de la computadora


def pc_turn(secret_num):
    """Set up the pc's shift"""
    system_num = randint(1, 100)
    print(f"El número que la computadora ha ingresado es: {system_num}")
    if system_num == secret_num:
        print("¡La pc ha acertado!")
        return True
    elif system_num > secret_num:
        print("La pc no lo ha conseguido. El número secreto es menor.\n")
        return False
    else:
        print("La pc no lo ha conseguido. El número secreto es mayor.\n")
        return False


def play_again():
    """Request if user want play again"""
    while True:
        answer = input("¿Quieres jugar otra vez? (s/n)\n")
        if answer.lower() == "s":
            return True
        elif answer.lower() == "n":
            return False
        else:
            print("Por favor, ingresa 's' para sí o 'n' para no.\n")

# Función principal del juego


def magic_num():
    """Set up the game"""
    while True:
        secret_num = randint(1, 100)
        print(secret_num)
        user_attempts = 0
        system_attempts = 0

        print("¡Bienvenida!")
        print("Competirás con la pc para encontrar un número secreto")
        print("Este se encuentra entre el número 1 y el número 100 ")

        while True:
            user_attempts += 1
            if user_turn(secret_num):
                print(f"Lo has conseguido en el intento # {user_attempts}\n")
                break

            system_attempts += 1
            if pc_turn(secret_num):
                print(f"La pc lo consiguió al {system_attempts} intento\n")
                break

        if not play_again():
            print("Gracias por jugar. Hasta luego.\n")
            break


# Llama la función principal del juego
if __name__ == "__main__":
    magic_num()
