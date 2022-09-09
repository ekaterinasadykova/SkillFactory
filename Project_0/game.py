"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    # предполагаемое число
    predict_number = 50
    # максимальное число диапазона
    max_number = 100
    # минимальное число диапазона
    min_number = 1
    while True:
        count += 1

        if number == predict_number:
            break  # выход из цикла если угадали
        elif number > predict_number:
            # двигаем минимальную границу диапазона вверх
            min_number = predict_number
            # пытаемся угадать число делением диапазона пополам
            # ceil используется для приведения результата деления пополам к большему целому
            predict_number = predict_number + np.ceil((max_number - predict_number) / 2)
        else:
            # двигаем максимальную границу диапазона вниз
            max_number = predict_number
            # пытаемся угадать число делением диапазона пополам
            # floor используется для приведения результата деления пополам к меньшему целому
            predict_number = min_number + np.floor((predict_number - min_number) / 2)

    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
