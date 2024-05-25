from django.db import models

# Create your models here.
# from django.db import models

class TextFile(models.Model):
    file_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    # section = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='image/')
    # description = models.TextField()
    

    def __str__(self):
        return self.title
    
    
class Image(models.Model):
    file = models.ForeignKey(TextFile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/')
    description = models.TextField()