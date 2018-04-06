from django.db import models


class Priority(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Task(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    done = models.BooleanField()

    def __str__(self):
        return '{}, priority: {}, done: {}'.format(
            self.description,
            self.priority,
            self.done
        )
