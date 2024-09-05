def single_root_words(root_word, *other_words):
    same_words = [] # создаем пустой список
    root_word = root_word.lower() # переводим в нижний регистр
    for i in other_words: # перебираем слова
        other_words = i.lower() # переводим в нижний регистр
        if root_word in other_words or other_words in root_word: # проверяем условие
            same_words.append(i) # добавляем в список если условие выполняется
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)