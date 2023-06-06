INSERT INTO `project`.`students` (`id_students`,`fio`,`date_of_birth`,`age`,`sex`,`documents`,`document_code`) VALUES 
('S001','Kargapolov Denis Andreevich','2005-04-07',18,'m','passport','4617539198'),
('S002','Stecuk Maxim Nikolaevich','2006-03-28',17,'m','passport','4617539199'),
('S003','Zuhir Amira Saidovna','2008-04-18',16,'f','passport','4617148828'),
('S004','Kruchkova Anastasia Sergeevna','2010-01-01',13,'f','svidetelstvo','1337666444'),
('S005','Volozhanin Vladik Kirillovich','2006-08-08',17,'m','passport','4618687310'),
('S006','Lotuga Danila Dapkunatevich','2008-05-13',16,'m','passport','1842003333'),
('S007','Klementiev Lesha Ibragimovich','2008-05-14',16,'m','passport','6667778880'),
('S008','Maximova Angelina Vyacheslavovna','2013-06-06',10,'f','svidetelstvo','8800228777'),
('S009','Sobchak Ksenia Anatolyevna','2013-07-08',10,'f','svidetelstvo','1234567890'),
('S010','Gorshok Grisha Grigoryev','2005-03-06',18,'m','passport','4718678123'),
('S011','Adushkina Katya Marzhelovna','2008-09-09',16,'f','passport','4819432030'),
('S012','Arogundade Zak Franclin','2010-09-04',13,'m','svidetelstvo','9757589056'),
('S013','Reichwald Benjamin Igrevich ','2009-08-03',14,'m','passport','8631598709'),
('S014','Tumor Yves Anatolievich','2006-10-10',17,'m','passport','1352867089'),
('S015','Miros Vlad Nikolaevich','2007-05-19',16,'m','passport','8213967513'),
('S016','Rudkovskiy Gnom Gnomich','2013-08-06',10,'m','svidetelstvo','3128891221'),
('S017','Pupkin Petr Vovochkin','2006-11-19',17,'m','passport','8689120767'),
('S018','Blinovskaya Elena Viktorovna','2008-06-15',16,'f','passport','6231877812'),
('S019','Dubrovina Arina Romanovna','2009-07-03',14,'f','passport','6132967126'),
('S020','Dubok Vasily Nikolaevich','2010-03-06',13,'m','svidetelstvo','8213697679');

INSERT INTO `project`.`parent` (`fio`, `students_id`, `phone_number`, `email`) VALUES 
('Stecuk Nikolay Kirillovuch', 'S002', '+78908097878', 'sergay@mail.ru'),
('Zuhir Said Saidovich', 'S003', '+78320751673', 'saidsaid@gmail.com'),
('Kruchkov Sergey Anatolievich', 'S004', '+76713248983', 'kruchkov@mail.ru'),
('Volozhanin Kiriill Vyacheslavovich', 'S005', '+73284727362', 'volozh@mail.ru'),
('Lotuga Dapkunayte lvovich', 'S006', '+72347286823', 'dabdab@gmail.com'),
('Klementyev Vyacheslav Igorevich', 'S007', '+74732734679', 'klimsanich@mail.ru'),
('Maximov Maxim Maximich', 'S008', '+77342622839', 'slaymyangel@mail.ru'),
('Sobchak Anatoly Andreevich', 'S009', '+72734629342', 'sobsob@mail.ru'),
('Gorshok Grigory Grigoryevich', 'S010', '+78324282389', 'pankihoy@mail.ru'),
('Adushkin Marzhela Nikolaevich', 'S011', '+73242868688', 'ayavdush@mail.ru'),
('Arogundade Franclin Ferdinand', 'S012', '+73847279469', 'notmymail@mail.ru'),
('Reichwal Igor Igorevich', 'S013', '+72364729879', 'reichreich@mail.ru'),
('Tumor Anoly Andreevich', 'S014', '+77126319796', 'tumooor@gmail.com'),
('Miros Vladlena Andreevna', 'S015', '+78347237696', 'ohimtired@mail.ru'),
('Rudkovskaya Yana Igorevna', 'S016', '+76429469293', 'yayanarudkovskaya@mail.ru'),
('Pupkina Marina Andreevna', 'S017', '+77237187679', 'pupkina1939@mail.ru'),
('Blinovskia Klim Sanich', 'S018', '+72376723480', 'blinblin@mail.ru'),
('Dubrovin Roman Antonovich', 'S019', '+76342274920', 'dubdub@mail.ru'),
('Dubok Nikolay Nikolayevich', 'S020', '+71732108798', 'dubokvdube@mail.ru');

INSERT INTO `project`.`employees` (`id_employees`, `fio`, `age`, `date_of_birth`, `sex`, `document`, `document_code`, `position`, `email`, `work_experience (months)`) VALUES 
('E001', 'Zhukov Nikolay Nikolaevich', '30', '1993-04-23', 'm', 'passport', '6847534578', 'teacher', 'VLIUZNN@mail.ru', '36'),
('E002', 'Margancova Katerina Ivanova', '20', '2003-07-15', 'f', 'passport', '6213261873', 'teacher', 'hikate@mail.ru', '10'),
('E003', 'Svetlov Igor Vladimirovich', '30', '1993-08-16', 'm', 'passport', '8327261769', 'teacher', 'svetlov@mail.ru', '43'),
('E004', 'Vlasov Dmitry Antonovich', '35', '1988-09-03', 'm', 'passport', '8213797989', 'teacher', 'vlasovzz@mail.ru', '53'),
('E005', 'Awakura Lain Li', '28', '1995-07-07', 'f', 'passport', '8923172178', 'teacher', 'lastprotocol@mail.ru', '27');

INSERT INTO `project`.`events` (`name`, `place`, `date_time`, `employees_ev_org_id`, `description`) VALUES 
('school jubiley', 'school hall', '2023-05-05 13:00:00', 'E002', 'Hooray nashey school celih nol let!!!'),
('day of kofeman', 'school bufet', '2023-06-08 17:00:00', 'E003', 'COFFEE!!!');

INSERT INTO `project`.`departments` (`id_departments`, `name`, `head`, `age_restrictions`, `description`) VALUES 
('D01', 'Maths', 'Petr Petrov', '7-18', 'Solving different tasks'),
('D02', 'Programming', 'Lain Awakura', '10-18', 'web development processes'),
('D03', 'Design', 'Katerina Margancova', '10-18', 'design practice and theory'),
('D04', 'Robotics', 'Igor Svetlov', '13-18', 'all styles of making & coding robots');

INSERT INTO `project`.`classes` (`id_classes`,`name`, `departments_id`, `employees_id`, `classroom`, `days`, `time`, `description`) VALUES
('C01', 'OlympMaths', 'D01', 'E001', '237', 'mon thy sat', '18:30 - 20:00', 'Very Intersting'),
('C02', 'C++ coding', 'D02', 'E004', '217', 'mon tue wed', '18:30 - 20:00', 'coding!!!'),
('C03', 'Logical operations', 'D02', 'E005', '218', 'thu fri sat', '16:00 - 18:00', 'logica'),
('C04', 'History Design', 'D03', 'E002', '307', 'fri sat', '15:30 - 17:00', 'Very Intersting!'),
('C05', 'Controllers', 'D04', 'E003', '308', 'mon wen fri', '17:30 - 19:30', 'Prog and Create controllers for robots;)'),
('C06', 'SchoolMaths', 'D01', 'E001', '237', 'mon thy sat', '17:00 - 18:30', 'Extra School Lessons');

INSERT INTO `project`.`workload` (`students_id`, `departments_id`, `classes_id`, `employees_id`, `selected days`,`teacher's_commentary`) VALUES 
('S001', 'D02', 'C03', 'E005', 'thu fri', NULL),
('S002', 'D01', 'C01', 'E001', 'mon sat', NULL),
('S010', 'D03', 'C04', 'E002', 'sat', NULL),
('S002', 'D04', 'C05', 'E003', 'mon wen', NULL),
('S004', 'D04', 'C05', 'E003', 'mon', NULL),
('S005', 'D01', 'C01', 'E001', 'mon thu sat', NULL),
('S005', 'D01', 'C06', 'E001', 'mon thu sat', NULL),
('S006', 'D02', 'C02', 'E004', 'mon tue wed', NULL),
('S006', 'D02', 'C03', 'E005', 'thu fri sat', NULL),
('S007', 'D03', 'C04', 'E002', 'fri sat', 'do not seat with other students'),
('S008', 'D04', 'C05', 'E003', 'mon wen fri', NULL),
('S009', 'D01', 'C01', 'E001', 'mon sat', NULL),
('S009', 'D02', 'C02', 'E004', 'mon', NULL),
('S011', 'D03', 'C04', 'E002', 'sat', NULL),
('S012', 'D04', 'C05', 'E003', 'mon wen', NULL),
('S013', 'D02', 'C02', 'E004', 'mon tue', 'do not make effort with student'),
('S014', 'D01', 'C01', 'E001', 'mon', NULL),
('S014', 'D01', 'C06', 'E001', 'mon', NULL),
('S015', 'D03', 'C04', 'E002', 'sat', 'not payed enough'),
('S016', 'D01', 'C01', 'E001', 'sat', NULL),
('S016', 'D01', 'C06', 'E001', 'sat', NULL),
('S017', 'D02', 'C02', 'E004', 'mon tue', NULL),
('S018', 'D04', 'C05', 'E003', 'wen', NULL),
('S019', 'D03', 'C04', 'E002', 'fri sat', 'seat closer to teacher'),
('S020', 'D03', 'C04', 'E002', 'fri ', NULL);

INSERT INTO `project`.`users` (`Login`, `Password`, `students_id`, `employees_id`) VALUES 
('tulenchik666', 'kukarekyyyyy', 'S002', Null),
('amiranagibator228', 'zaychik1999', 'S003', Null),
('nastyamirnaya228', 'bitcheslocal1333', 'S004', Null),
('vladospapiros777', 'ogurec2003', 'S005', Null),
('dant4ick2203', 'yalubluselenygomez', 'S006', Null),
('leshaXgod', 'secretsecret3', 'S007', Null),
('maximova2007', 'optimusprime666', 'S008', Null),
('SobchakSobchak', 'ahahahahahahahah', 'S009', Null),
('gorshochekschemto', 'witchersdoll', 'S010', Null),
('psihushkaa4', 'lovenhante333', 'S011', Null),
('aloecoder', 'gtbsg0000', 'S012', Null),
('benjaminSek', 'aoaoaoaoaoaooaoa', 'S013', Null),
('tumortumor', 'inspiteofwar2007', 'S014', Null),
('vladosmiros', 'nuaktogood', 'S015', Null),
('rudik777', 'gnomiiiiik', 'S016', Null),
('zhukovN', 'zhuknevivozhuk', Null, 'E001'),
('margancova2008', 'ihkatyakatya', Null, 'E002'),
('svetlovv', 'parol228775', Null, 'E003'),
('linuxlover1993', '44444444', Null, 'E004'),
('lainlainlain', 'lastprotocol', Null, 'E005');