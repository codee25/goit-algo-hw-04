def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:

            for line in file:
                cleaned_line = line.strip()
                print(cleaned_line)
                if not cleaned_line:
                    continue

                parts = cleaned_line.split(',')
                print(parts)
                if len(parts) == 2:
                    try:
                        salary = int(parts[1])
                        total += salary
                        count += 1
                    except ValueError:
                        print(
                            f"Помилка: Некоректне значення зарплати у рядку: {cleaned_line}. Пропускаємо.")
                        continue

        if count > 0:
            average = total / count
        else:
            average = 0

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return (0, 0)

    except Exception as e:
        print(f"Виникла неочікувана помилка при роботі з файлом: {e}")
        return (0, 0)

    return (total, average)


path_to_file = "salary.txt"
total, average = total_salary(path_to_file)

print(
    f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
