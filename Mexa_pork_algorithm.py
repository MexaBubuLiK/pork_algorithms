import random
import math

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def check(guess, word):
    correct = 0
    for i in range(len(guess)):
        if guess[i] == word[i]:
            correct += 1
    return correct
# ================

# Составляем массив из всех возможных вариантов комбинаций из длины слова word


def combinations(lst):
    if (len(lst) == 0):
        return []
    elif (len(lst) == 1):
        return [lst]
    else:
        l = []
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]
            for c in combinations(xs):
                l.append([x]+c)
        return l
# конец ================

# Функций гессера


def guesser(word):

    array_seed = []

    temp_str = ""

    word_characters = []

    check_usage = 0

    final_array = []

    index = 0
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
        if (check(array_seed[i], word) > 0):
            for j in range(check(array_seed[i], word)):
                word_characters.append(alphabet[i])
        if (len(word_characters) == len(word)):
            # print(word_characters)
            break
# конец ================

# Переводим массив в строковый вид
    for c in combinations(word_characters):
        index += 1
        for i in range(len(c)):
            temp_str += c[i]
        final_array.append(temp_str)
        temp_str = ""
        #print("Элемент номер " + str(index) + " = " + final_array[index - 1])
    # конец ================

    # print("Поиск строки по функции начинается")

    # print("Количетсво итераций до построения финального массива = "+str(check_usage))

# Ищем искомую строку
    for i in range(len(final_array)):
        check_usage += 1
        if (check(final_array[i], word) == len(word)):
            #print("Загадано слово " + str(final_array[i]))
            #print("Финальное количесво итераций = " + str(check_usage))
            break
        # конец ================
    return check_usage


array_for_average = []
sum = 0

with open("C:/Users/Mexa/Downloads/words.txt") as fp:
    for line in fp:
        print("У слова " + str(line[0:5]) + " " +
              str(guesser(line[0:5])) + " итераций")
        sum += guesser(line[0:5])
        array_for_average.append(guesser(line[0:5]))
        # print(guesser(line))

print("Среднее количество итераций за весь файл = " +
      str(sum/len(array_for_average)))

# Составляем массив из всех возможных вариантов комбинаций из длины слова word


def combinations(lst):
    if (len(lst) == 0):
        return []
    elif (len(lst) == 1):
        return [lst]
    else:
        l = []
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]
            for c in combinations(xs):
                l.append([x]+c)
        return l
# конец ================
