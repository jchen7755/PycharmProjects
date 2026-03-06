USE petadoptdb;

CREATE TABLE pet_owner (
    LastName varchar(255),
    FirstName varchar(255),
    PetID int
);

INSERT INTO pet_owner VALUES("Mann", "Gray", 1);
INSERT INTO pet_owner VALUES("Jones", "Jordan", 5);
INSERT INTO pet_owner VALUES("Wright", "Mary Anne", 6);

SELECT * FROM pets
LEFT JOIN pet_owner ON pets.ID = pet_owner.PetID;