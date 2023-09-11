import random
import math

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def check(guess, word):
    correct = 0
    for i in range(len(guess)):
        if guess[i] == word[i]:
            correct += 1
    else:
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

# Создаём класс с индивидумами в виде списка


class Individual(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.fitness = 0
# конец ================

# Начало ген алгоритма

# Клонируем чтоб не повторялись


def clone(value):
    # print(value.fitness)
    ind = Individual(value[:])
    # print(ind.fitness)
    #ind.fitness = check(value, word)
    # print(ind.fitness)
    return ind  # value


# конец ================
# clone(population[0])

# С помощью турнира отбираем рандомные особи, и среди них выбираем всех у кого высокая приспособленность


def selTournament(population, population_size):
    offspring = []
    print("===== Начался турнирный отбор ======")
    print("====== Текущая популяция ======")
    for i in range(population_size):
        print("Индивид № " + str(i + 1) + " " + str(population[i]))
    print("\n============== ИТОГИ ==============")
    for n in range(population_size):
        i1 = i2 = i3 = 0
        while i1 == i2 or i1 == i3 or i2 == i3:
            i1 = random.randint(0, population_size-1)
            i2 = random.randint(0, population_size-1)
            i3 = random.randint(0, population_size-1)
        offspring.append(max(
            [population[i1], population[i2], population[i3]], key=lambda ind: ind.fitness))
        print("Победитель № " + str(n + 1) + " " + str(offspring[n]))
    return offspring


# конец ================
#print(selTournament(population, population_size))

# С помощью кроссинговера свапаем части хромосом


def startSex(child1, child2):
    s = random.randint(1, len(child1)-1)
    print("Первый Чел до "+str(child1))
    print("Второй Чел до "+str(child2))
    print("Точка хромосомного переноса = " + str(s))
    temp1 = child1[s:]
    temp2 = child2[s:]
    child1[s:] = temp2
    child2[s:] = temp1
    print("Первый Чел после "+str(child1))
    print("Второй Чел после "+str(child2) + "\n")
# конец ================


# print(population[0])
# print(population[2])
#startSex(population[0], population[2])
# print(population[0])
# print(population[2])

# Мутации


def startMutation(mutant, word_characters):
    print("Мутант до " + str(mutant))
    indexMutant = random.randint(0, len(word_characters)-1)
    if (mutant[indexMutant] == word_characters[indexMutant]):  # word_characters
        #print("Отдельный ген мутанта " + str(mutant[index]) + " равен случайной мутации " + str(word_characters[index]))
        random.shuffle(mutant)
    else:
        #print("Отдельный ген мутанта " + str(mutant[index]) + " отличается от случайной мутации " + str(word_characters[index]))
        mutant[indexMutant] = word_characters[indexMutant]  # alphabet
    print("Мутант после " + str(mutant))


# конец ================

def startMutationSecond(mutant):
    #print("Вероятность шафла равна = 0.2")
    print("Мутант до " + str(mutant))
    indexMutant = random.randint(0, len(mutant)-1)
    index = random.randint(0, len(alphabet)-1)
    while (mutant[indexMutant] == alphabet[index]):
        index = random.randint(0, len(alphabet)-1)
    mutant[indexMutant] = alphabet[index]
    if (random.random() <= 0.2):
        random.shuffle(mutant)
        #print("Шафл сработал")
    print("Мутант после " + str(mutant))

#startMutation(combinations("forks")[ random.randint(0, math.factorial(len("forks"))-1)])

# print(fitness_Values)
# print(max(fitness_Values))


def generateLetters(lenght):
    array = []
    for i in range(lenght):
        array.append(alphabet[random.randint(0, len(alphabet)-1)])
    return array


def guesser(word):

    population_size = 10

    population = []

    fitness_Values = []

    generationCounter = 0

    generationThreshhold = 15

    crossover_Probability = 0.9

    mutation_Probability = 0.8

    max_Generations = 10000

    array_seed = []

    array_seed_second = []

    temp_str = ""

    temp_seed = []

    word_characters = []

    check_usage = 0

    # Создаём массив строк с однобуквенными элементами
    for i in range(len(alphabet)):
        for j in range(len(word)):
            temp_str += alphabet[i]
            temp_seed.append(alphabet[i])
        array_seed.append(temp_str)
        array_seed_second.append(temp_seed)
        temp_str = ""
        temp_seed = []
    # конец ================
    # Вычисляем все существующие буквы для комбинаций
    for i in range(len(array_seed)):
        check_usage += 1
        if (check(array_seed[i], word) > 0):
            for j in range(check(array_seed[i], word)):
                word_characters.append(alphabet[i])
        if (len(word_characters) == len(word)):
            # print(word_characters)
            break

    print("\nСтартовая выборка популяции\n")
    # Создаём популяцию и записываем значения их приспособленности в массив приспособленностей
    for i in range(population_size):
        ind = Individual(combinations(word_characters)
                         [i*random.randint(9, 12)])
        print("Индивидум № " + str(i + 1) + " " + str(ind))
        ind.fitness = check(ind, word)
        population.append(ind)
        fitness_Values.append(population[i].fitness)
    # конец ================
    # Тут происходит генетический алгоритм как раз
    if (max(fitness_Values) == len(word) and generationCounter == 0):
        print("=======================================")

        print("Поколение: " + str(generationCounter) + " Макс приспособ. = " + str(max(fitness_Values)
                                                                                   ) + ", Средняя приспособ = " + str(sum(fitness_Values) / population_size))

        best_index = fitness_Values.index(max(fitness_Values))

        worst_index = fitness_Values.index(min(fitness_Values))
        print("Лучший индивидум = " + str(population[best_index]))

        print("Худший индивидум = " + str(population[worst_index]))

        print("Количество итераций = " + str(check_usage +
              generationCounter * population_size) + "\n")

        return check_usage + generationCounter * population_size

    while max(fitness_Values) < len(word) and generationCounter < max_Generations:  # max_Generations
        generationCounter += 1
        offspring = selTournament(population, population_size)
        offspring = list(map(clone, offspring))

        print("\n====== Случайный кроссинговер ======")

        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < crossover_Probability:  # crossover_Probability
                print("Отобраны родители " + str(child1) + " и " + str(child2))
                startSex(child1, child2)

        for i in range(population_size):
            print("Потомки № " + str(i + 1) + " " + str(offspring[i]))

        print("\n====== Старт случайных мутаций ======")

        for i in range(len(offspring)):
            if random.random() < mutation_Probability:  # mutation_Probability
                print("-----------------------------------")
                print("Индивид № " + str(i+1) +
                      " доброволец на мутацию - " + str(offspring[i]) + "\n")
                startMutation(offspring[i], word_characters)

        for ind in offspring:
            #print("Челик " + str(ind) + " приспособленность ДО = " + str(ind.fitness))
            ind.fitness = check(ind, word)
            #print("Челик " + str(ind) + " приспособленность ПОСЛЕ = " + str(ind.fitness))

        population[:] = offspring
        fitness_Values = [ind.fitness for ind in population]

        maxFitness = max(fitness_Values)
        averageFitness = sum(fitness_Values) / population_size
        print("\n")
        for i in range(population_size):
            print("Текущий индивид № " + str(i + 1) + " " + str(population[i]))
        # Доп мутации
        if (maxFitness <= len(word) - 1 and generationCounter >= generationThreshhold):
            print("\n ===== Дополнительные индивиды для посева =====")
            for i in range(population_size):
                # Если число поколений перевалило трешхолд, то с некоторой вероятностью заменяем некоторых членов на новичков
                if (random.random() < 0.8):  # mutation_Probability
                    k = random.randint(0, math.factorial(len(word)) - 1)
                    # Проверка на то, что отличаются хромосомы между собой
                    while population[i] == Individual(combinations(word_characters)[k]):
                        k = random.randint(0, math.factorial(len(word)) - 1)
                    print("Вырожденец " + str(population[i]))
                    population[i] = Individual(
                        combinations(word_characters)[k])
                    print("Заменяется на " + str(population[i]) + "\n")
                    population[i].fitness = check(population[i], word)
                    fitness_Values[i] = population[i].fitness

            maxFitness = max(fitness_Values)
            averageFitness = sum(fitness_Values) / population_size
            # print(population[i])

        print("=======================================")

        print("Поколение: " + str(generationCounter) + " Макс приспособ. = " +
              str(maxFitness) + ", Средняя приспособ = " + str(averageFitness))

        best_index = fitness_Values.index(max(fitness_Values))
        worst_index = fitness_Values.index(min(fitness_Values))
        print("Лучший индивидум = " + str(population[best_index]))

        print("Худший индивидум = " + str(population[worst_index]))

        print("Количество итераций = " + str(check_usage +
              generationCounter * population_size))
        print("============== Конец текущего поколения ====================\n")
        # Возвращаем количество итераций
        if (maxFitness == len(word) or generationCounter == max_Generations):
            return check_usage + generationCounter * population_size

# Второй вариант с полностью рандомным посевом


def guesser2(word):

    population_size = 10

    population = []

    fitness_Values = []

    generationCounter = 0

    crossover_Probability = 0.9

    mutation_Probability = 0.8

    max_Generations = 10000

    check_usage = 0

    print("==================СТАРТ==================" + "\n")
    # Создаём популяцию и записываем значения их приспособленности в массив приспособленностей
    for i in range(population_size):
        ind = Individual(generateLetters(len(word)))
        #print("Индивид № " + str(i + 1) + str(ind))
        ind.fitness = check(ind, word)
        population.append(ind)
        fitness_Values.append(population[i].fitness)
    # конец ================
    # Тут происходит генетический алгоритм как раз
    if (max(fitness_Values) == len(word) and generationCounter == 0):
        print("=======================================")

        print("Поколение: " + str(generationCounter) + " Макс приспособ. = " + str(max(fitness_Values)
                                                                                   ) + ", Средняя приспособ = " + str(sum(fitness_Values) / population_size))

        best_index = fitness_Values.index(max(fitness_Values))

        worst_index = fitness_Values.index(min(fitness_Values))
        print("Лучший индивидум = " + str(population[best_index]))

        print("Худший индивидум = " + str(population[worst_index]))

        print("Количество итераций = " + str(check_usage +
              generationCounter * population_size) + "\n")

        return check_usage + generationCounter * population_size

    while max(fitness_Values) < len(word) and generationCounter < max_Generations:  # max_Generations
        generationCounter += 1
        offspring = selTournament(population, population_size)
        offspring = list(map(clone, offspring))
        print("\n====== Случайный кроссинговер ======")
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < crossover_Probability:  # crossover_Probability
                print("Отобраны родители " + str(child1) + " и " + str(child2))
                startSex(child1, child2)
        # print(offspring)
        for i in range(population_size):
            print("Потомки № " + str(i + 1) + " " + str(offspring[i]))
        print("\n====== Старт случайных мутаций ======")
        for i in range(len(offspring)):
            if random.random() < mutation_Probability:  # mutation_Probability
                print("-----------------------------------")
                print("Индивид № " + str(i+1) +
                      " доброволец на мутацию - " + str(offspring[i]) + "\n")
                startMutationSecond(offspring[i])

        for ind in offspring:
            #print("Челик " + str(ind) + " приспособленность ДО = " + str(ind.fitness))
            ind.fitness = check(ind, word)
            #print("Челик " + str(ind) + " приспособленность ПОСЛЕ = " + str(ind.fitness))

        population[:] = offspring
        fitness_Values = [ind.fitness for ind in population]

        maxFitness = max(fitness_Values)
        averageFitness = sum(fitness_Values) / population_size
        print("\n")
        for i in range(population_size):
            print("Текущий индивид № " + str(i + 1) + " " + str(population[i]))
        # Доп мутации
        if (maxFitness <= len(word) - 1 and generationCounter >= max_Generations):  # max_Generations
            for i in range(population_size):
                # Если число поколений перевалило трешхолд, то с некоторой вероятностью заменяем некоторых членов на новичков
                if (random.random() < 0.8):  # mutation_Probability
                    population[i] = Individual(generateLetters(len(word)))
                    population[i].fitness = check(population[i], word)
                    fitness_Values[i] = population[i].fitness

            maxFitness = max(fitness_Values)
            averageFitness = sum(fitness_Values) / population_size
            # print(population[i])

        print("=======================================")

        print("Поколение: " + str(generationCounter) + " Макс приспособ. = " +
              str(maxFitness) + ", Средняя приспособ = " + str(averageFitness))

        best_index = fitness_Values.index(max(fitness_Values))
        worst_index = fitness_Values.index(min(fitness_Values))
        print("Лучший индивидум = " + str(population[best_index]))

        print("Худший индивидум = " + str(population[worst_index]))

        print("Количество итераций = " + str(check_usage +
              generationCounter * population_size))
        print("============== Конец текущего поколения ====================\n")
        # Возвращаем количество итераций
        if (maxFitness == len(word) or generationCounter == max_Generations):
            return check_usage + generationCounter * population_size


    # конец ================
guesser("ruben")
# guesser2("ruben")

#array_for_average = []
#summA = 0
#
# with open("C:/Users/Mexa/Downloads/words.txt") as fp:
#    for line in fp:
#        iteration = guesser(line[0:5])
#        print("У слова " + str(line[0:5]) + " " +
#              str(iteration) + " итераций")
#        summA += iteration
#        array_for_average.append(iteration)
#        # print(guesser(line))
#
# print("Среднее количество итераций за весь файл (второй алгоритм) = " +
#      str(summA/len(array_for_average)))
