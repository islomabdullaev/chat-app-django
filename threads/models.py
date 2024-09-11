from django.db import models


class Chat(models.Model):
    name = models.CharField(max_length=36)

    def __str__(self) -> str:
        return self.name


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.CharField(max_length=24)
    message = models.TextField()

    def __str__(self) -> str:
        return f"{self.chat} | {self.user} --> {self.message}"

