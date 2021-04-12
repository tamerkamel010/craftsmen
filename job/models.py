from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# Client Model 
class Client(AbstractUser):
    country = models.CharField(max_length=500, default='Egypt')
    city = models.CharField(max_length=500, default='Cairo')
    phone = models.CharField(max_length=12)
    job_title = models.CharField(max_length=500, default='Just Client', null=True, blank=True)
    job_category = models.ForeignKey('Category', on_delete=models.DO_NOTHING)
    profile_img = models.ImageField(upload_to = 'imgs/')
    user_permissions = None
    groups = None
    class Category(models.TextChoices):
        CRAFTSMAN = 'CM', ('Craftsman')
        WORK_OWNER = 'Emp', ('Employer')
    category = models.CharField(max_length=500, choices=Category.choices, default=Category.WORK_OWNER)
    rate = models.IntegerField()
    # get Full Name 
    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ('first_name', )
        db_table = 'Clients'
    def __str__(self):
        return '%s %s' %(self.first_name, self.last_name)
# Job Model 
class Job(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=500)
    slug = AutoSlugField(populate_from = 'title', unique = True) # slug 
    content = models.TextField(max_length=2000)
    location = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='imgs/', blank=True, null=True)
    min_bid = models.DecimalField(max_digits=9, decimal_places=2)
    max_bid = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    # absoutle_url 
    def get_absolute_url(self):
        return reverse('job_detail', kwargs={ 'slug' : self.slug })

    # Save 
    def save(self, *args, **kwargs, ):
        self.slug = slugify(self.job_title + '-' + self.slug + str(get_random_string(12)) )
        super(Job, self).save(*args, **kwargs)
    # Meta 
    class Meta:
        ordering = ['job_title']
        db_table = 'Jobs'
    def __str__(self):
        return self.job_title
    

# Category Model 
class Category(models.Model):
    name = models.CharField(max_length=500)
    class Meta:
        db_table = 'Job Categories'
        ordering = ['name']
    def __str__(self):
        return self.name