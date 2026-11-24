sensor_operator = int(input("Введите имя оператора:"))
sensor_start_data = int(input("Введите текущее значение давления (Па):"))
with open("sensor_log.txt", "a", encoding="utf-8") as f:
  f.write(f"{sensor_operator}\t{{sensor_start_data}\n")
print("Данные успешно сохранены в sensor_log.txt")
