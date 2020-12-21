from django.shortcuts import render, redirect, HttpResponse
from idu_app.models import student, mark
from django.contrib import messages
import pandas as pd

# Create your views here.


def home(request):
    """function to redirect to homepage"""

    return render(request, 'idu_app/home.html')

def programmedetails(request):
    """function to redirect to programme details page"""
    return render(request, 'idu_app/programmedetails.html')

def studetails(request):
    """function to redirect to student details page"""

    return render(request, 'idu_app/studetails.html')


def registeration(request):
    """This function is for uploading student details in database"""
    if request.method == "POST":

        stu_data = pd.read_excel(request.FILES.get(
            'excelfile'))  # read file from html form

        data_length = range(len(stu_data))  # calculate length of file

        for i in data_length:
            """ Loop to run data loader for students data """

            stu_first_name = str(stu_data.at[i, 'stu_first_name'])
            stu_last_name = str(stu_data.at[i, 'stu_last_name'])
            stu_full_name = str(stu_data.at[i, 'stu_full_name'])
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
                               stu_class=stu_class, stu_roll_no=stu_roll_no, stu_father_name=stu_father_name, stu_contact=stu_contact,
                               stu_mother_name=stu_mother_name, stu_address_line1=stu_address_line1, stu_address_line2=stu_address_line2,
                               stu_city=stu_city, stu_postalcode=stu_postalcode)
            students.save()
        messages.success(
            request, "Your student registeration data has been successfully uploaded.")
        return redirect("idu:studetails")
    else:
        return HttpResponse('404 - Not found')


def marksheet(request):
    """This function is for uploading student marksheet in database"""
    if request.method == "POST":

        stu_marks = pd.read_excel(request.FILES.get(
            'excelmarksfile'))  # read file from html form
        print(stu_marks)
        data_length = range(len(stu_marks))  # calculate length of file

        for i in data_length:
            """ Loop to run data loader for students marks """

            stu_full_name = str(stu_marks.at[i, 'stu_full_name'])
            stu_roll_no = int(stu_marks.at[i, 'stu_roll_no'])
            stu_class = str(stu_marks.at[i, 'stu_class'])
            stu_sub1 = int(stu_marks.at[i, 'stu_sub1'])
            stu_sub2 = int(stu_marks.at[i, 'stu_sub2'])
            stu_sub3 = int(stu_marks.at[i, 'stu_sub3'])
            stu_sub4 = int(stu_marks.at[i, 'stu_sub4'])
            stu_sub5 = int(stu_marks.at[i, 'stu_sub5'])
            stu_total_marks = int(stu_sub1 + stu_sub2 +
                                  stu_sub3 + stu_sub4 + stu_sub5)
            stu_average_marks = int((stu_total_marks/500) * 100)

            marks = mark(stu_full_name=stu_full_name, stu_roll_no=stu_roll_no, stu_class=stu_class,
                         stu_sub1=stu_sub1, stu_sub2=stu_sub2, stu_sub3=stu_sub3, stu_sub4=stu_sub4, stu_sub5=stu_sub5,
                         stu_total_marks=stu_total_marks, stu_average_marks=stu_average_marks)
            marks.save()
        messages.success(request, "Marksheets has been successfully uploaded.")
        return redirect("idu:studetails")
    else:
        return HttpResponse('404 - Not found')
