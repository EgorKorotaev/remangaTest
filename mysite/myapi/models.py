from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Title(models.Model):
    ru_name = models.CharField(max_length=280)
    en_name = models.CharField(max_length=280)
    alt_name = models.CharField(max_length=280)
    description = models.CharField(max_length=1000)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.ru_name} / {self.en_name} / {self.alt_name}"


class Volume(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name="title_volume")
    name = models.CharField(max_length=280)
    cost = models.IntegerField()
    number = models.CharField(max_length=60)  # номер тома

    def __str__(self):
        return f"volume {self.number} «{self.name}»"


class Chapter(models.Model):
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE, related_name="volume_chapter")
    number = models.CharField(max_length=60)
    content = models.TextField()
    view_counter = models.IntegerField(default=0)
    likes_counter = models.IntegerField(default=0)

    def __str__(self):
        return f"chapter {self.number}"

    def increase_view_counter(self):
        self.view_counter += 1
        return self

    def increase_likes_counter(self):
        self.likes_counter += 1
        return self

