print("-----Ипотечный калькуляттор-----")
print("Базовая ставка составляет 10%.")
print("--------------------------------")
rate = 10

print("\nВыберите свой регион: "
      "\n1 - Центральный\n2 - Северо-Западный"
      "\n3 - Южный\n4 - Северо-Кавказский"
      "\n5 - Приволжский\n6 - Уральский"
      "\n7 - Сибирский\n8 - Дальневосточный")
region_value = int(input())

print("У вас более трех детей?:\n1 - Да\n2 - Нет")
kid_value = int(input())

print("Есть ли у вас зарплатный проект в нашем банке?:\n1 - Да\n2 - Нет")
salary_value = int(input())

print("Оформлено ли у вас страхование в нашем банке?:\n1 - Да\n2 - Нет")
insurance_value = int(input())

if region_value == 8:
    rate = 2
else:
    if kid_value == 1:
        rate = rate - 1
    if salary_value == 1:
        rate = rate - 0.5
    if insurance_value == 1:
        rate = rate - 1.5

print("Ваша ставка: ", rate, "%")