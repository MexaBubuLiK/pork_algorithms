import random
import math

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def check(guess, word):
    correct = 0
    for i in range(len(guess)):
        if guess[i] == word[i]:
            correct += 1
    if (correct == len(word)):
        return "done"
    else:
        return correct
# ================

# Функция возвращает массив строк со ступенчатым видом чисел


def makeArray(lenght, array):
    test_array = []
    for i in range(lenght):
        test_array.append("")
        for j in range(lenght):
            test_array[i] += str(array[i][j])
    return test_array
# конец ================
# print(check("guess", "guess"))


def guesser(word):

    array_seed = []

    temp_str = ""

    word_characters = []

    check_usage = 0

    # Создаём массив строк с однобуквенными элементами
    for i in range(len(alphabet)):
        for j in range(len(word)):
            temp_str += alphabet[i]
        array_seed.append(temp_str)
        temp_str = ""
    # конец ================

    # print(array_seed)

    # Вычисляем все существующие буквы для комбинаций
    for i in range(len(array_seed)):
        check_usage += 1
        if (check(array_seed[i], word) == "done"):
            return check_usage
        if (check(array_seed[i], word) > 0):
            for j in range(check(array_seed[i], word)):
                word_characters.append(alphabet[i])
        if (len(word_characters) == len(word)):
            # print(word_characters)
            break

    constructor = ["" for _ in range(len(word_characters))]
    # print(constructor)
    for k in range(len(word_characters)):
        array = [[0 for _ in range(len(word_characters))]
                 for _ in range(len(word_characters))]
        for i in range(len(word_characters)):
            for j in range(len(word_characters)):
                if (i == j):
                    array[i][j] = word_characters[k]
                    # print(array[i][j].replace("0", "f", 1))
                    # print("Строка " + str(i) + " столбец " + str(j))
        # Создаём массив из 5 строк где искомывый символ находится на каждом месте из 5
        test_array = makeArray(len(word_characters), array)
        # В цикле заполняем все пустые места чтобы получить искомое слово
        for i in range(len(test_array)):
            if (str(constructor[i]) == ""):
                check_usage += 1
                if (check(test_array[i], word) == 1):
                    constructor[i] += word_characters[k]
        # Переводим в строковый вид
        temp_str = ""
        for c in range(len(constructor)):
            temp_str += str(constructor[c])

    # Выводим найденное слово
    # print(temp_str)
    # конец ================
    return check_usage
# конец ================


array_for_average = []
sum = 0

with open("C:/Users/Mexa/Downloads/words.txt") as fp:
    for line in fp:
        print("У слова " + str(line[0:5]) + " " +
              str(guesser(line[0:5])) + " итераций")
        sum += guesser(line[0:5])
        array_for_average.append(guesser(line[0:5]))
        # print(guesser(line))

print("Среднее количество итераций за весь файл (второй алгоритм) = " +
      str(sum/len(array_for_average)))
