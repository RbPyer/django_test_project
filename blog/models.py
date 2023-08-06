from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Post(models.Model):
    """
    Data about record
    """
    title = models.CharField("Заголовок поста", max_length=100)
    main_text = models.TextField("Текст поста")
    author = models.CharField("Автор", max_length=100)
    date = models.DateField("Дата публикации")
    image = models.ImageField("Изображение", upload_to="image/%Y")

    def __str__(self):
        return f"{self.title} | {self.author}"

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comments(models.Model):
    """
    Comments from users
    """
    email = models.EmailField()
    name = models.CharField("Имя", max_length=50)
    text_comments = models.TextField("Комментарий", max_length=2000)
    post = models.ForeignKey(Post, verbose_name="Публикация", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} | {self.post}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
