import random
key = [5, 6, 3, 1, 9, 7, 2, 8]
text = input('Введите слово‚: ')
mas = [0] * len(text)
j = 0
for i in range(len(text)):
    if i > 0 and i % len(key) == 0:
        j += 1
    mas[i] = key[i - 8*j]
kod = []
k = min(mas)
while k <= max(mas):
    for i in range(len(mas)):
        if mas[i] == k:
            kod.append(text[i])
        if random.randint(0, 6) == 3:
            kod.append(' ')
    k += 1
print('Шифр: ', kod)

h = 0
while h < len(kod):
    if kod[h] == ' ':
        kod.pop(h)
        h = h - 1
    h += 1
text = [0] * len(kod)
k = min(mas)
j = 0
while k <= max(mas):
    for i in range(len(mas)):
        if mas[i] == k:
            text[i] = kod[j]
            j += 1
    k += 1
print('Дешифр: ', text)