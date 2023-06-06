INSERT INTO `lr7_games`.`game` (`title`, `manufacturer`, `min_players`, `max_players`, `min_age`) VALUES ('Диксит', 'Libellud', '3', '6', '8');
INSERT INTO `lr7_games`.`game` (`title`, `manufacturer`, `min_players`, `max_players`, `min_age`) VALUES ('Диксит', 'Asmodee', '3', '6', '12');
INSERT INTO `lr7_games`.`game` (`title`, `manufacturer`, `min_players`, `max_players`) VALUES ('Монополия', 'Hasbro Inc', '2', '6');
INSERT INTO `lr7_games`.`game` (`title`, `manufacturer`, `min_players`, `max_players`, `min_age`) VALUES ('Jungle', 'Asmodee', '2', '4', '9');

INSERT INTO `lr7_games`.`clients` (`id_client`, `surname`, `name`, `phone_number`, `mail`) VALUES ('K1', 'Петров', 'Петр', '8-962-587-33-01', 'arpet@mail.ru');
INSERT INTO `lr7_games`.`clients` (`id_client`, `surname`, `name`, `date_of_birth`, `mail`, `address`) VALUES ('K2', 'Швыркин', 'Василий', '1988-09-10', 'vasvas@gmail.com', 'ул. Пионерская, 26-58');

INSERT INTO `lr7_games`.`employees` (`service_number`, `surname`, `name`) VALUES ('C01', 'Жуков', 'Дмитрий');
INSERT INTO `lr7_games`.`employees` (`service_number`, `surname`, `name`) VALUES ('C02', 'Васичкин', 'Сергей');

INSERT INTO `lr7_games`.`orders` (`method_of_obtaining`, `created`, `client`, `employee`) VALUES ('Самовывоз', '2017-09-12 16:12', 'K1', 'C01');
INSERT INTO `lr7_games`.`orders` (`method_of_obtaining`, `created`, `client`, `employee`) VALUES ('Самовывоз', '2017-09-12 16:14', 'K2', 'C01');
INSERT INTO `lr7_games`.`orders` (`method_of_obtaining`, `created`, `client`, `employee`) VALUES ('Доставка', '2017-09-13 10:09', 'K1', 'C02');

INSERT INTO `lr7_games`.`filling` (`order_number`, `game_title`, `game_manufacturer`, `amount`) VALUES ('1', 'Диксит', 'Libellud', '1');
INSERT INTO `lr7_games`.`filling` (`order_number`, `game_title`, `game_manufacturer`, `amount`) VALUES ('1', 'Монополия', 'Hasbro Inc', '2');
INSERT INTO `lr7_games`.`filling` (`order_number`, `game_title`, `game_manufacturer`, `amount`) VALUES ('2', 'Монополия', 'Hasbro Inc', '4');
INSERT INTO `lr7_games`.`filling` (`order_number`, `game_title`, `game_manufacturer`, `amount`) VALUES ('3', 'Диксит', 'Asmodee', '1');
INSERT INTO `lr7_games`.`filling` (`order_number`, `game_title`, `game_manufacturer`, `amount`) VALUES ('3', 'Jungle', 'Asmodee', '1');
