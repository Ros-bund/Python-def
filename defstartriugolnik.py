# объявление функции
def draw_triangle(fill, base):
    mid = base // 2 + 1
    for i in range(1, mid + 1):
        print(fill * i)
        
    for i in range(mid - 1, 0, -1):
        print(fill * i)
    

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)