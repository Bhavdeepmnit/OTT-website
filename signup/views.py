from django.shortcuts import render, redirect
import mysql.connector as sql
email=''
pwd=''
# Create your views here.
def signaction(request):
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
            c="insert into users (email, password) values('{}','{}')".format(email,pwd)
            cursor.execute(c)
            m.commit()
            return redirect('/login/')
    return render(request, 'signup_page.html')

