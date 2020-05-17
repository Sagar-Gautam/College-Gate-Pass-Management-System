from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from reportlab.pdfgen import canvas

from .models import feedback
from .models import gatepass


def piet(request):
    return render(request,'piet.html')
def about(request):
    return render(request,'about.html')
def signup(request):
    return render(request,'signup.html')
def signup_data(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('pwd')
    cond=User.objects.filter(email=email,username=username)
    if cond:
        return HttpResponse("USER ALREADY EXIST PLEASE CHANGE YOUR EMAIL OR USERNAME ")
    else:
        print(username,password,email)
        user=User.objects.create(username=username,password=password, email=email)
        user.set_password(password)
        user.save()
        return render(request,'login.html')    
    

def ug(request):
    return render(request,'ug.html')
def pg(request):
    return render(request,'pg.html')
def diploma(request):
    return render(request,'diploma.html')
def summarized(request):
    return render(request,'summarized.html')
def programs(request):
    return render(request,'programs.html')
def elig(request):
    return render(request,'elig.html')
def placement(request):
    return render(request,'placement.html')
def btech(request):
    return render(request,'btech.html')
def mtech(request):
    return render(request,'mtech.html')
def bba(request):
    return render(request,'bba.html')
def mba(request):
    return render(request,'mba.html')
def bca(request):
    return render(request,'bca.html')
def mca(request):
    return render(request,'mca.html')
def mca2(request):
    return render(request,'mca2.html')
def diploma1(request):
    return render(request,'diploma1.html')
def bvoc(request):
    return render(request,'bvoc.html')
def pharmacy(request):
    return render(request,'pharmacy.html')
def feedbk(request):
    return render(request,'feedbk.html',{})
def feedbk_data(request):
    name=request.POST.get('name','default')
    fname = request.POST.get('fname', 'default')
    course = request.POST.get('course', 'default')
    email = request.POST.get('email', 'default')
    contact_number = request.POST.get('number', 'default')
    comment = request.POST.get('comment', 'default')
    print(fname, course,email,contact_number,comment)
    feedback.objects.create(name =name, fname = fname, course = course, email =email,contact_number = contact_number,comment = comment)
    return HttpResponse("Thanks for feedback :)")

def login(request):
    return render(request,'login.html')
def login_data(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['pwd']
        print(username,password)
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request)
            return render(request,'piet.html')

        return HttpResponse(" INAVLID USERNAME AND PASSWORD or PLEASE SIGNUP FIRST THEN LOGIN :(")



def tlogin(request):
    return render (request,'tlogin.html')

def tlogin_data(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['pwd']
            print(username, password)
            user = authenticate(username=username, password=password)
            if user is not None and user.is_superuser==True:
                tlogin(request)
                return render(request, 'gate.html')
            return HttpResponse("  PLEASE ENTER A VALID USERNAME AND PASSWORD :( ")

def gate(request):
     name=request.POST.get('name','default')
     father_name=request.POST.get('fname','default')
     roll_no= request.POST.get('roll', 'default')
     branch= request.POST.get('branch', 'default')
     gender= request.POST.get('gender', 'default')
     contact_number = request.POST.get('number', 'default')
     purpose_of_visit= request.POST.get('pov', 'default')
     date=request.POST.get('date', 'default')
     entry_time= request.POST.get('entry', 'default')
     exit_time= request.POST.get('exit', 'default')


     print(name,father_name,roll_no,branch,gender,contact_number,purpose_of_visit,date, entry_time, exit_time )
     gatepass.objects.create(name=name,father_name=father_name, roll_no=roll_no, branch=branch, gender=gender, contact_number=contact_number, purpose_of_visit= purpose_of_visit,date=date, entry_time=entry_time, exit_time=exit_time)
     return HttpResponse("gate pass created<br> <a href='pdf'> download gatepass pdf</a>")

def getpdf(request):
    t=gatepass.objects.all()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'
    p = canvas.Canvas(response)
    for i in t:

        f = i.name
        ff=i.father_name
        r=i.roll_no
        b=i.branch
        g=i.gender
        c=i.contact_number
        pv=i.purpose_of_visit
        d=i.date
        en=i.entry_time
        ex=i.exit_time


    p.setFont("Helvetica",21)
    p.setFillColor("green")
    p.drawCentredString(300,800,"PANIPAT INSTITUTE OF ENGINEERING & TECHNOLOGY")
    p.setFont("Helvetica",45)
    p.setFillColor("black")
    p.drawCentredString(230, 750, "GATE PASS")

    p.setFont("Helvetica", 30)
    p.setFillColor("black")
    p.drawCentredString(150,680,'Name :-')
    p.setFont("Helvetica", 30)
    p.setFillColor("blue")
    p.drawCentredString(270, 680,f)

    p.setFont("Helvetica", 30)
    p.setFillColor("black")
    p.drawCentredString(200, 610, 'Father Name :-')
    p.setFont("Helvetica", 30)
    p.setFillColor("blue")
    p.drawCentredString(370, 610, ff)

    p.setFont("Helvetica", 30)
    p.setFillColor("black")
    p.drawCentredString(195, 540, 'Roll Number :-')
    p.setFont("Helvetica", 30)
    p.setFillColor("blue")
    p.drawCentredString(364, 540, str(r))

    p.setFont("Helvetica", 30)
    p.setFillColor("black")
    p.drawCentredString(162, 470, 'Branch :-')
    p.setFont("Helvetica", 30)
    p.setFillColor("blue")
    p.drawCentredString(280, 470, b)

    p.setFont("Helvetica", 30)
    p.setFillColor("black")
    p.drawCentredString(163, 400, 'Gender :-')
    p.setFont("Helvetica", 30)
    p.setFillColor("blue")
    p.drawCentredString(330, 400, g)

    p.setFont("Helvetica", 30)
    p.setFillColor("black")
    p.drawCentredString(183, 330, 'Mob. No. :-')
    p.setFont("Helvetica", 30)
    p.setFillColor("blue")
    p.drawCentredString(350, 330, str(c))

    p.setFont("Helvetica", 30)
    p.setFillColor("black")
    p.drawCentredString(233, 260, 'Purpose Of Visit :-')
    p.setFont("Helvetica", 30)
    p.setFillColor("blue")
    p.drawCentredString(450, 260, pv)

    p.setFont("Helvetica", 30)
    p.setFillColor("black")
    p.drawCentredString(153, 190, 'Date :-')
    p.setFont("Helvetica", 30)
    p.setFillColor("blue")
    p.drawCentredString(300, 190, str(d))

    p.setFont("Helvetica", 30)
    p.setFillColor("black")
    p.drawCentredString(198, 120, 'Entry Time :-')
    p.setFont("Helvetica", 30)
    p.setFillColor("blue")
    p.drawCentredString(345, 120, str(en))

    p.setFont("Helvetica", 30)
    p.setFillColor("black")
    p.drawCentredString(190, 50, 'Exit Time :-')
    p.setFont("Helvetica", 30)
    p.setFillColor("blue")
    p.drawCentredString(330, 50, str(ex))

    p.showPage()
    p.save()
    return response