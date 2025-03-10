import math
import random
import fcntl

def lcm(a, b):
    """Функция для вычисления НОК двух чисел."""
    return abs(a * b) // math.gcd(a, b)


def lcm_three(a, b, c):
    """Функция для вычисления НОК трёх чисел."""
    return lcm(lcm(a, b), c)


def play_lcm_game(rounds=3):
    """Функция для запуска игры."""
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the smallest common multiple of given numbers.")

    for _ in range(rounds):
        # Генерируем три случайных числа
        a, b, c = random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)
        correct_answer = lcm_three(a, b, c)

        print(f"Question: {a} {b} {c}")
        user_answer = input("Your answer: ")

        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return  # Завершаем игру после первой ошибки

    print(f"Congratulations, {name}!")


# Запуск игры
if __name__ == "__main__":
    play_lcm_game()
