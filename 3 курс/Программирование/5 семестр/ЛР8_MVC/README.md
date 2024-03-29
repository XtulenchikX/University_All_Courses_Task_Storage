# Лабораторная работа 8

__Автор:__ Стецук Максим ИВТ 3 курс

### В данной лабораторной работе был реализован следующий функционал:
1. Создан собственный модуль _stecuk.py_ по аналогии с _zhukov.py_.
2. Реализован собственнный класс _UserStecuk_ по аналогии с _UserZhukov_, который наследует методы User, реализованы два новых метода для класса _UserStecuk_:
   - __get_b_date__: получает дату рождения;
   - __get_f_lan__: получает название любимого языка программирования.
3. Реализован шаблон _extended_layout.html_, который наследует базовый шаблон layout.html и дописывает в него информацию из пункта 2.
4. Внутри пакета _app_lr8_ создан пакет _controllers_, в котором реализован контроллер _StoreUserController_, который формирует не html, а json.

### Добавленные маршруты:
- [/](https://lr8mvc.tulenchik.repl.co/) : по данному маршруту возвращается шаблон _extended_layout.html_, с записанной из модуля _stecuk.py_ информацией.
- [/zhukov](https://lr8mvc.tulenchik.repl.co/zhukov) :  по данному маршруту возвращается шаблон _layout.html_, с записанной из модуля _zhukov.py_ информацией.
- [/jsonSM](https://lr8mvc.tulenchik.repl.co/jsonSM) : по данному маршруту возвращается __json__ с информацией из модуля _stecuk.py_.
- [/jsonZN](https://lr8mvc.tulenchik.repl.co/jsonZN) : по данному маршруту возвращается __json__ с информацией из модуля _zhukov.py_.
- По остальным маршрутам возвращается шаблон-заглушка _plug_layout.html_.