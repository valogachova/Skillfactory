import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Угадываем число в диапазоне от 1 до 100, используя бинарный поиск.
    Функция принимает число, сгенерированное программой, и возвращает число попыток.
    Args:
        number (int): Загаданное число.
    Returns:
        int: Число попыток.
    """
    count = 0
    lower_bound = 1
    upper_bound = 100
    midpoint = 50  
    

    while True:
        count += 1

        if number == midpoint:
            break
        elif midpoint < number:
            lower_bound = number + 1
        else:
            upper_bound = number - 1

        # Adjust the prediction to the midpoint of the new bounds
        midpoint = (lower_bound + upper_bound) // 2

    return count


number = np.random.randint(1, 101)
print(f"Загаданное компьютером число: {number}", "Программа угадала это число за", game_core_v3(number), "попыток.")