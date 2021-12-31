# Create your models here.
from ckeditor.fields import RichTextField
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse


# Create your models here.
class Blog(models.Model):
    heading = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    sub_head = models.CharField(max_length=200, null=True)
    desc = RichTextField(blank=True, null=True)
    more_desc = RichTextField(blank=True, null=True)
    img = models.ImageField(upload_to='blog/')
    author = models.CharField(max_length=100, default=None)
    date = models.DateField()
    list_display = ('heading', 'author', 'date')

    class Meta:
        verbose_name_plural = "Blogs"
        ordering = ('-date',)

    def __str__(self):
        return self.heading

    def get_detail_url(self):
        return reverse("blog_details", kwargs={'b_slug': self.slug})


class Contact(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    from_email = models.EmailField()
    mobile_num = models.CharField(max_length=15, null=True)
    subject = models.CharField(max_length=15, null=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.name + "-" + self.from_email


class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{10,10}$',
        message="Phone must be in the format: '+999999999'.Please enter 10 digits mobile number.")
    phone = models.CharField(validators=[phone_regex], max_length=10)
    website = models.CharField(max_length=100)

    def __str__(self):
        return self.name + "-" + self.email


class Testimonials(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testmonial_profiepic/')
    quote = models.TextField()

    def __str__(self):
        return self.name + "-" + self.company


class Clients(models.Model):
    company_name = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='clients_logo/')

    def __str__(self):
        return self.company_name + "-" + self.website


class Email_subscription(models.Model):
    email = models.EmailField()


class Blog_Comment(models.Model):
    name = models.CharField(max_length=100)
    slug=models.SlugField()
    email = models.CharField(max_length=100)
    message = models.TextField()
    date=models.DateTimeField(auto_now_add=True,null=True)
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
