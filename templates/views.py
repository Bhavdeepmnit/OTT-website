from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import mysql.connector as sql

# Log in action
def loginaction(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # or wherever
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

# Sign up action
def signaction(request):
    if request.method == "POST":
        # Connect to MySQL
        m = sql.connect(host="localhost", user="root", passwd="sheikha#A93", database="website")
        cursor = m.cursor()

        # Get form data
        email = request.POST['email']
        password = request.POST['password']

        # Insert the data into the 'users' table (now you've created it)
        insert_query = "INSERT INTO users (email, password) VALUES (%s, %s)"
        cursor.execute(insert_query, (email, password))

        # Commit the transaction
        m.commit()

        # Close the connection
        cursor.close()
        m.close()

        # Redirect to login page or wherever you need
        return redirect('login')  # Assuming 'login' is the name of your login view.

    return render(request, 'signup_page.html')