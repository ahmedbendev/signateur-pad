from django.db import models

# Create your models here.

class Signateur(models.Model):
      img_data = models.ImageField(upload_to='signateur_pics')

      def __str__(self):
          return str(self.pk)   