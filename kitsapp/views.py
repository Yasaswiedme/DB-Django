from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from .models import Student
import mysql.connector
from django.contrib import messages
# Create your views here.
def read(request):
    students=[]
    mydb=mysql.connector.connect(
    host="db.c1eg48sc6wt0.ap-south-1.rds.amazonaws.com",
    user="DB",
    password="Db.1234567",
    database="DB"
    )
    mycursor=mydb.cursor()
    mycursor.execute("select * from ssv")
    myresult=mycursor.fetchall()

    for x in myresult:
        student=Student()
        student.username=x[0]
        student.password=x[1]
        student.gender=x[2]
        student.branch=x[3]
        student.address=x[4]
        students.append(student)
    return render(request,'read.html',{'studentsinfo':students})

def delete(request,uname):
    if request.method == 'POST':
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="myrce"
        )
        mycursor = mydb.cursor()
        # Assuming you're passing the ID of the record you want to delete via POST
        uname = request.POST.get('username')
        # Execute SQL query to delete the record with the given ID
        mycursor.execute("DELETE FROM ssv WHERE username = %s", (uname,))
        mydb.commit()
        return redirect('read')  # Redirect to the read function after deletion
    else:
        return render(request, 'delete.html')


def add_student(request):
    if(request.method=='POST'):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="myrce"
        )
        mycursor = mydb.cursor()       
        uname=request.POST['username']
        pwd=request.POST['pwd']
        gender=request.POST['gender']
        branch=request.POST['branch']
        address=request.POST['address']        
        mycursor.execute("insert into reg(username,password,gender,branch,address) VALUES('"+uname+"','"+pwd+"','"+gender+"','"+branch+"','"+address+"')")
        mydb.commit()    
        return redirect('read')
    else:
        return render(request,'add_student.html')

def editstudent(request,uname):
    if(request.method=='POST'):
        con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="myrce"
        )
        newcur=con.cursor()
        uname=request.POST['username']
        pwd=request.POST['pwd']
        gender=request.POST['gender']
        branch=request.POST['branch']
        address=request.POST['address']
        newcur.execute("update reg set username='"+uname+"',password='"+pwd+"',gender='"+gender+"',branch='"+branch+"',address='"+address+"' where uname='"+str(uname)+"'")
        con.commit()
        return redirect("add_student")
    else:
        return render(request,'editstudent.html')
