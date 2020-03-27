from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Wizard(models.Model):
    name = models.CharField(max_length=45)
    house = models.CharField(max_length=45)
    pet = models.CharField(max_length=45)
    year = models.IntegerField()



# #SQL Queries to ORM
# from firstORM_APP import Wizard

# #Write SQL queries as ORM commands
# Wizard.objects.create(name='Harry Potter',house='Gryffindor',pet='Hedwig',year=5)
# Wizard.objects.create(name='Hermione Granger',house='Gryffindor',pet='Crookshanks',year=5)
# Wizard.objects.filter(house='Gryffindor')

# wiz = Wizard.objects.get(id=1)
# wiz.year = 6
# wiz.save

# #Write ORM commands as SQL queries
# INSERT INTO Wizard (name, house, pet, year) VALUES ('Luna Lovegood', 'Ravenclaw', 'none', 4);
# INSERT INTO Wizard (name, house, pet, year) VALUES ('Padma Patil', 'Ravenclaw', 'none', 5);
# SELECT house FROM Wizard WHERE house = 'Ravenclaw';
# UPDATE Wizard SET year = 5 WHERE name = 'Luna Lovegood';
