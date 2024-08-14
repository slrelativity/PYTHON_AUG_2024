-- parties db belt review QUERIES ---
SELECT * FROM users;
SELECT * FROM parties;

-- create a party --
INSERT INTO parties
	(what, location, date, all_ages, description, user_id)
VALUES 
	('space party', 'Mars', '2024-09-09', 1, 'the best party of the century', 1);
    
-- GET ALL PARTIES AND THIER USERS/HOST/creator
SELECT * FROM parties
JOIN users
ON parties.user_id = users.id;

-- get one party
SELECT * FROM parties
JOIN users
ON users.id = parties.user_id
WHERE parties.id = 3;

-- UPDATE a party ---
UPDATE parties
SET
	what = 'update what',
    location = 'update location',
    date = '2024-12-12',
    all_ages = 1,
    description = 'an update!'
WHERE id = 3;
    
    
