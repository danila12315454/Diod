from django.db import models


class User(models.Model):
    login = models.CharField(max_length=15, verbose_name="Логин")
    email = models.CharField(max_length=40, verbose_name="Почта")
    password = models.CharField(max_length=30, verbose_name="Пароль")
    name = models.CharField(max_length=30, verbose_name="Имя")
    description = models.CharField(max_length=300, verbose_name="Описание", )

    profile_photo = models.ImageField(upload_to="photos/profile_photos", verbose_name="Фото аккаунта", blank=True)


class Post(models.Model):
    creator_id = models.IntegerField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    photos = models.ImageField(upload_to="photos/post_photos")
    text = models.CharField(max_length=1000)
    like_num = models.IntegerField()
    like_list = models.CharField(max_length=1000)

    def get(self, value):
        value = str(value)
        if value == "like_list":
            return str(self.like_list).split("~@~")
        else:
            return -1


class Chats(models.Model):
    chat_id = models.IntegerField()
    user_ids = models.CharField(max_length=1000)
    chat_photo = models.ImageField(upload_to="photos/chat_photos")
    msg_history = models.CharField(max_length=1000000)

    def get(self, value):
        value = str(value)
        if value == "msg_history":
            return [tuple(i.split("@~@")) for i in str(self.msg_history).split("~@~")]
        elif value == "user_ids":
            return str(self.user_ids).split("~@~")
        else:
            return -1
