def get_cats_info(path):

    cats_list = []

    try:
        with open(path, 'r', encoding='utf-8') as file:

            for line in file:
                cleaned_line = line.strip()

                if not cleaned_line:
                    continue

                parts = cleaned_line.split(',')

                if len(parts) == 3:
                    cat_id, name, age = parts

                    cat_dict = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }

                    cats_list.append(cat_dict)
                else:
                    print(
                        f"Помилка: Рядок має некоректний формат: {cleaned_line}. Пропускаємо.")

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return []

    except Exception as e:
        print(f"Виникла неочікувана помилка при роботі з файлом: {e}")
        return []

    return cats_list


cats_info = get_cats_info("cats_file.txt")
print(cats_info)
