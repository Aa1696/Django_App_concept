from django.db import models

# Create  models here.
# Add blog app to settings.
#Create a migration.
#Migrate
#Add to admin



class Blog(models.Model):
    title=models.CharField(max_length=100)
    model_image=models.ImageField(upload_to='images/')
    proj_date=models.DateTimeField()
    proj_body=models.TextField(max_length=500)

    def __str__(self):
        return self.title

    def summary(self):
        return self.proj_body[:100]


