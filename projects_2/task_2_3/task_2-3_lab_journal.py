# task_2-3_lab_journal.py
# Программа имитирует заполнение страницы электронного лабораторного журнала
# с адаптивной шириной рамки

# 1. Сбор данных
name = input("Введите ФИО исследователя: ")
date = input("Введите дату (ДД.ММ.ГГГГ): ")
experiment = input("Введите название эксперимента: ")
conclusion = input("Введите вывод: ")

# 2. Определение ширины рамки
# Минимальная ширина внутренней части - 48 символов (чтобы влез заголовок)
# Если введенные данные длиннее, рамка расширяется
min_width = 48
max_data_len = max(len(name), len(date), len(experiment))

# Рассчитываем ширину с учетом левой части "ФИО исследователя : " (19 символов)
# и пробелов по краям (2 символа)
required_width = max_data_len + 19 + 2
frame_width = max(min_width, required_width)

# 3. Формирование рамки
line = "+" + "-" * frame_width + "+"
header = f"| {'Электронный лабораторный журнал':<{frame_width}} |"

# Выравниваем левую часть (метки) и правую часть (значения)
label_width = 17
info_name = f"| {'ФИО исследователя':<{label_width}} : {name:<{frame_width - label_width - 3}} |"
info_date = f"| {'Дата':<{label_width}} : {date:<{frame_width - label_width - 3}} |"
info_exp = f"| {'Эксперимент':<{label_width}} : {experiment:<{frame_width - label_width - 3}} |"
conclusion_title = f"| {'Вывод:':<{frame_width}} |"

# 4. Разбиваем вывод на строки, чтобы он поместился в рамку
words = conclusion.split()
lines = []
current_line = ""

for word in words:
    if len(current_line) + len(word) + 1 <= frame_width:
        current_line += word + " "
    else:
        lines.append(current_line.strip())
        current_line = word + " "

if current_line:
    lines.append(current_line.strip())

conclusion_lines = [f"| {line:<{frame_width}} |" for line in lines]

# 5. Запись в файл с использованием with open
with open("journal.txt", "w", encoding="utf-8") as file:
    file.write(line + "\n")
    file.write(header + "\n")
    file.write(line + "\n")
    file.write(info_name + "\n")
    file.write(info_date + "\n")
    file.write(info_exp + "\n")
    file.write(line + "\n")
    file.write(conclusion_title + "\n")
    for cline in conclusion_lines:
        file.write(cline + "\n")
    file.write(line + "\n")

print("\nДанные успешно записаны в файл journal.txt")
