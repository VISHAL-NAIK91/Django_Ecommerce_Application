from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name_plural  = 'categories'
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name