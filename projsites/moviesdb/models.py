from django.db import models
# from django.urls import reverse


# Create your models here.
class Movie(models.Model):
    """Model representing a movie."""
    # # needs modification for poster
    # poster = models.CharField('poster', max_length=1, unique=True, help_text='<a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    # or use ImageField()
    title = models.CharField(max_length=100)
    rating = models.ForeignKey('Grade', help_text='Enter a movie rating category (e.g. PG-13)',
                               on_delete=models.SET_NULL, null=True)
    duration = models.IntegerField(help_text='Select a genre for this book')

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    # def get_absolute_url(self):
    #     """Returns the url to buy a ticket for this movie."""
    #     need modification
    #     return reverse('Buy Tickets', args=[str(self.id)])


class Grade(models.Model):
    """Model representing an author."""
    rating_letter = models.CharField(max_length=10)
    details = models.CharField(max_length=100)

    class Meta:
        ordering = ['rating_letter', 'details']

    # def get_absolute_url(self):
    #     """Returns the url to access a particular author instance."""
    #     return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.rating_letter}, {self.details}'
