# __Лабораторная работа 4__

## __Изменения добавленные в новых версиях Python__

_Автор работы: Стецук Максим 2гр.1п.гр._

## __*Конструкция match-case*__ ##
В Python 3.10 появился оператор выбора _match case_.

_Основное назначение:_ заменяет повторяющиеся операторы if-else компактной структурой сравнения с шаблоном.

### Общая структура ###

```python
match subject:
    case <pattern_1>:
        <action_1>
    case <pattern_2>:
        <action_2>
    case <pattern_3>:
        <action_3>
    case _:
        <action_4>
```

### В выражениях match-case можно использовать различные типы шаблонов ### 
Наиболее распространённые:  
- Шаблон литерал (literal);
- Шаблон захвата (capture);
- Шаблон подстановки (wildcard);
- Шаблон последовательностей (sequence).

### Примеры структур для каждого шаблона ###  

__*Шаблон литерал*__ (оператор работает с литеральными объектами, такими, как числа, строки, значение None и логическими значениями True/False).

Сравнивает исходный предмет с некоторым литеральным объектом (классическое сравнение на соответствие).

Структура:
```python
subject = object

match subject:
    case literal_object1:
        <action_1>
    case literal_object2:
        <action_2>
    case literal_object3:
        <action_3>
```
Пример использования шаблона находится в файле _literal.py_  
Для запуска ввести:
```shell
python literal.py
```

__*Шаблон захвата*__ (удобнее всего применять в структуре некоторой функции, в которую передаётся некоторое значение или None)

Внутри функции выражение match case выполнит сравнение захваченного значения с None. В случае равенства выполнится некоторое действие, а в случае неравенства захваченное значение будет передано в переменную.

Структура:
```python
def func(obj=...):
    match obj:
        case None:
            <action_1>
        case some_obj:
            <action_2>
```
Пример использования шаблона находится в файле _capture.py_  
Для запуска ввести:
```shell
python capture.py
```

__*Шаблон подстановки*__ (отличается от остальных шаблонов тем, что применяется знак подстановки '_')

Производит сопоставление без привязки к конкретному значению.  
В некоторых случаях данный шаблон можно сравнить с обычным else.

Структура:
```python
match subject:
    case object1:
        <action_1>
    case object2:
        <action_2
    case _:
        <action_3>
```
Пример использования шаблона находится в файле _wildcard.py_  
Для запуска ввести:
```shell
python wildcard.py
```

__*Шаблон последовательностей*__ (используются распакованные элементы различных последовательностей(коллекций))

Простыми словами, распаковывает элементы послеовательности в некоторые переменные и производит некоторую операцию в зависимости от количества полученных элементов или заданного условия.

Структура:
```python
some_collection = (...)

match some_collecton:
    case a1:
        <action_1>
    case a1, a2:
        <action_2
    case a1, a2, a3:
        <action_3>
    case _:
        <action_4>
```
Пример использования шаблона находится в файле _sequence.py_  
Для запуска ввести:
```shell
python sequence.py
```

### Комбинирование шаблонов ### 
В конструкции match-case можно сравнивать сразу несколько шаблонов.  
Для этого используется логический оператор | (или). Таким образом проверяется, соответствует ли хотя бы один шаблон заданному значению.

Структура:
```python
match subject:
    case <pattern_1> | <pattern_2>:
        <action_1>
    case <pattern_3>:
        <action_2>
    case _:
        <action_3>
```

Также, для задания переменной удовлетворяющего условия для выполнения некоторого шаблона используется оператор 'as'.

Структура:
```python
match subject:
    case <pattern_1> | <pattern_2> as some_object:
        <action_1>
    case <pattern_3>:
        <action_2>
    case _:
        <action_3>
```
Более понятно данный оператор будет рассмотрен в _интересных примерах_.

### Интересные примеры ###
__*Пример 1*__  
Программа на вход принимает строку вида: day-mon-year-plan, а затем преобразует её. При ошибочном вводе информирует об этом.

__Для проверки можно использовать:__ 22-11-2023-пойти на концерт

Код находится в файле _interesting1.py_  
Для запуска ввести:
```shell
python interesting1.py
```

__*Пример 2*__

Работа с классами объектов с помощью конструкции match-case и проверке параметра объекта класса на соответствие значения через 'as'.  

Кратко о программе: Создан класс студенты, с некоторыми свойствами, в том числе и свойством _mark_ по которому ведётся проверка на то, сдал, не сдал или получил шанс на аппеляцию конкретный студент и выводится соответствующее сообщение.

Код находится в файле _interesting2.py_  
Для запуска ввести:
```shell
python interesting2.py
```

## __*Класс Counter()*__ ##  
Добавлен в Python 3.10. Содержится в модуле _collections_.

Класс __Counter()__ модуля __collections__ - это подкласс словаря dict для подсчета хеш-объектов (неизменяемых, таких как строки, числа, кортежи и т.д.).

Синтаксис:
```Python
from collections import Counter

cnt = Counter([iterable-or-mapping])
```
(iterable-or-mapping - итерируемая последовательность или словарь.)  
Возвращаемое значение: __объект__.

### Атрибуты и методы: ###
- Counter.elements()
- Counter.most_common()
- Counter.subtract()
- Counter.total()
- Counter.update()

### 1) Counter.elements()  ###  
Возвращает итератор по элементам, в котором каждый элемент повторяется столько раз, во сколько установлено его значение. Элементы возвращаются в порядке их появления. Если количество элементов меньше единицы, то метод Counter.elements() просто проигнорирует его.

```Python
from collections import Counter

count = Counter(x=7, y=5, z=3)
count.elements()
```

Рабочий код находится в файле count.elements.py  
Запуск через Shell:
```Shell
python count.elements.py
```

### 2) Counter.most_common([n])  ###  
Возвращает список из n наиболее распространенных элементов и их количество от наиболее распространенных до наименее. Если n опущено или None, метод cnt.most_common() возвращает все элементы в счетчике.
```Python
from collections import Counter

count = Counter('What Amazing Text i wrote in the past! It was so nice, that i forgot them:)')
count.most_common(n)
```

Рабочий код находится в файле m_com.py  
Запуск через Shell:
```Shell
python m_com.py
```

### 3) Counter.subtract([iterable-or-mapping])  ###  
Вычитает элементы текущего счетчика count и итерируемой последовательности или другого словаря или другого счетчика Counter(). Подобно методу словаря dict.update(), но вычитает количество (значения ключей), а не заменяет их.
```Python
from collections import Counter

count1 = Counter(x=7, y=5, z=3)
count2 = Counter(x=3, y=2, z=1)
count1.subtract(count2)
```
Рабочий код находится в файле sub.py  
Запуск через Shell:
```Shell
python sub.py
```

### 4) Counter.total()  ###  
Вычисляет сумму значений текущего счетчика.
```Python
from collections import Counter

count = Counter(x=7, y=5, z=3)
count.total()
```
Рабочий код находится в файле total.py  
Запуск через Shell:
```Shell
python total.py
```

### 5) Counter.update([iterable-or-mapping])  ###  
Cкладывает элементы текущего счетчика count и итерируемой последовательности или другого словаря или другого счетчика Counter(). Работает подобно методу словаря dict.update(), но складывает количество (значения ключей), а не заменяет их.
```Python
from collections import Counter

count1 = Counter(x=7, y=5, z=3)
count2 = Counter(x=3, y=2, z=1, t=2)
count1.update(count2)
```
Рабочий код находится в файле upd.py  
Запуск через Shell:
```Shell
python upd.py
```

__*!Для объектов collections.Counter() доступны обычные методы словарей!*__

### Минимальные ограничения типа Counter() ###  
- Значения ключей предназначены для чисел, представляющих счетчики, однако в случае с Counter() в них можно хранить всё что угодно;
- Для работы методов словарей, значения ключей должны иметь соответствующие типы, иными словами, значение должно поддерживать соответсвующий метод;
- Мультимножественные методы предназначены только для случаев использования с положительными значениями. Входные значения ключей могут быть отрицательными или нулевыми, но в результате операций сохраняются только положительные значения;
- Метод Counter.elements() работает только с положительными целыми числами и будет игнорировать ноль и отрицательные значения;

### _Пример использования Counter() для подсчёта наиболее часто встречающихся слов в тексте_ ###  
Программа считывает файл text.txt, а затем с помощью метода most_common получает список наиболее частых слов в файле и их количество.

Рабочий код находится в файле read_count.py  
Запуск через Shell:
```Shell
python read_count.py
```

## __*Конструкция DataClass*__ ##  
Добавлен в Python 3.7. Содержится в модуле _dataclasses_.

Модуль dataclasses предоставляет декоратор и функции для автоматического добавления сгенерированных специальных методов, таких как __init__() и __repr__() , в определяемые пользователем классы.

Базовая конструкция (пример класса пользователь):
```python
from dataclasses import dataclass

@dataclass
class Person:
    fName: str
    sName: str
    PhoneNumber: str
```

### Задание значений по умолчанию ###  
Структура:
```python
from dataclasses import dataclass

@dataclass
class Person:
    fName: str
    sName: str
    Year: int = 2023

Maks = Person('Maks', 'Tulenchik')
```
Рабочий код находится в файле defaultVal.py  
Запуск через Shell:
```Shell
python defaultVal.py
```
### Изменение значений полей ###
__Изменяемая структура:__
```python
from dataclasses import dataclass

@dataclass
class Person:
    fName: str
    sName: str
    Year: int = 2023

Maks = Person('Maks', 'Tulenchik')
Maks.fName = 'Maksim'
```
Имя будет изменено без возникновения исключений.

Рабочий код находится в файле changeable.py  
Запуск через Shell:
```Shell
python changeable.py
```

__НЕ изменяемая структура:__  
Параметр _Frozen_
```python
from dataclasses import dataclass

@dataclass(frozen = True)
class Person:
    fName: str
    sName: str
    Year: int = 2023

Maks = Person('Maks', 'Tulenchik')
Maks.fName = 'Maksim'
```
Вернётся исключение _dataclasses.FrozenInstanceError_

Рабочий код находится в файле not_changeable.py  
Запуск через Shell:
```Shell
python not_changeable.py
```

### Сравнение DataClasses ###
Параметр _Order_

Простейшая конструкция:
```python
from dataclasses import dataclass

@dataclass(order = True)
class Person:
    age: int
    fName: str
    sName: str
```
Сравнение происходит по порядку.

Рабочий код находится в файле comparison.py  
Запуск через Shell:
```Shell
python comparison.py
```

### Наследование в DataClasses ###
Простейшая конструкция наследования:
```python
from dataclasses import dataclass

@dataclass
class Person:
    fName: str
    sName: str

@dataclass
class Worker(Person):
    sallary: float
```

Рабочий код находится в файле inheritance.py  
Запуск через Shell:
```Shell
python inheritance.py
```

### Реализация ранее продемонстрированного примера с классами и match-case конструкцией через DataClasses ###
Работа с классами объектов с помощью конструкции match-case и проверке параметра объекта класса на соответствие значения через 'as'.  

Кратко о программе: Создан класс студенты, с некоторыми свойствами, в том числе и свойством _mark_ по которому ведётся проверка на то, сдал, не сдал или получил шанс на аппеляцию конкретный студент и выводится соответствующее сообщение.

Код находится в файле _interesting2_dc_remake.py_  
Для запуска ввести:
```shell
python interesting2_dc_remake.py
```