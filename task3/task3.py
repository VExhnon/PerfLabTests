import sys
import json

def load_json(file_path):
    """Загружает данные из JSON файла."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json(file_path, data):
    """Сохраняет данные в JSON файл."""
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def update_test_values(tests, values_dict):
    """Обновляет значения тестов на основе словаря values_dict."""
    for test in tests:
        test_id = test.get("id")
        if test_id in values_dict:
            test["value"] = values_dict[test_id]  # Обновляем значение

        # Рекурсивное обновление вложенных тестов
        if "values" in test:
            update_test_values(test["values"], values_dict)

def main():
    if len(sys.argv) != 4:
        print("Введите три аргумента: путь к values.json, путь к tests.json и путь к report.json.")
        sys.exit(1)

    # Считываем пути к файлам из аргументов командной строки
    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    # Загружаем данные из JSON файлов
    values_data = load_json(values_file)
    tests_data = load_json(tests_file)

    # Преобразуем список значений в словарь для быстрого поиска
    values_dict = {item["id"]: item["value"] for item in values_data["values"]}

    # Обновляем значения тестов
    update_test_values(tests_data["tests"], values_dict)

    # Сохраняем обновленные данные в report.json
    save_json(report_file, tests_data)

    print(f"Отчет успешно сформирован и сохранен в {report_file}")

if __name__ == "__main__":
    main()
