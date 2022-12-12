def encryptionCaesar(text: str, shift: int) -> str:
    """Функция шифрования. На вход принимает
    исходную строку и смещение. На выходе
    зашифрованная строка."""
    res = ''
    dictionary = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    symbol = [' ', ',', '!', '.', '?']
    # Проходимся по каждому символу в тексте
    for t in text:
        # Проверяем что символ есть в словаре
        if t in dictionary:
            # Узнаём индекс буквы словаря
            for i in range(len(dictionary)):
                # Если порядковый номер буквы + ключ находятся
                # выходит за диапазон словаря
                if dictionary[i] == t and i + shift >= len(dictionary):
                    # Добавляем к строке
                    res += dictionary[(i + shift) % len(dictionary)]
                # Если порядковый номер буквы + ключ находятся
                # не выходит из диапазона словаря
                elif len(dictionary) > i + shift > 0 and dictionary[i] == t:
                    # Добавляем к строке
                    res += dictionary[i + shift]
        elif t in symbol:
            res += t
        # Если символа нет в словарях то пропускаем его
        else:
            pass
    # Возвращаем зашифрованный текст
    return res


def decryptionCaesar(text: str, shift: int) -> str:
    """Функция дешифрования. На вход принимает
    зашифрованную строку и смещение.
    На выходе исходная строка."""
    res = ''
    dictionary = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    symbol = [' ', ',', '!', '.', '?']
    for t in text:
        if t in dictionary:
            for i in range(len(dictionary)):
                # Если порядковый номер буквы + ключ находятся
                # не выходит из диапазона словаря
                if dictionary[i] == t and 0 <= i - shift <= len(dictionary):
                    # Добавляем букву по индексу
                    res += dictionary[i - shift]
                # Если порядковый номер буквы + ключ находятся
                # выходит за диапазон словаря
                elif i - shift < 0 and dictionary[i] == t:
                    # Добавляем букву по индексу
                    res += dictionary[(i - shift) % len(dictionary)]
        elif t in symbol:
            res += t
        # Если символа нет в словарях то пропускаем его
        else:
            pass
            # Возвращаем зашифрованный текст
    return res
