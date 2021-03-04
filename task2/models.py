from django.db import models


class Library(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name="authors")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, related_name="books")
    available = models.BooleanField(default=True)
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.name


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class TakenBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, related_name="takes")
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, related_name="taken_books")
    returned = models.BooleanField(default=False)
    take_date = models.DateTimeField(auto_now_add=True)
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name="taken_books")