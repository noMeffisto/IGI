from geometric_lib.circle import area as circle_area, perimeter as circle_perimeter
from geometric_lib.square import area as square_area, perimeter as square_perimeter

# Ввод данных пользователем
radius = float(input("Enter the radius of the circle: "))
side = float(input("Enter the side length of the square: "))

# Вычисление и вывод результатов для круга
print(f"Circle area (radius={radius}): {circle_area(radius)}")
print(f"Circle perimeter (radius={radius}): {circle_perimeter(radius)}")

# Вычисление и вывод результатов для квадрата
print(f"Square area (side={side}): {square_area(side)}")
print(f"Square perimeter (side={side}): {square_perimeter(side)}")