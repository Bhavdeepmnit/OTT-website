from django.shortcuts import render
import mysql.connector as sql

name=''
email=''
message=''
# Create your views here.
def feedaction(request):
    global name, email, message
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="sheikha#A93",database='website')
        cursor=m.cursor()
        d=request.POST
        for key, value in d.items():
            if key=="email":
                email=value
            if key=="name":
                name=value
            if key=="message":
                message=value
        c="insert into feedback (name, email, message) values('{}','{}', '{}')".format(name, email, message)
        cursor.execute(c)
        m.commit()
        return render(request, 'feed_submit.html')
    return render(request, 'feedback.html')