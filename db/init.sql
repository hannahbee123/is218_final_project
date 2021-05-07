CREATE DATABASE biostatsData;
use biostatsData;

CREATE TABLE IF NOT EXISTS biostats (
    `id` int AUTO_INCREMENT,
    `biostats_1` VARCHAR(4) CHARACTER SET utf8,
    `Column_2` VARCHAR(10) CHARACTER SET utf8,
    `Column_3` VARCHAR(6) CHARACTER SET utf8,
    `Column_4` VARCHAR(14) CHARACTER SET utf8,
    `Column_5` VARCHAR(15) CHARACTER SET utf8,
    PRIMARY KEY (`id`)
);
INSERT INTO biostats (biostats_1,Column_2,Column_3,Column_4,Column_5) VALUES
    ('Alex','       "M"','41','74','170'),
    ('Bert','       "M"','42','68','166'),
    ('Carl','       "M"','32','70','155'),
    ('Dave','       "M"','39','72','167'),
    ('Elly','       "F"','30','66','124'),
    ('Fran','       "F"','33','66','115'),
    ('Gwen','       "F"','26','64','121'),
    ('Hank','       "M"','30','71','158'),
    ('Ivan','       "M"','53','72','175'),
    ('Jake','       "M"','32','69','143'),
    ('Kate','       "F"','47','69','139'),
    ('Luke','       "M"','34','72','163'),
    ('Myra','       "F"','23','62','98'),
    ('Neil','       "M"','36','75','160'),
    ('Omar','       "M"','38','70','145'),
    ('Page','       "F"','31','67','135'),
    ('Quin','       "M"','29','71','176'),
    ('Ruth','       "F"','28','65','131');
