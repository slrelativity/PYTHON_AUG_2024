-- TEST for DOGS DB --

-- Read (get all dogs)
SELECT * FROM dogs;

-- Create Dogs
INSERT INTO dogs (name, age, breed, color)
VALUES ('Spot', 4, 'Lab', 'brown'),
	   ('Zoey', 4, 'GSP', 'grey'),
	   ('Nala', 3, 'cane corso', 'grey');
       
INSERT INTO dogs (name, age, breed, color)
VALUES ('Spot', 4, 'Lab', 'brown');


-- GET one dog
SELECT * FROM dogs
WHERE id=4;


-- UDPATE
UPDATE dogs 
SET 
    name= 'Bobby2',
    age= 4,
    breed= 'big pupper',
    color= 'blue'
WHERE id = 4;

-- get all the awards
SELECT * FROM awards;

-- show me a dog's awards
SELECT * FROM dogs 
LEFT JOIN awards
ON dogs.id = awards.dog_id
WHERE dogs.id = 6;

-- all the awards and recipient 
SELECT * FROM awards
LEFT JOIN dogs
ON awards.dog_id = dogs.id;

