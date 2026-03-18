# объявление функции
def print_case_counts(s):
    upper_count = 0
    lower_count = 0
    
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
            
    print(f"Букв в верхнем регистре: {upper_count}")
    print(f"Букв в нижнем регистре: {lower_count}")

# Пример проверки:
# print_case_counts("Hello World! 123")

# считываем данные
s = input()

# вызываем функцию
print_case_counts(s)