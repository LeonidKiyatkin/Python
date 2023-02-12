"""
3) Создать(не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
eng_rus = [['One', 'Один'], ['Two', 'Два'], ['Three', 'Три'],
           ['Four', 'Четыре']]

with open('file2.txt', 'r', encoding='utf-8') as data:
    lines = data.read()
    for i in range(len(eng_rus)):
        lines = lines.replace(eng_rus[i][0], eng_rus[i][1])

with open('file2answ.txt', 'w', encoding='utf-8') as data:
    data.write(lines)
