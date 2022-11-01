import re

text = input("Write your text: ")
phrases = []
final = re.sub(r"\W+", r" ", text).split(' ')       #удаляем символы, которые не являются словами

for i in range(len(final)):
    tmp = ""
    for j in range(i + 1, len(final) + 1):          #после окончания каждой итерации цикла получаем одну из подстрок данной строки
        tmp = ""
        for k in range(i, j):
            tmp += final[k] + " "
        match = re.search(r"\bВТ\b(?:[ ]\w*){,5}\bИТМО\b", tmp)
        if match and (match[0] not in phrases):
            phrases.append(match[0])                #добавляем различные! строчки в новый массив

phrases.sort(key=len)

if len(phrases) != 0:
    for i in range(len(phrases)):
        print(phrases[i])
else:
    print("No matches")