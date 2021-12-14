revenue = float(input("Введите значение выручки (RUB) - "))
costs = float(input("Введите значение издержек (RUB) - "))
result = revenue - costs
if result > 0:
    print(f"Поздравляю! Ваша компания работает с прибылью {result} RUB!")
    print(f"Рентабельность выручки составила {100 * result / revenue:.1f}%")
    personal_n = int(input("Сколько счастливых целочисленных сотрудников работает в вашей компании? "))
    print(f"Если вы раздадите прибыль компании сотрудникам, то каждый получит по {result / personal_n:.3f} RUB.")
elif result < 0:
    print(f"Увы ваша компания пока сработала с убытком {-result} RUB!")
else:
    print("Ноль это тоже хороший результат")
