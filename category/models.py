from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length = 50, unique=True)
    slug = models.SlugField(max_length = 100, unique=True)
    description = models.TextField(max_length = 255, blank = True)
    cat_image = models.ImageField(upload_to = 'photos/categories', blank = True)

    # to correct the plural form , we use verbose
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
 
#   this function will make the Category of each product , when they click on that , then it will show that Category product only 
    def get_url(self):
         return reverse('products_by_category',args=[self.slug])

    def __str__(self):
        return self.category_name