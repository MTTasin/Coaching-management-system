from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class courses(models.Model):
    image = models.ImageField(upload_to='courses/')
    title = models.CharField(max_length=100)
    marketing_line = models.CharField(max_length=1000)
    description_for_card = RichTextUploadingField(blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.title
    

class teachers(models.Model):
    image = models.ImageField(upload_to='students/', blank=True, null=True)
    user = models.ForeignKey('profile', on_delete=models.CASCADE, related_name='teachers') 
    description = RichTextUploadingField(blank=True, null=True)
    salary = models.IntegerField()


    def save(self, *args, **kwargs):
        if not self.image and self.user.image:
            self.image = self.user.image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.name.username
    
class teachers_attandance(models.Model):
    name = models.ManyToManyField("teachers", verbose_name=("Teachers"))
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class class_topic(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    courses = models.ManyToManyField("courses", verbose_name=("Courses"))
    description = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.title


class routine(models.Model):
    title = models.CharField(max_length=100)
    courses = models.ManyToManyField("courses", verbose_name=("Courses"))
    routine_pdf = models.FileField(upload_to='routine/', default='routine/nonepdf.pdf')

    def __str__(self):
        return self.title
    
class results(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField("courses", verbose_name=("Courses"))
    result = models.FileField(upload_to='results/', default='results/default.pdf')
    

    def __str__(self):
        return self.name
    
class students(models.Model):
    image = models.ImageField(upload_to='students/', blank=True, null=True)
    user = models.ForeignKey('profile', on_delete=models.CASCADE, related_name='students')   
    address = models.CharField(max_length=100)
    courses = models.ManyToManyField("courses", verbose_name=("Courses"))
    description = RichTextUploadingField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.image and self.user.image:
            self.image = self.user.image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.name.username

class students_attandance(models.Model):
    name = models.ManyToManyField("students", verbose_name=("Students"))
    date = models.DateField()

    def __str__(self):
        return str(self.date)


    
class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class gallery(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    
    def __str__(self):
        return self.name


class carousel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='carousel/')
    color = models.CharField(max_length=10)
    
    
    def __str__(self):
        return self.title
    
class student_payment(models.Model):
    name = models.ManyToManyField("students", verbose_name=("Students"))
    pay_for = models.CharField(max_length=100)
    paid_amount = models.IntegerField()
    paid_date = models.DateField()
    

    def __str__(self):
        return str(self.name.first())


class profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile/default.png', upload_to='profile/')
    
    def __str__(self):
        return f'{self.name.username}'
    def save(self, *args, **kwargs):
        super(profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path) # Open image

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.image.path) # Save it again and override the larger image


class give_number(models.Model):
    number = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.number)

class enroll(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    gurdian_name = models.CharField(max_length=100)
    gurdian_phone = models.IntegerField()
    gurdian_relation = models.CharField(max_length=100)
    courses = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class notices(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextUploadingField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title