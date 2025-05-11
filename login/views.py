from django.shortcuts import render, redirect
import mysql.connector as sql
email=''
pwd=''
# Create your views here.
def loginaction(request):
    global email, pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="sheikha#A93",database='website')
        cursor=m.cursor()
        d=request.POST
        for key, value in d.items():
            if key=="email":
                email=value
            if key=="password":
                pwd=value
        
        c="select * from users where email='{}' and password='{}'".format(email,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return redirect('/login/')
        else:
            return redirect('/movies/')
    return render(request, 'login_page.html')
