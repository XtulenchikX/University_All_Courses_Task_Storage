# Лабораторная работа 9

### Автор: Стецук Максим ИВТ 3 курс

1. Файлы реализованного в ходе выполнения лабораторной работы проекта расположены в каталоге _Project_

2. Развертывание реализованного проекта:

- [Ссылка на образ в DockerHub](https://hub.docker.com/r/makstulenchik/fastapi_project)
- [Ссылка на скринкаст с демонстрацией BPR](https://disk.yandex.ru/i/MNCAv3CNTD6FCQ)

_BPR - Build, Push, RUN_  
_Скринкаст стоит смотреть на ускорении x1.5_

---

#### Последовательность действий (использованные команды):

1. Открыть терминал и перейти в каталог проекта
2. Создать образ:
   ```Shell
   docker build -t makstulenchik/fastapi_project:0.0.1 .
   ```
3. Авторизоваться в Docker (eсли ранее это не было сделано):
   ```Shell
   docker login
   ```
4. Запушить образ в DockerHub:
   ```Shell
   docker push makstulenchik/fastapi_project:0.0.1
   ```
5. Запустить контейнер (если нет локального образа, то он будет взят с DockerHub):
   ```Shell
   docker run -p 80:80 makstulenchik/fastapi_project:0.0.1
   ```
