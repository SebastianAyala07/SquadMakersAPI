CREATE DATABASE squadmakers;
use squadmakers;

CREATE TABLE `joke` (
    `id` int AUTO_INCREMENT,
    `joke_text` varchar(250) NOT NULL,
    primary key(`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

insert  into `joke`(`joke_text`) values
('What kind of tea is hard to swallow? Reality'),
('What do you call a pig that does karate? A pork chop');
