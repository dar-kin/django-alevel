from django.db import models


class Author1(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book1(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author1, related_name="books", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

