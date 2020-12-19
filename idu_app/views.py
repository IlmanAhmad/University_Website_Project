from django.shortcuts import render
from idu_app.models import student
import pandas as pd

# Create your views here.
def home(request):
    """function to redirect to homepage"""
    
    if request.method == "POST":
        # stu_data = pd.read_excel(r'C:\Users\shane\PycharmProjects\pythonProject\Univeritywebsite\studentdata.xlsx')
        stu_data = pd.read_excel(request.FILES.get('excelfile'))
        data_length = range(len(stu_data))

        for i in data_length:
            """ Loop to run data loader for students data """

            stu_first_name = str(stu_data.at[i, 'stu_first_name'])
            stu_last_name = str(stu_data.at[i, 'stu_last_name'])
            stu_full_name = str(stu_data.at[i, 'stu_first_name'])
            stu_class = str(stu_data.at[i, 'stu_class'])
            stu_roll_no = int(stu_data.at[i, 'stu_roll_no'])
            stu_father_name = str(stu_data.at[i, 'stu_father_name'])
            stu_contact = str(stu_data.at[i, 'stu_contact'])
            stu_mother_name = str(stu_data.at[i, 'stu_mother_name'])
            stu_address_line1 = str(stu_data.at[i, 'stu_address_line1'])
            stu_address_line2 = str(stu_data.at[i, 'stu_address_line2'])
            stu_city = str(stu_data.at[i, 'stu_city'])
            stu_postalcode = str(stu_data.at[i, 'stu_postalcode'])
            students = student(stu_first_name=stu_first_name, stu_last_name=stu_last_name, stu_full_name=stu_full_name, 
            stu_class= stu_class, stu_roll_no=stu_roll_no, stu_father_name=stu_father_name, stu_contact=stu_contact, 
            stu_mother_name=stu_mother_name, stu_address_line1=stu_address_line1, stu_address_line2=stu_address_line2, 
            stu_city=stu_city, stu_postalcode=stu_postalcode)
            print(students)
            students.save()

    return render(request,'idu_app/home.html')