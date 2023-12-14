# Лабораторная работа 2
## Реализация удаленного импорта

__Автор:__ Стецук Максим ИВТ 3 курс

### Видео с демонстрацией удалённого импорта:  
*В записях демонстрируются удалённый импорт модуля __myremotemodule.py__ c локального хоста и с хоста Replit*  
- [Локальный сервер](https://disk.yandex.ru/i/lw3z5Hd1T9L8eA)
- [Replit сервер](https://disk.yandex.ru/i/ozX8w0s1ZTjB9Q)

### Скриншоты с демонстрацией удалённого импорта LocalHost
![](/Screenshots/Local1.png)
Запустил сервер, а в другом проекте файл со скриптом:
![](/Screenshots/Local2.png)
Добавил путь в sys.path (LocalHost) и проверил что он добавился:
![](/Screenshots/Local3.png)
Импортировал модуль *myremoutemodule.py* и запустил функцию из неё (сразу после импорта в консоли проекта, в котором запущен сервер, появилась строка с информацией об успешном get запросе):
![](/Screenshots/Local4.png)

### Скриншоты с демонстрацией удалённого импорта с Replit
![](/Screenshots/Replit1.png)
Запустил сервер на Replit, а в локальном проекте файл со скриптом:
![](/Screenshots/Replit2.png)
Добавил путь в sys.path и проверил что он добавился:
![](/Screenshots/Replit3.png)
Импортировал модуль *myremoutemodule.py* и запустил функцию из неё (сразу после импорта в консоли Replit, где запущен сервер, появилась строка с информацией об успешном get запросе):
![](/Screenshots/Replit4.png)

## Код запускаемого скрипта (activation_script.py)
```Python
import re
import sys
from urllib.request import urlopen
from importlib.abc import PathEntryFinder
from importlib.util import spec_from_loader

class URLFinder(PathEntryFinder):
    def __init__(self, url, available):
        self.url = url
        self.available = available
        
    def find_spec(self, name, target=None):
        if name in self.available:
            origin = "{}/{}.py".format(self.url, name)
            loader = URLLoader()
            return spec_from_loader(name, loader, origin=origin)
        else:
            return None
        
def url_hook(some_str):  
    if not some_str.startswith(("http", "https")):
        raise ImportError
    with urlopen(some_str) as page:
        data = page.read().decode("utf-8")
    filenames = re.findall("[a-zA-Z_][a-zA-Z0-9_]*.py", data)
    modnames = {name[:-3] for name in filenames}
    return URLFinder(some_str, modnames)

sys.path_hooks.append(url_hook)
print(sys.path_hooks)

from urllib.request import urlopen

class URLLoader:
    def create_module(self, target):
        return None
    def exec_module(self, module):
        with urlopen(module.__spec__.origin) as page:
            source = page.read()
        code = compile(source, module.__spec__.origin, mode="exec")
        exec(code, module.__dict__)
```

## Cкрипт с использованием модуля _requests_ и обработкой исключения в ситуации, когда хост (где лежит модуль) недоступен
(Вместо __urllib__ в функциях: _url_hook_ и _exec_module_, используется __requests__)
```Python
import re
import requests
import sys
from importlib.abc import PathEntryFinder
from importlib.util import spec_from_loader

class URLFinder(PathEntryFinder):
    def __init__(self, url, available):
        self.url = url
        self.available = available
        
    def find_spec(self, name, target=None):
        if name in self.available:
            origin = "{}/{}.py".format(self.url, name)
            loader = URLLoader()
            return spec_from_loader(name, loader, origin=origin)
        else:
            return None
        
def url_hook(some_str):
    if not some_str.startswith(("http", "https")):
        raise ImportError
    try:
        response = requests.get(some_str)
    except Exception:
        print('Prodlems with path, check server address and his performance!')
    else:
        data = response.text
        filenames = re.findall("[a-zA-Z_][a-zA-Z0-9_]*.py", data)
        modnames = {name[:-3] for name in filenames}
        return URLFinder(some_str, modnames)

sys.path_hooks.append(url_hook)
print(sys.path_hooks)

class URLLoader:
    def create_module(self, target):
        return None

    def exec_module(self, module):
        response = requests.get(module.__spec__.origin)
        source = response.text
        code = compile(source, module.__spec__.origin, mode="exec")
        exec(code, module.__dict__)
```
[Видео с демонстрацией работы данного скрипта на локальном и на удалённом серверах](https://disk.yandex.ru/i/rv0vBW5mimHHbA)