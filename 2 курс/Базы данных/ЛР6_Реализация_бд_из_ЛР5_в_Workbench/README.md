# __Лабораторная работа 6__

## __Реализация БД из ЛР5 в Workbench__

_Автор работы: Стецук Максим 2гр.1п.гр._


1. Графическая схема представлена в файле __*Scheme.png*__
2. Запрос для создания представлен в файле __*DataBaseCreate.sql*__
3. Запросы добавления данных представлены ниже:
- Добавление данных в таблицу _manufacturer_
```sql
INSERT INTO `labwork6`.`manufacturer` (`Manufacturer_name`, `Web-site`) VALUES ('super_disks', 'super_disks.org');
INSERT INTO `labwork6`.`manufacturer` (`Manufacturer_name`, `Web-site`) VALUES ('disksForYou', 'disksFY.ru');
```
- Добавление данных в таблицу _model_
```sql
INSERT INTO `labwork6`.`model` (`Model_name`, `Manufacturer`, `Disk_size`, `Rotation_speed`, `Interface_type`) VALUES ('simple', 'super_disks', '128', '1000', 'common');
INSERT INTO `labwork6`.`model` (`Model_name`, `Manufacturer`, `Disk_size`, `Rotation_speed`, `Interface_type`) VALUES ('standard', 'super_disks', '512', '3000', 'normal');
INSERT INTO `labwork6`.`model` (`Model_name`, `Manufacturer`, `Disk_size`, `Rotation_speed`, `Interface_type`) VALUES ('model1', 'disksForYou', '256', '2000', 'standard');
INSERT INTO `labwork6`.`model` (`Model_name`, `Manufacturer`, `Disk_size`, `Rotation_speed`, `Interface_type`) VALUES ('model2', 'disksForYou', '1024', '4000', 'standard');
```
- Добавление данных в таблицу _disk_
```sql
INSERT INTO `labwork6`.`disk` (`Serial_Number`, `Model`, `Date_of_purchase`) VALUES ('123', 'simple', '2022-01-12');
INSERT INTO `labwork6`.`disk` (`Serial_Number`, `Model`, `Date_of_purchase`) VALUES ('234', 'simple', '2022-02-23');
INSERT INTO `labwork6`.`disk` (`Serial_Number`, `Model`, `Date_of_purchase`) VALUES ('137', 'standard', '2022-01-29');
INSERT INTO `labwork6`.`disk` (`Serial_Number`, `Model`, `Date_of_purchase`) VALUES ('179', 'model1', '2023-03-27');
INSERT INTO `labwork6`.`disk` (`Serial_Number`, `Model`, `Date_of_purchase`) VALUES ('181', 'model1', '2022-08-19');
INSERT INTO `labwork6`.`disk` (`Serial_Number`, `Model`, `Date_of_purchase`) VALUES ('138', 'model1', '2022-06-15');
INSERT INTO `labwork6`.`disk` (`Serial_Number`, `Model`, `Date_of_purchase`) VALUES ('172', 'model2', '2021-04-03');
```
4. [Ссылка на видео с демонстрацией целостности БД](https://disk.yandex.ru/i/qzLvVD9MHDvNsg)

В данном видео:
- продемонстрировано изменение названия производителя и названия модели, с каскадным изменением зависимых полей;
- продемонстрировано каскадное удаление строк из зависимых таблиц, при удалении ключевых полей из родительской таблицы.
