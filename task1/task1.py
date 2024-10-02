import sys


def circular_path(n, m):
    # Создаем массив от 1 до n
    circular_array = list(range(1, n + 1))
    path = []  # Путь, который будем выводить в конце
    index = 0  # Начальная позиция

    print(f"Круговой массив: {circular_array}")

    # Добавляем первый элемент в путь
    path.append(circular_array[index])

    while True:
        interval = []
        for _ in range(m):
            # Добавляем элемент в интервал
            interval.append(circular_array[index])
            # Переход на следующий элемент с учетом кругового массива
            index = (index + 1) % n

        # Выводим текущий интервал
        print(f"Интервал: {interval}")


        if interval[-1] not in path:
            path.append(interval[-1])
        else:
            break

        # Начинаем новый интервал с последнего элемента текущего интервала
        index = (index - 1 + n) % n  # Оставляем индекс на последнем элементе текущего интервала

    # Преобразуем путь в строку
    return ' '.join(map(str, path))


if __name__ == "__main__":
    try:
        # Ввод значений n и m с клавиатуры
        n = int(input("Введите значение n: "))
        m = int(input("В5ведите значение m: "))
    except ValueError:
        print("Аргументы должны быть целыми числами.")
        sys.exit(1)

    result = circular_path(n, m)
    print(f"Путь: {result}")
