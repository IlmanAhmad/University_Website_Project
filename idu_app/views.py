from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from idu_app.models import student, mark, contact, teacher
from django.contrib import messages
import pandas as pd

# Create your views here.


def home(request):
    """function to redirect to homepage"""

    return render(request, 'idu_app/home.html')

def faculty(request):
    """funtion to redirect to faculty details page"""
    teachers = teacher.objects.all()
    params = {'teachers': teachers}
    return render(request, 'idu_app/faculty.html', params)


def handlelogin(request):
    """function to handle login authentication"""
    if request.method == "POST":
        user = request.POST.get('user', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=user, password=password)
        if user is not None:
            request.session['uid'] = request.POST.get('user', '')
            login(request, user)
            messages.success(request, "Your login is successful.")
            return redirect("idu:home")
        else:
            messages.error(request, "Invalid id or password")
            return redirect("idu:home")
    else:
        return HttpResponse('404 - Not found')

@login_required
def handlelogout(request):
    """function to handle logout authentication"""
    logout(request)
    messages.success(request, "Your have successfully logged out")
    return redirect("idu:home")


def contactus(request):
    """function to redirect to contact us page"""
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contacts = contact(name=name, email=email, phone=phone, desc=desc)
        contacts.save()
        messages.success(
            request, "Your request has been submitted. We'll revert back to you with details soon.")
        return render(request, "idu_app/contact.html")

    return render(request, 'idu_app/contact.html')


def programmedetails(request):
    """function to redirect to programme details page"""

    return render(request, 'idu_app/programmedetails.html')

@staff_member_required # restricting the URL to admin only users
def studetailsadmin(request):
    """function to redirect to student details admin page"""

    return render(request, 'idu_app/studetailsadmin.html')


def sturegisterdetails(request):
    """function to redirect to student details page"""
    if request.method == "POST":
        stu_roll_no = request.POST.get('roll', '')
        stu_details = student.objects.filter(stu_roll_no=stu_roll_no).values()
        params = {'stu_details': stu_details}
        return render(request, 'idu_app/sturegisterdetails.html', params)

    return render(request, 'idu_app/sturegisterdetails.html')


def results(request):
    """function to redirect to student results page"""
    if request.method == "POST":
        stu_roll_no = request.POST.get('roll_no', '')
        mark_list = mark.objects.filter(stu_roll_no=stu_roll_no).values()
        params = {'mark_list': mark_list}
        return render(request, 'idu_app/results.html', params)

    return render(request, 'idu_app/results.html')


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
            stu_semester = str(stu_data.at[i, 'stu_semester'])
            stu_roll_no = int(stu_data.at[i, 'stu_roll_no'])
            stu_father_name = str(stu_data.at[i, 'stu_father_name'])
            stu_contact = str(stu_data.at[i, 'stu_contact'])
            stu_mother_name = str(stu_data.at[i, 'stu_mother_name'])
            stu_address_line1 = str(stu_data.at[i, 'stu_address_line1'])
            stu_address_line2 = str(stu_data.at[i, 'stu_address_line2'])
            stu_city = str(stu_data.at[i, 'stu_city'])
            stu_postalcode = str(stu_data.at[i, 'stu_postalcode'])
            students = student(stu_first_name=stu_first_name, stu_last_name=stu_last_name, stu_full_name=stu_full_name,
                               stu_semester=stu_semester, stu_roll_no=stu_roll_no, stu_father_name=stu_father_name, stu_contact=stu_contact,
                               stu_mother_name=stu_mother_name, stu_address_line1=stu_address_line1, stu_address_line2=stu_address_line2,
                               stu_city=stu_city, stu_postalcode=stu_postalcode)
            students.save()

        messages.success(
            request, "Your student registeration data has been successfully uploaded.")
        return redirect("idu:studetailsadmin")
    else:
        return HttpResponse('404 - Not found')


def updatestudetailsadmin(request):
    """This function is for modifying student details in database"""

    if request.method == "POST":
        stu_data = pd.read_excel(request.FILES.get(
            'excelfile'))
        data_length = range(len(stu_data))
        for i in data_length:
            stu_roll_no = int(stu_data.at[i, 'stu_roll_no'])
            stu_obj = student.objects.get(stu_roll_no=stu_roll_no)
            if stu_obj.stu_roll_no == stu_roll_no:
                stu_obj.stu_first_name = str(stu_data.at[i, 'stu_first_name'])
                stu_obj.stu_last_name = str(stu_data.at[i, 'stu_last_name'])
                stu_obj.stu_full_name = str(stu_data.at[i, 'stu_full_name'])
                stu_obj.stu_semester = str(stu_data.at[i, 'stu_semester'])
                stu_obj.stu_father_name = str(
                    stu_data.at[i, 'stu_father_name'])
                stu_obj.stu_contact = str(stu_data.at[i, 'stu_contact'])
                stu_obj.stu_mother_name = str(
                    stu_data.at[i, 'stu_mother_name'])
                stu_obj.stu_address_line1 = str(
                    stu_data.at[i, 'stu_address_line1'])
                stu_obj.stu_address_line2 = str(
                    stu_data.at[i, 'stu_address_line2'])
                stu_obj.stu_city = str(stu_data.at[i, 'stu_city'])
                stu_obj.stu_postalcode = str(stu_data.at[i, 'stu_postalcode'])

                stu_obj.save()
        messages.success(
            request, "Your student registeration data has been successfully modified.")

        return redirect("idu:studetailsadmin")


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
            stu_semester = str(stu_marks.at[i, 'stu_semester'])
            stu_sub1 = int(stu_marks.at[i, 'stu_sub1'])
            stu_sub2 = int(stu_marks.at[i, 'stu_sub2'])
            stu_sub3 = int(stu_marks.at[i, 'stu_sub3'])
            stu_sub4 = int(stu_marks.at[i, 'stu_sub4'])
            stu_sub5 = int(stu_marks.at[i, 'stu_sub5'])
            stu_total_marks = int(stu_sub1 + stu_sub2 +
                                  stu_sub3 + stu_sub4 + stu_sub5)
            stu_average_marks = int((stu_total_marks/500) * 100)

            marks = mark(stu_full_name=stu_full_name, stu_roll_no=stu_roll_no, stu_semester=stu_semester,
                         stu_sub1=stu_sub1, stu_sub2=stu_sub2, stu_sub3=stu_sub3, stu_sub4=stu_sub4, stu_sub5=stu_sub5,
                         stu_total_marks=stu_total_marks, stu_average_marks=stu_average_marks)
            marks.save()
        messages.success(request, "Marksheets has been successfully uploaded.")
        return redirect("idu:studetailsadmin")
    else:
        return HttpResponse('404 - Not found')


def updatemarksheet(request):
    """This function is for modifying student marksheet data in database"""

    if request.method == "POST":
        stu_data = pd.read_excel(request.FILES.get(
            'excelmarksfile'))
        data_length = range(len(stu_data))
        for i in data_length:
            stu_roll_no = int(stu_data.at[i, 'stu_roll_no'])
            stu_obj = mark.objects.get(stu_roll_no=stu_roll_no)
            if stu_obj.stu_roll_no == stu_roll_no:
                stu_obj.stu_full_name = str(stu_data.at[i, 'stu_full_name'])
                stu_obj.stu_semester = str(stu_data.at[i, 'stu_semester'])
                stu_obj.stu_sub1 = int(stu_data.at[i, 'stu_sub1'])
                stu_obj.stu_sub2 = int(stu_data.at[i, 'stu_sub2'])
                stu_obj.stu_sub3 = int(stu_data.at[i, 'stu_sub3'])
                stu_obj.stu_sub4 = int(stu_data.at[i, 'stu_sub4'])
                stu_obj.stu_sub5 = int(stu_data.at[i, 'stu_sub5'])
                stu_obj.stu_total_marks = int(stu_obj.stu_sub1 + stu_obj.stu_sub2 +
                                  stu_obj.stu_sub3 + stu_obj.stu_sub4 + stu_obj.stu_sub5)
                stu_obj.stu_average_marks = int((stu_obj.stu_total_marks/500) * 100)

                stu_obj.save()
        messages.success(
            request, "Your student marksheet data has been successfully modified.")

        return redirect("idu:studetailsadmin")

    
