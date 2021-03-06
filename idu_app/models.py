from django.db import models

# Create your models here.
class teacher(models.Model):
    """Faculty details form class"""

    photo = models.ImageField(upload_to="home/images", default="")
    name = models.CharField(max_length=255, default="")
    designation = models.CharField(max_length=255, default="")
    about = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.name

class student(models.Model):
    """Student details form class"""
  
    stu_roll_no = models.IntegerField(unique=True)
    stu_first_name = models.CharField(max_length=255, default="")
    stu_last_name = models.CharField(max_length=255, default="")
    stu_full_name = models.CharField(max_length=255, default="")
    stu_semester = models.CharField(max_length=10, default="")
    stu_father_name = models.CharField(max_length=255, default="")
    stu_mother_name = models.CharField(max_length=255, default="")
    stu_contact = models.CharField(max_length=15)
    stu_address_line1 = models.CharField(max_length=255, default="")
    stu_address_line2 = models.CharField(max_length=255, default="")
    stu_city = models.CharField(max_length=100, default="")
    stu_postalcode = models.CharField(max_length=6)

    def __str__(self):
        return self.stu_full_name
    
class mark(models.Model):
    """Class for storing student Marks"""

    stu_full_name = models.CharField(max_length=255, default="")
    stu_roll_no = models.IntegerField(unique=True)
    stu_semester = models.CharField(max_length=10, default="")
    stu_sub1 = models.CharField(max_length=4, default=0)
    stu_sub2 = models.CharField(max_length=4, default=0)
    stu_sub3 = models.CharField(max_length=4, default=0)
    stu_sub4 = models.CharField(max_length=4, default=0)
    stu_sub5 = models.CharField(max_length=4, default=0)
    stu_total_marks = models.IntegerField()
    stu_average_marks = models.IntegerField()

    def __str__(self):
        return self.stu_full_name

class contact(models.Model):
    """Class for storing contact details requests"""

    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=15, default=0)
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name



