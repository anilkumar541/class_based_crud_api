from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'
        default_permissions = ()

    def __unicode__(self):    
        return self.category_name
        
