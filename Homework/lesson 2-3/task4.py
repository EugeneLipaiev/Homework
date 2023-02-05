a = 37
b = 65
c = 78

P_delta = a + b + c #периметр трикутника
print(P_delta)

S_delta = a*b/0.5 #визначаємо площу трикутника через катіти
print(S_delta)

h = a*b/c
S_delta_1 = c*h/0.5 #перевіряємо площу трикутника через висоту
print(S_delta_1)
S_delta = S_delta_1

radius_delta = (a+b-c)/0.5 #визначаємо радіус кола присаного в трикутник
print(radius_delta)

results_1 = "|{Num1} {Num2:>19.0f}|"
print("_" *40)
print(results_1.format(
    Num1 = "Perimeter of delta",
    Num2 = P_delta
))
results_2 = "|{Num3} {Num4:>24.0f}|"
print(results_2.format(
    Num3 = "Area of delta",
    Num4 = S_delta
))
results_3 = "|{Num5} {Num6:>5.0f}|"
print(results_3.format(
    Num5 = "Area of delta through the height",
    Num6 = S_delta
))
results_4 = "|{Num7} {Num8:>25.0f}|"
print(results_4.format(
    Num7 = "Radius delta",
    Num8 = radius_delta))
print("_" *40)


