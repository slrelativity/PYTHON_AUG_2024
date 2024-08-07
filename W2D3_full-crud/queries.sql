-- TEST for DOGS DB --

-- Read (get all dogs)
SELECT * FROM dogs;

-- Create Dogs
INSERT INTO dogs
	(name, age, breed, color)
VALUES
	('Spot', 4, 'Lab', 'brown'),
    ('Zoey', 4, 'GSP', 'grey'),
    ('Nala', 3, 'cane corso', 'grey');