def logic_circuit():
    print("--- Расчет логической схемы (Вариант 4) ---")
    try:
        # Ввод данных пользователем
        a = int(input("Введите A (0 или 1): "))
        b = int(input("Введите B (0 или 1): "))
        c = int(input("Введите C (0 или 1): "))
        d = int(input("Введите D (0 или 1): "))

        if not all(val in [0, 1] for val in [a, b, c, d]):
            print("Ошибка: вводите только 0 или 1!")
            return

        # Вспомогательные функции для логических элементов
        def nand(*args): return int(not all(args))
        def nor(*args): return int(not any(args))
        def xor(x, y): return x ^ y

        # УРОВЕНЬ 1 (1 элемент) 
        s1 = xor(a, b)

        # УРОВЕНЬ 2 (4 элемента И-НЕ) 
        n1 = nand(a, s1)
        n2 = nand(b, s1)
        n3 = nand(c, s1)
        n4 = nand(d, s1)

        # УРОВЕНЬ 3 (3 элемента ИЛИ-НЕ) 
        # Используются выходы NAND и прямые сигналы A, B, C 
        r1 = nor(n1, n2, a)
        r2 = nor(n2, n3, b)
        r3 = nor(n3, n4, c)

        # ВЫХОД (1 элемент И-НЕ)
        y = nand(r1, r2, r3)

        # Вывод промежуточных данных для отчета 
        print("\n--- Промежуточные состояния для схемы ---")
        print(f"S1 (XOR): {s1}")
        print(f"NAND-уровень: N1={n1}, N2={n2}, N3={n3}, N4={n4}")
        print(f"NOR-уровень:  R1={r1}, R2={r2}, R3={r3}")
        print(f"ИТОГОВЫЙ ВЫХОД Y: {y}")

    except ValueError:
        print("Ошибка: вводите только целые числа (0 или 1)!")

if __name__ == "__main__":
    logic_circuit()
