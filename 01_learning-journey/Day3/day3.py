print('Введите процент посещаемости:')
attendance = int(input())
print('Сделано ли ДЗ (1 - да, 0 - нет):')
homework_done = int(input())
if attendance > 75 and homework_done == 1:
    result = "Допущен"
else: result = 'Не допущен'

print(result)