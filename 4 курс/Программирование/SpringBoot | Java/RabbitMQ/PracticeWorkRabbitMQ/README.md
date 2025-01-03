# Practice work | RabbitMQ

#### _Автор: Стецук Максим 1гр.2п.гр._

> _В файле `RabbitMQAppTest` представлена конфигурация для `Bruno`, которая использовалась при тестировании_

---

### Пример успешного запуска приложения через IntelliJ IDEA
![Пример успешного запуска прилоожения через IntelliJ IDEA](images/01.png)

### Пример успешной отправки ссобщения через `ProducerController`
> Отправка через Bruno

![Отправка через Bruno](images/02.png)

> Успешный вывод в консоль

![Успешный вывод в консоль](images/03.png)

### Пример сообщения через `PublisherController`
> Отправка через Bruno, без `routingKey`

![Отправка через Bruno, без routingKey](images/04.png)

> Успешный вывод в консоль

![Успешный вывод в консоль](images/05.png)

> Отправка через Bruno, с `routingKey = info`

![Отправка через Bruno, с routingKey = info](images/06.png)

> Успешный вывод в консоль

![Успешный вывод в консоль](images/07.png)

### Пример отправки с оставшимися ключами маршрутизации
> Отправка через Bruno, с `routingKey = error`

![Отправка через Bruno, с routingKey = error](images/08.png)

> Отправка через Bruno, с `routingKey = warning`

![Отправка через Bruno, с routingKey = warning](images/09.png)

> Успешный вывод в консоль
![Успешный вывод в консоль](images/10.png)
