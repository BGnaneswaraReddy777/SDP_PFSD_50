from django.db import models
class Docter(models.Model):
    Docusername = models.CharField(max_length=10)
    Docterpassword= models.CharField(max_length=200)
    Docteremail= models.EmailField()
    googlelink= models.CharField(max_length=150)

    class Meta:

        db_table="Docter"
# # Create your models here.
