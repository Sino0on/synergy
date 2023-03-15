from django.db import models


class Program(models.Model):
    title = models.CharField(max_length=123)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='programs/')
    pre_image = models.CharField(max_length=123)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Программа'
        verbose_name_plural = 'Программы'
        ordering = ['-date']


class Grant(models.Model):
    title = models.CharField(max_length=123)
    preview = models.CharField(max_length=255)
    image = models.ImageField(upload_to='grants/')
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Грант'
        verbose_name_plural = 'Гранты'
        ordering = ['-date']


class Feedback(models.Model):
    name = models.CharField(max_length=123)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    proffesion = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-date']

