# Simple Entry Management Software - Innovacer

### Technologies Used:
* Frontend - HTML/CSS
* Backend - Flask
* Database - MySQL
* APIs - SMTP ( Email 📧 , Twillio (SMS) )

### Overall Approach towards the problem

The task was to create a Entry Management Software for visitor.
I made the app very simple and easy to understand, using frontend
of HTML/CSS, which provides two option for visitor, that is to 
Check-in or Check-out. Once the user Checks in there's a simple form
which asks for user details and host information. After storing the 
information in MySQL Database, the host is informed about the visitor
through mail and sms. Once the meeting is over, visitor checks out by 
using the check-out option from the web-app.

For Mailing the host, I've used Simple Mail Transfer Protocol(SMTP),
but in the case of SMS, I've added the code for Twilio API, but due 
to limitation of resources I'm unable to send SMS, but provided with
the resources and the available phone number. This web-app is tested
and can be extended for global user.

I used the name Innovacer just to show that this app is not owned by
any employee of Innovaccer. So I intentionally chose the name Innovacer.
### Project Screenshots on LocalHost

<img alt="image_1" src="working/Screenshot 2019-11-26 at 5.00.21 PM.png" width="700px">

Starting Screen 

<img alt="image_1" src="working/Screenshot 2019-11-26 at 5.01.03 PM.png" width="700px">

Check in information of Visitor and Host

<img alt="image_1" src="working/Screenshot 2019-11-26 at 5.01.12 PM.png" width="700px">

Successfully Checked in 

<img alt="image_1" src="working/Screenshot 2019-11-26 at 5.03.17 PM.png" width="700px">

Check Out who are already checked in 

<img alt="image_1" src="working/Screenshot 2019-11-26 at 5.01.24 PM.png" width="700px">

Successfully Checked out

### Libraries/Dependencies

* flask_mysqldb
* Flask
* flask_ngrok
* smtplib
* datetime
* etc. ( listed in requirements.txt)

### POST NOTE

This is most simple app I could have made using the least resources. Unfortunately, my message credits of Twilio are all spent on previous hackathons, but still I've added the code for the message api. Ofcourse, there are some future scope with the same project I find it very interesting, so I will continue working on it, because of exams I can't focus on the frontend part, but I do commit that I've given my 100% to this project. I'll keep updating the project to increase it's usability.

