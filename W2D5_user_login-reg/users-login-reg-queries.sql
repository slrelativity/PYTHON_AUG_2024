-- users login reg queries

SELECT * FROM users;

-- create user -- 
INSERT INTO users (first_name, last_name, email, password)
VALUES ('alice', 'alisson', 'a@a.com', '12345678');

-- find a user by email
SELECT * FROM users
WHERE email = 'asdfsdaasdsadasd@asdsa.com';

-- get user by id
SELECT * FROM users
WHERE id = 3;