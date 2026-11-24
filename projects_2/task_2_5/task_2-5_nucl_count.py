sequence = input("Введите последовательность ДНК: ")
sequence_up = sequence.upper()

length = len(sequence)

print("\n=== Анализ последовательности ДНК ===")
print(f"\nПоследовательность в верхнем регистре: {sequence_up}")
print("\nПодсчёт нуклеотидов:")

for nucl in "ATGC":
    count = sequence_up.count(nucl)
    percent = (count / length) * 100 if length > 0 else 0
    print(f"{nucl}: {count} ({percent:.1f}%)")

print(f"\nОбщая длина: {length} нуклеотидов")
