
# Структуры данных

**План занятия**

1. Списки (list)
2. Словари (dict)
3. Кортежи (tuple)
4. Множества (set)
5. defaultdict
6. Counter

## Зачем?

Структуры данных - это база питона, потому что невозможно просто хранить значения переменных в виде строки или числа, нужно как-то организовать их наборы. Выбор правильной структуры данных дает больше возможностей для использования и повышает скорость работы программы, что важно для работы с большими объемами данных

## Списки

Список, или массив (list) -- это такая структура данных, где все элементы имеют порядковый номер (индекс), по которому их можно вызвать. Элементы могут повторяться (т.е. в ячейках с разными индексами могут быть записаны переменные с одинаковым значением / одинаковые константы). В списке могут храниться данные разных типов. Записывается в [ ].


```python
a = 5
b = "hello"

some_list = [4.89, a, "spam", True, "spam", b]
print(some_list)
```

    [4.89, 5, 'spam', True, 'spam', 'hello']
    


```python
sentence = "Из этого предложения получится список"
letters = list(sentence)  # разбивает строку на минимальные элементы, т.е. посимвольно
words = sentence.split() # разбивает строку на слова по пробелам

print(words)
print(letters)
```

    ['Из', 'этого', 'предложения', 'получится', 'список']
    ['И', 'з', ' ', 'э', 'т', 'о', 'г', 'о', ' ', 'п', 'р', 'е', 'д', 'л', 'о', 'ж', 'е', 'н', 'и', 'я', ' ', 'п', 'о', 'л', 'у', 'ч', 'и', 'т', 'с', 'я', ' ', 'с', 'п', 'и', 'с', 'о', 'к']
    

К элементам массива можно обращаться как по ключу от 0 до длины - 1, так и по отрицательному ключу, где -1 - это последний элемент, -2 - предпоследний и так далее


```python
a = ['first', 'second', 'third']
print(a[0])
print(a[-1])
print(a[-2])
```

    first
    third
    second
    

list() принимает на вход только один аргумент. Этот аргумент должен быть итерируемым (по нему можно пройти циклом for, например, строка). Из числа сделать список не получится


```python
numbers = list(123)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-47-11a0477006f6> in <module>
    ----> 1 numbers = list(123)
    

    TypeError: 'int' object is not iterable


Список может быть пустым


```python
new_list = []
print(new_list)
```

    []
    

В списке может лежать список или любой другой объект


```python
a = [[3, 4, 5], [6, 7, 8], {1, 2, 3}]
a[0] = 5
print(a)
```

    [5, [6, 7, 8], {1, 2, 3}]
    

Но! Надо быть аккуратными, потому что бывает так:


```python
a = [1, 2, 3]
b = [a, 1, 5, 6]
print(b)
a[0] = 9
print(b)
a = [20, 10, 11]
print(b)
```

    [[1, 2, 3], 1, 5, 6]
    [[9, 2, 3], 1, 5, 6]
    [[9, 2, 3], 1, 5, 6]
    

**Основные методы и операции с list**

1. \+ : простое сложение
2. append : добавить элемент в конец
3. extend : расширить список (то же, что и +)


```python
a = [1, 2, 3]
a.append(5)
print(a)
a.append([6,7,8])
print(a)
```

    [1, 2, 3, 5]
    [1, 2, 3, 5, [6, 7, 8]]
    

Сложение можно записать разными способами


```python
a = [1, 2, 3]
a.extend([7, 8, 9])
print(a)

a = [1, 2, 3]
a = a + [7, 8, 9]
print(a)

a = [1, 2, 3]
a += [7, 8, 9]
print(a)
```

    [1, 2, 3, 7, 8, 9]
    [1, 2, 3, 7, 8, 9]
    [1, 2, 3, 7, 8, 9]
    

Можно удалить элемент по ключу


```python
a = ['this', 'is', 'some', 'list']
del a[2]
print(a)
```

    ['this', 'is', 'list']
    

Срез - это копия части массива. Параметры задаются в квадратных скобках после имени списка


```python
a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(a[4:])  # элементы, начиная с индекса 4
print(a[:6])  # элементы, до индекса 6 (не включительно)
print(a[4:6])  # элементы, с индекса 4 по 6 (не включительно)
print(a[2:8:2])  # элементы, с индекса 2 по 8 (не включительно) с шагом 2
print(a[8:2:-1])  # элементы, с индекса 2 (не включительно) по 8 (включительно) с шагом -1 (в обратном порядке)
print(a[::-1])  # элементы в обратном порядке
```

    [50, 60, 70, 80, 90, 100]
    [10, 20, 30, 40, 50, 60]
    [50, 60]
    [30, 50, 70]
    [90, 80, 70, 60, 50, 40]
    [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    

List comprehensions - как еще можно создавать списки:


```python
# напоминание a = ['this', 'is', 'list']
new_a = [x for x in a if x.endswith("is")]
new_a
```




    ['this', 'is']




```python
odds = [x for x in range(10) if x%2 == 1]
odds
```




    [1, 3, 5, 7, 9]



## Кортежи

Кортеж (tuple) - это тип неизменяемых данных, если элемент списка можно поменять, то у tuple такой возможности нет


```python
# пустой кортеж
new_tuple = ()
print(new_tuple)

# непустой кортеж
siblings = ('brother', 'sister')
print(siblings)

# кортеж из списка
words = tuple(words)
print(words)

# кортеж из строки
letters = tuple(sentence) # строка разбивается на минимальные единицы, т.е. посимвольно
print(letters)
```

    ()
    ('brother', 'sister')
    ('Из', 'этого', 'предложения', 'получится', 'список')
    ('И', 'з', ' ', 'э', 'т', 'о', 'г', 'о', ' ', 'п', 'р', 'е', 'д', 'л', 'о', 'ж', 'е', 'н', 'и', 'я', ' ', 'п', 'о', 'л', 'у', 'ч', 'и', 'т', 'с', 'я', ' ', 'с', 'п', 'и', 'с', 'о', 'к')
    


```python
words += siblings # прибавляем siblings к words и записываем результат в words
print(words)

big_family = siblings * 3
print(big_family)
```

    ('Из', 'этого', 'предложения', 'получится', 'список', 'brother', 'sister')
    ('brother', 'sister', 'brother', 'sister', 'brother', 'sister')
    


```python
print(words[0])   # первый элемент кортежа
print(words[-1])  # последний элемент кортежа
print(words[2:5]) # элементы кортежа со 2 по 5 (включая 2 и не включая 5)
```

    Из
    sister
    ('предложения', 'получится', 'список')
    

## Словари (повторение)

Словари - это структура данных, где есть ключи - уникальные идендитикаторы и значения - соответствующие им объекты.


```python
# пустой словарь
d = dict()
print(d)

# пустой словарь
d = {}
print(d)
```

    {}
    {}
    


```python
# словарь со значениями
d = {'a': 2}
print(d)

# словарь со значениями из списка кортежей ключ-значение
d = dict([('a', 2)])
print(d)
```

    {'a': 2}
    {'a': 2}
    


```python
# словарь из заданных ключей, где у каждого значение None
d = dict.fromkeys(['a', 'b', 'c'])
print(d)

# словарь из заданных ключей, где каждому дается в соответствие какое-то одно дефолтное значение
d = dict.fromkeys(['a', 'b', 'c'], 2)
print(d)
```

    {'a': None, 'b': None, 'c': None}
    {'a': 2, 'b': 2, 'c': 2}
    


```python
# ключи
print(d.keys())

# значения
print(d.values())

# пары ключ-значение
print(d.items())
```

    dict_keys(['a', 'b', 'c'])
    dict_values([2, 2, 2])
    dict_items([('a', 2), ('b', 2), ('c', 2)])
    

Если мы не знаем, есть ключ или нет, но не хотим ошибку KeyError, мы можем брать значения по-другому, получая ничего (None) без ошибки. Для этого используется метод get


```python
d = {1: 90, 2: 89, 3: 54}
d[7]
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-48-723e14a698a7> in <module>
          1 d = {1: 90, 2: 89, 3: 54}
    ----> 2 d[7]
    

    KeyError: 7



```python
d = {1: 90, 2: 89, 3: 54}
print(d.get(7))
```

    None
    

## Множества

Множество (set) - это структура данных, чем-то похожая и на массив, и на словарь, но от них отличающаяся.

Как и массивы, множества содержат элементы. Но в отличие от массивов, где элементы упорядочены, в множестве они идут в "произвольном" порядке.

На словари множества похожи тем, что, как и ключи в словарях, элементы множеств неупорядочены и поэтому должны быть уникальны.

Поиск в множестве происходит быстрее, чем в массиве, потому что в массивы мы проходим каждый элемент с 1 до последнего или искомого, а во множестве другой, более быстрый алгоритм. Если вам нужно собрать какие-то данные, а потом проверять, есть ли в этих данных что-то, то целесообразно использовать именно множества. Во-вторых, преобразование в множества помогают быстро превратить набор данных в набор уникальных элементов.


```python
# создаем множество из списка (массива)

sentence = "the cat is on the mat"
words = set(sentence.split())  # превращаем список, который возвращает split(), в массив
animals = set(['cat', 'dog', 'elephant', 'crocodile', 'fox', 'cat', 'elephant'])

print(words)
print(animals)
```

    {'mat', 'the', 'is', 'cat', 'on'}
    {'fox', 'crocodile', 'elephant', 'cat', 'dog'}
    


```python
# создаем множество из строки

letters = set(sentence)  # разбивает строку на минимальные элементы, т.е. посимвольно
print(letters)
```

    {'n', 'c', 'o', 'h', 'a', 's', 't', 'm', 'e', ' ', 'i'}
    

Обратите внимание, что все элементы получившихся множеств уникальны! Если вам не нужно знать, сколько раз встречаются объекты и в каком порядке, можно использовать множество.

Множества нельзя складывать, зато можно добавлять в них элементы -- это делается функцией add(), которая тоже пишется через точку после названия множества.


```python
animals.add('tiger')
print(animals)
```

    {'tiger', 'fox', 'crocodile', 'elephant', 'cat', 'dog'}
    


```python
a = {}
type(a)
```




    dict




```python
# пустое множество
new_set = set() # обратите внимание, что просто скобочек в данном случае недостаточно!
print(new_set)
```

    set()
    


```python
a = set([1, 2, 3, 4, 5, 6])
b = set([4, 5, 6, 7, 8, 9])

# объединение
c = a | b
print(c)

# пересечение
c = a & b
print(c)

# разность
c = a - b
print(c)

# симметрическая разность, то есть элементы, входящие в a или в b, но не в оба множества одновременно
c = a ^ b
print(c)
```

    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    {4, 5, 6}
    {1, 2, 3}
    {1, 2, 3, 7, 8, 9}
    

## Основные функции

1. sum - сумма элементов
2. len - длина (или количество элементов)
3. sorted - сортировка
4. enumerate - проход с нумерацией


```python
a = [1, 2, 3, 4, 5]
print(len(a))
print(sum(a))
```

    5
    15
    


```python
a = set([1, 2, 3, 4, 5])
print(len(a))
print(sum(a))
```

    5
    15
    


```python
a = dict.fromkeys([1, 2, 3, 4, 5], 10)
print(a)
print(len(a))
print(sum(a)) # сумма ключей
```

    {1: 10, 2: 10, 3: 10, 4: 10, 5: 10}
    5
    15
    


```python
a = dict.fromkeys(['1', '2', '3'], 10)
print(a)
print(len(a))
print(sum(a)) # сумма ключей - здесь ошибка, потому что нельзя сложить строки математически
```

    {'1': 10, '2': 10, '3': 10}
    3
    


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-46-b9daaeaaeea2> in <module>
          2 print(a)
          3 print(len(a))
    ----> 4 print(sum(a)) # сумма ключей - здесь ошибка, потому что нельзя сложить строки математически
    

    TypeError: unsupported operand type(s) for +: 'int' and 'str'



```python
a = {1: 90, -2: 45, 3: 500, -5: 800, 0: 900}

for key in sorted(a):
    print(key, a[key])
```

    -5 800
    -2 45
    0 900
    1 90
    3 500
    


```python
for key in sorted(a, reverse=True):
    print(key, a[key])
```

    3 500
    1 90
    0 900
    -2 45
    -5 800
    


```python
# сортировка по значениям
for key in sorted(a, key=a.get):
    print(key, a[key])
```

    -2 45
    1 90
    3 500
    -5 800
    0 900
    


```python
# сортировка по квадрату ключа
for key in sorted(a, key=lambda x: x**2, reverse=True):
    print(key, a[key])
```

    -5 800
    3 500
    -2 45
    1 90
    0 900
    

Enumerate возвращает номер элемента по порядку и сам элемент, это бывает полезно, когда нужно делать что-то сложно с объектом или есть другой объект, к которому мы адресуемся


```python
a = [900, 45, 67, 23, 1]
for key, value in enumerate(a):
    print(key, value)
```

    0 900
    1 45
    2 67
    3 23
    4 1
    


```python
a = [900, 45, 67, 23, 1]
b = [234, 436, 123, 657, 31]
for key, value in enumerate(a):
    print(value, b[key])
```

    900 234
    45 436
    67 123
    23 657
    1 31
    

## defaultdict

Если мы составляем частотный словарь или что-то похожее, где есть начальное значение в словаре, но мы, опять же, не хотим получать ошибку KeyError, можно использовать структуру данных defaultdict, который если нет ключа, добавляет такой ключ и ставит в качестве значения некое дефолтное


```python
from collections import defaultdict
```


```python
d = defaultdict(int) # дефолт - 0
print(d)
print(d[9])
print(d)
```

    defaultdict(<class 'int'>, {})
    0
    defaultdict(<class 'int'>, {9: 0})
    

частотный словарь букв в строке


```python
d = defaultdict(int)
some_string = 'a little less conversation, a little more action'
for letter in some_string:
    d[letter] += 1
print(d)
```

    defaultdict(<class 'int'>, {'a': 4, ' ': 7, 'l': 5, 'i': 4, 't': 6, 'e': 5, 's': 3, 'c': 2, 'o': 4, 'n': 3, 'v': 1, 'r': 2, ',': 1, 'm': 1})
    

можно превратить такой словарь в обычный


```python
d = dict(d)
print(d)
```

    {'a': 4, ' ': 7, 'l': 5, 'i': 4, 't': 6, 'e': 5, 's': 3, 'c': 2, 'o': 4, 'n': 3, 'v': 1, 'r': 2, ',': 1, 'm': 1}
    

можно задавать другой тип дефотного значения, например, список

в примере - словарь, где слова группируются по длине


```python
d = defaultdict(list)
some_string = 'a little less conversation, a little more action'
for word in some_string.split():
    d[len(word)].append(word)
d = dict(d)
print(d)
```

    {1: ['a', 'a'], 6: ['little', 'little', 'action'], 4: ['less', 'more'], 13: ['conversation,']}
    

## Counter

Counter итерируется (проходит) по списку или другому объекту и считает количество элементов, сохраняя все в словарь вида ключ - количество


```python
from collections import Counter
```


```python
some_string = 'a little less conversation, a little more action'

Counter(some_string)
```




    Counter({'a': 4,
             ' ': 7,
             'l': 5,
             'i': 4,
             't': 6,
             'e': 5,
             's': 3,
             'c': 2,
             'o': 4,
             'n': 3,
             'v': 1,
             'r': 2,
             ',': 1,
             'm': 1})




```python
some_string = 'a little less conversation, a little more action'

Counter(some_string.split())
```




    Counter({'a': 2,
             'little': 2,
             'less': 1,
             'conversation,': 1,
             'more': 1,
             'action': 1})



Counter можно складывать или обновлять (добавлять элементы)


```python
lyrics = [
    'a little less conversation, a little more action',
    'a little more bite and a little less bark',
    'a little less fight and a little more spark'
]
c = Counter()
print(c)

for line in lyrics:
    c += Counter(line.split())
print(c)
```

    Counter()
    Counter({'a': 6, 'little': 6, 'less': 3, 'more': 3, 'and': 2, 'conversation,': 1, 'action': 1, 'bite': 1, 'bark': 1, 'fight': 1, 'spark': 1})
    

#### Упражнения на типы данных

1. Например, "the cat in the hat".title() ==> "The Cat In The Hat", а мы хотим "The Cat in the Hat" 


```python
def proper_title_case(s):
    nocaps = ["the", "in"] # This needs to be extended.
    #Your code goes below this comment
    return #here goes what you want the function to return
print(proper_title_case('An ant on a table'))#to test the function
print(proper_title_case('The Cat In the Hat'))#to test the function
```

2. Базовый csv парсер: парсирует длинную строку в список списков.


```python
myspreadsheet ="""Subject,Height,Occupation
1,74.37000326528938,Psychologist
2,67.49686206937491,Psychologist
3,74.92356434760966,Psychologist
4,64.62372198999978,Psychologist
5,67.76787900026083,Linguist
6,61.50397707923559,Psychologist
7,62.73680961908566,Psychologist
8,68.60803984763902,Linguist
9,70.16090500135535,Psychologist
10,76.81144438287173,Linguist"""

def csv_parser(s):
    """Parses the string s into lines, and then parses those lines by
    splitting on the comma and converting the numerical data to int.
    The output is a list of lists of subject data."""
    #Your code goes below this comment
    # Data is our output. It will be a list of lists.    

    # Split csv into lines and store them in a list called 'lines'.
    
    # Remove the first element from lines, so that you have only the data lines left.
    
    # At this stage, we loop through the list called lines.
    # As you loop
    #     i. split each line on the commas;
    #    ii. convert the Subject variable to int.
    #   iii. convert the Height variable to float.
    #    iv. add to data a list consisting of this line's Subject, Height, and Occupation values 
    
    return #here goes what you want the function to return
print(csv_parser(myspreadsheet))#to test your function
```

3. Дополните функцию, которая возвращает словарь, где профессия соотнесена с количеством раз она встречается в данных. На вход функция берёт результат применения csv_parser(myspreadsheet).


```python
def occupation_distribution(data):
    """Returns the list of occupations given in column 2 of data.
    data is the output of csv_parser(myspreadsheet)"""
    #Your code goes below this comment
    return #here goes what you want the function to return
print(occupation_distribution(myspreadsheet))#to test your function
```

Ответы:


```python
def proper_title_case(s):
    nocaps = ["the", "in", "on", "a", "an"] # This needs to be extended.
    #Your code goes below this comment
    s = s.title()
    words = s.split(" ")
    new_words = []
    for w in words:
        if w.lower() in nocaps:
            w = w.lower()
        new_words.append(w)
    y = " ".join(new_words)
    return y[0].upper() + y[1: ]
print(proper_title_case('An ant on a table'))#to test your function
print(proper_title_case('The Cat In the Hat'))#to test your function
```

    An Ant on a Table
    The Cat in the Hat
    


```python
myspreadsheet ="""Subject,Height,Occupation
1,74.37000326528938,Psychologist
2,67.49686206937491,Psychologist
3,74.92356434760966,Psychologist
4,64.62372198999978,Psychologist
5,67.76787900026083,Linguist
6,61.50397707923559,Psychologist
7,62.73680961908566,Psychologist
8,68.60803984763902,Linguist
9,70.16090500135535,Psychologist
10,76.81144438287173,Linguist"""

def csv_parser(s):
    """Parses the string s into lines, and then parses those lines by
    splitting on the comma and converting the numerical data to int.
    The output is a list of lists of subject data."""
    #Your code goes below this comment
    # Data is our output. It will be a list of lists.
    data = []    

    # Split csv into lines and store them in a list called 'lines'.
    lines = s.splitlines()
    
    # Remove the first element from lines, so that you have only the data lines left.
    lines = lines[1: ]
    
    # At this stage, we loop through the list called lines.
    # As you loop
    #     i. split each line on the commas;
    #    ii. convert the Subject variable to int.
    #   iii. convert the Height variable to float.
    #    iv. add to data a list consisting of this line's Subject, Height, and Occupation values 
    for line in lines:
        l = line.strip().split(",")
        l[0] = int(l[0])
        l[1] = float(l[1])
        data.append(l)
    return data
print(csv_parser(myspreadsheet))#to test your function
```

    [[1, 74.37000326528938, 'Psychologist'], [2, 67.49686206937491, 'Psychologist'], [3, 74.92356434760966, 'Psychologist'], [4, 64.62372198999978, 'Psychologist'], [5, 67.76787900026083, 'Linguist'], [6, 61.50397707923559, 'Psychologist'], [7, 62.73680961908566, 'Psychologist'], [8, 68.60803984763902, 'Linguist'], [9, 70.16090500135535, 'Psychologist'], [10, 76.81144438287173, 'Linguist']]
    


```python
def occupation_distribution(data):
    """Returns the list of occupations given in column 2 of data.
    data is the output of csv_parser(myspreadsheet)"""
    #Your code goes below this comment
    p = csv_parser(data)
    t = tuple(x[2] for x in p)
    occupation_dictionary = {"Linguist" : t.count("Linguist"), "Psychologist" : t.count("Psychologist")}
    return occupation_dictionary
print(occupation_distribution(myspreadsheet))#to test your function
```

    {'Linguist': 3, 'Psychologist': 7}
    
