# pork_algorithms
Внутри алгоритмы для решения задачи угадываниям слова из 5-ти букв

Чтобы запустить каждый алгоритм достаточно в функции gueesser("слово") вставить слово из пяти букв(хотя код написан с учётом любого количества букв, но возможны правки минимальные.
Файл "words.txt" нужен, чтобы проверить эфективность алгоритма
В текущем виде надо правильный путь указать в блоке с открытием файла вместо "C:/Users/Mexa/Downloads/words.txt" указать любой правильный путь, как правило это просто "words.txt"

================================ЗАДАЧКА===========================================
Зашифровано слово из 5 букв
Функция check принимает строку из 5 букв
Возвращает количество угаданных позиций (0-5)

Пример

Загадано - НОЖИК 

ЖОЖОЖ >> 2
ННННН >> 1
КНИЖО >> 0

Нужно за наименьшее количество итераций заставить функцию выдать число 5 (угадать слово)

Примечание:
Нельзя: менять k, вызывать check или как-то иначе обращаться/менять  word
Ваш код в сумме не более 300 строк (переносы на 120 символах)
Нельзя обращаться к внешним файлам и сайтам из кода
Саша Мосин должен понять, что у вас написано. Иначе дисквалификация

