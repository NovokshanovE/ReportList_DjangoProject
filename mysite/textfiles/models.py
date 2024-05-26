from django.db import models

# Create your models here.
# from django.db import models
class Group(models.Model):
    # group_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    # def __str__(self):
    #     return self.name
class TextFile(models.Model):
    group_id = models.ForeignKey(Group, related_name='files',on_delete=models.CASCADE)
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
    
