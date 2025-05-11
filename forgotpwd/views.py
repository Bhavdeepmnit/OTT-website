from django.shortcuts import render
import mysql.connector as sql
email=''
curr_pwd=''
new_pwd=''
# Create your views here.
def forgotaction(request):
    global email, curr_pwd, new_pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="sheikha#A93",database='website')
        cursor=m.cursor()
        d=request.POST
        for key, value in d.items():
            if key=="email":
                email=value
            if key=="curr_password":
                curr_pwd=value
            if key=="new_password":
                new_pwd=value
        
        c="select * from users where email='{}' and password='{}'".format(email,curr_pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            redirect('/forgotpwd/')
        else:
            c="update users set password='{}' where email='{}'".format(new_pwd, email)
            cursor.execute(c)
            m.commit()
            return redirect('/login/')
    return render(request, 'forgotpwd.html')
