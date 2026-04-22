from django.db import models

# Create your models here.


class StudentAusweis(models.Model):
    ausweis_nummer = models.CharField(max_length=20, unique=True)
    gueltig_bis = models.DateField()

    def __str__(self):
        return f"Ausweis {self.ausweis_nummer}"
    


class Student(models.Model):
   name = models.CharField(max_length=100)
   ausweis = models.OneToOneField(StudentAusweis, on_delete=models.PROTECT)
   matrikel_nummer = models.CharField(max_length=20, unique=True)

   def __str__(self):
       return f"{self.name} ({self.matrikel_nummer})"
   

class Professor(models.Model):
    name = models.CharField(max_length=100)
    fachgebiet = models.CharField(max_length=100)

    def __str__(self):
       return self.name
    

class Semester(models.Model):
    bezeichnung = models.CharField(max_length=50)

    def __str__(self):
        return self.bezeichnung


class Kursbeschreibung(models.Model):
    beschreibung = models.TextField()
    kurs = models.OneToOneField('Kurs', on_delete=models.CASCADE, )

    def __str__(self):
        return self.beschreibung[:50] # Zeigt die ersten 50 Zeichen der Kursbeschreibung an
    

class Kurs(models.Model):
    titel = models.CharField(max_length=200)
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, blank=True, related_name='kurse')
    semester = models.ForeignKey(Semester, on_delete=models.SET_NULL, null=True, blank=True)
    studenten = models.ManyToManyField(Student)

    def __str__(self):
        return self.titel
       




