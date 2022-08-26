# Даны две строки. Посчитайте сколько раз каждый символ 
# первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

symbols = input("Ввести симовлы ")
phrase = 'onetwonine'
dictionary = [] # список пустой

for symbol in symbols:
    if symbol not in dictionary:
        dictionary.append(symbol) # вносим символ в словарь
        count = 0
        for letter in phrase:
            if symbol == letter:
                count += 1
        print(f"Символ {symbol} встречается в '{phrase}' {count} раза")
    else:
        print(f"Символ {symbol} не был учтен")