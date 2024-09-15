from django.shortcuts import render, HttpResponse, redirect
from .models import Student, Department
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')


def view_all_students(request):
    stu = Student.objects.all()
    context = {
        'stu': stu
    }
    return render(request, 'view_all_students.html', context)


def add_students(request):
    departments = Department.objects.all()  # Fetch all departments to display in the dropdown

    if request.method == 'POST':
        # Fetching form data
        roll_no = request.POST['roll_no']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept_id = request.POST['dept']
        phone = request.POST['phone']
        email = request.POST['email']
        date_of_birth = request.POST.get('date_of_birth', None)  # Optional
        gender = request.POST.get('gender', '')  # Optional

        try:
            # Find the department by id
            department = Department.objects.get(id=dept_id)

            # Create and save the new student
            student = Student.objects.create(
                roll_no=roll_no,
                first_name=first_name,
                last_name=last_name,
                dept=department,
                phone=phone,
                email=email,
                date_of_birth=date_of_birth,
                gender=gender,
            )
            student.save()

            return redirect('view_all_students')
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}")

    # If GET request, render the form with department data
    return render(request, 'add_students.html', {'departments': departments})


def remove_students(request):
    stu = Student.objects.all()
    context = {
        'stu': stu
    }
    return render(request, 'remove_students.html', context)

def delete(request,student_id):
    dele=Student.objects.get(id=student_id)
    dele.delete()
    return redirect('remove_students')




def filter_students(request):
    if request.method == 'POST':
        name=request.POST['name']
        stu=Student.objects.all()
        if name:
            stu=stu.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        context={
            'stu':stu
        }
        return render(request,'view_all_students.html',context)
    elif request.method=='GET':
        return render(request, 'filter_students.html')
    else:
        return HttpResponse("An exception occured!!!")

