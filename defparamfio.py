# объявление функции
def print_fio(name, surname, patronymic):
    # Берем первые буквы, соединяем их и переводим в верхний регистр
    fio = surname[0] + name[0] + patronymic[0]
    print(fio.upper())

# Пример использования:
# print_fio("Александр", "Пушкин", "Сергеевич") 
# Выведет: ПАС

# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)