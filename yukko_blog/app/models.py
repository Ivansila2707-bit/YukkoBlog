from django.db import models

class Articles(models.Model):
    title = models.CharField('Пост',max_length=250)
    full_text = models.TextField('Текст поста')
    date = models.DateTimeField('Дата и время публикации')

    def __str__(self):
        return f"Пост: {self.title}"
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
