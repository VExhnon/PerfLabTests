import sys


def read_numbers_from_file(file_path):
    """Считываем целые числа из файла."""
    with open(file_path, 'r', encoding='utf-8') as file:
        numbers = [int(line.strip()) for line in file.readlines()]
    return numbers


def min_steps_to_equal_elements(nums):
    """Вычисляем минимальное количество шагов для приведения всех элементов массива к одному числу."""
    # Сортируем массив
    nums.sort()
    # Определяем медиану
    median = nums[len(nums) // 2]
    # Суммируем разницу между каждым элементом и медианой
    steps = sum(abs(num - median) for num in nums)
    return steps


def main():
    if len(sys.argv) != 2:
        print("Введите путь к файлу с массивом чисел в качестве аргумента.")
        sys.exit(1)

    # Считываем путь к файлу
    input_file = sys.argv[1]

    # Читаем числа из файла
    numbers = read_numbers_from_file(input_file)

    # Вычисляем минимальное количество шагов
    result = min_steps_to_equal_elements(numbers)

    # Выводим результат
    print(f"Минимальное количество шагов: {result}")


if __name__ == "__main__":
    main()
