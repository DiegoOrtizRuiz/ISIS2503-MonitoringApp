from django.db import models

class Variable(models.Model):
    user = models.CharField(max_length=50)
    value = models.FloatField(null=True, blank=True, default=None)
    
    def __str__(self):
        return '{} {}'.format(self.user, self.value)

