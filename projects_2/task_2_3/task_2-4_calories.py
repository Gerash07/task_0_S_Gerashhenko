mass_protein = input("Введите массу белков в продукте (г):")
mass_fats = input("Введите массу жиров в продукте (г):")
mass_carb = input("Введите массу углеводов в продукте (г):")

print(f"Кал={(mass_protein*4)+(mass_fats*9)+(mass_carb*4)}")
