
drop TABLE schedules;
drop TABLE appointments;
drop TABLE pets;
drop TABLE users;

CREATE TABLE users (
  user_id SERIAL PRIMARY KEY,
  name VARCHAR(30),
  email VARCHAR(35),
  password VARCHAR(20),
  zipcode VARCHAR(10),
  phone_no VARCHAR(12)
);

INSERT INTO users (name, email, password, zipcode, phone_no) VALUES ('aleena waseem', 'aleenawaseem@ymail.com', 'pet1', '94582', '5103998740');
INSERT INTO users (name, email, password, zipcode, phone_no) VALUES ('taymoor khan', 'taymoor.response@gmail.com', 'pet12', '94586', '5108945182');
INSERT INTO users (name, email, password, zipcode, phone_no) VALUES ('amal taymoor', 'aleenataymoor@gmail.com', 'pet123', '94536', '6503137835');
INSERT INTO users (name, email, password, zipcode, phone_no) VALUES ('adil waseem', 'virgo_bizrate@yahoo.com', 'pet1234', '94568', '5108946595');


CREATE TABLE pets (
  pet_id SERIAL PRIMARY KEY,
  pet_name VARCHAR(30),
  species VARCHAR(20),
  user_id INTEGER REFERENCES users,
  pic_url VARCHAR(255)
);


INSERT INTO pets (pet_name, species, user_id, pic_url) VALUES ('Poppy', 'cat', 3, 'https://i.imgur.com/6ygEgmB.jpeg');
INSERT INTO pets (pet_name, species, user_id, pic_url) VALUES ('Bruno', 'dog', 4, 'https://post.medicalnewstoday.com/wp-content/uploads/sites/3/2020/02/322868_1100-800x825.jpg');
INSERT INTO pets (pet_name, species, user_id, pic_url) VALUES ('Kiwi', 'parrot', 1, 'https://pixy.org/src/469/thumbs350/4692529.jpg');
INSERT INTO pets (pet_name, species, user_id, pic_url) VALUES ('Chase', 'dog', 2, 'https://secure.img1-fg.wfcdn.com/im/03796479/resize-h445%5Ecompr-r85/4307/43074506/Hanging+Golden+Retriever+Puppy+Statue.jpg');


CREATE TABLE appointments (

  appointment_id SERIAL PRIMARY KEY,
  pet_id INTEGER REFERENCES pets,
  appointment_time_stamp timestamp,
  appointment_type VARCHAR(15),
  send_reminder Boolean
);

INSERT INTO appointments (pet_id) VALUES (1);
INSERT INTO appointments (pet_id) VALUES (2);
INSERT INTO appointments (pet_id) VALUES (3);
INSERT INTO appointments (pet_id) VALUES (4);


CREATE TABLE schedules (

  schedule_id SERIAL PRIMARY KEY,
  pet_id INTEGER REFERENCES pets,
  schedule_type VARCHAR(15),
  time_schedule timestamp
);

INSERT INTO schedules (pet_id)  VALUES (1);
INSERT INTO schedules (pet_id) VALUES (2);
INSERT INTO schedules (pet_id) VALUES (3);
INSERT INTO schedules (pet_id) VALUES (4);

CREATE TABLE reminders (

  id SERIAL PRIMARY KEY,
  name varchar(50),
  phone_number varchar(50),
  delta INTEGER,
  time timestamp,
  timezone varchar(50)
);
