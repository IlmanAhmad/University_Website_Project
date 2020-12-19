from django.db import models

# Create your models here.
class student(models.Model):
    """Student details form class"""

    stu_first_name = models.CharField(max_length=255, default="")
    stu_last_name = models.CharField(max_length=255, default="")
    stu_full_name = models.CharField(max_length=255, default="")
    stu_class = models.CharField(max_length=10, default="")
    stu_roll_no = models.IntegerField(primary_key=True, unique=True)
    stu_father_name = models.CharField(max_length=255, default="")
    stu_contact = models.CharField(max_length=15)
    stu_mother_name = models.CharField(max_length=255, default="")
    stu_address_line1 = models.CharField(max_length=255, default="")
    stu_address_line2 = models.CharField(max_length=255, default="")
    stu_city = models.CharField(max_length=100, default="")
    stu_postalcode = models.CharField(max_length=6)

    def __str__(self):
        return self.stu_full_name
    
class mark(models.Model):
    """Class for storing student Marks"""

    stu_roll_no = models.ForeignKey(student, on_delete=models.CASCADE)
    stu_full_name = models.CharField(max_length=255, default="")
    stu_class = models.CharField(max_length=10, default="")
    stu_sub1 = models.CharField(max_length=4, default=0)
    stu_sub2 = models.CharField(max_length=4, default=0)
    stu_sub3 = models.CharField(max_length=4, default=0)
    stu_sub4 = models.CharField(max_length=4, default=0)
    stu_sub5 = models.CharField(max_length=4, default=0)
    stu_total_marks = models.CharField(max_length=4, default=0)
    stu_average_marks = models.CharField(max_length=4, default=0)

    def __str__(self):
        return self.stu_roll_no



