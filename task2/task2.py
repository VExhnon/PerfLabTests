import sys
import math

def read_circle_data(file_path):
    """Считываем координаты центра окружности и радиус из файла."""
    with open(file_path, 'r') as file:
        center_x, center_y = map(float, file.readline().strip().split())
        radius = float(file.readline().strip())
    return center_x, center_y, radius

def read_points_data(file_path):
    """Считываем координаты точек из файла."""
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(float, line.strip().split())
            points.append((x, y))
    return points

def determine_point_position(center_x, center_y, radius, point_x, point_y):
    """Определяем положение точки относительно окружности."""
    # Вычисляем расстояние от центра окружности до точки
    distance = math.sqrt((point_x - center_x) ** 2 + (point_y - center_y) ** 2)

    if math.isclose(distance, radius):  # Точка на окружности
        return 0
    elif distance < radius:  # Точка внутри окружности
        return 1
    else:  # Точка снаружи окружности
        return 2

def main():
    if len(sys.argv) != 3:
        print("Введите два аргумента: путь к файлу с окружностью и путь к файлу с точками.")
        sys.exit(1)

    # Считываем пути к файлам
    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    # Считываем данные об окружности
    center_x, center_y, radius = read_circle_data(circle_file)

    # Считываем точки
    points = read_points_data(points_file)

    # Определяем положение каждой точки относительно окружности и выводим результат
    for point_x, point_y in points:
        position = determine_point_position(center_x, center_y, radius, point_x, point_y)
        print(position)

if __name__ == "__main__":
    main()
