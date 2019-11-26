from flask import Flask, request, jsonify, render_template,redirect, url_for, flash, logging, session
#from werkzeug.utils import secure_filename
from flask_mysqldb import MySQL
import pickle
import os
import os
import sys
import requests
import sys
from flask_ngrok import run_with_ngrok
import nexmo
import smtplib
from datetime import datetime




app = Flask(__name__)
app.debug = True
#app.config.from_pyfile('config.py')
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'hellofriend'
app.config['MYSQL_DB'] = 'summerg'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


@app.route('/')
def home():
    return render_template('front.html')

@app.route('/checkin',methods=['POST'])
def checkin():


    return render_template('checkin.html')
    
    
@app.route('/checkin/submit',methods=['POST'])
def submit_in():

    name1 = request.form['user_name']
    email_v = request.form['email']
    phone = request.form['phone_no']
    email = request.form['host_email']
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    name_h = request.form['host_user_name']
    
    print(dt_string)
    cur = mysql.connection.cursor()
    
    cur.execute("INSERT INTO visitors(name,email,Phone,Check_in,host_name) VALUES(%s,%s,%s,%s,%s)",(name1,email_v,phone,dt_string,name_h))
    mysql.connection.commit()
    cur.close()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('manthankeim7@gmail.com', 'pfvwgdflwgczvugn')
        
    subject = name1 + 'Checked in at ' + dt_string
    body = 'Dear' + name_h + ', ' + name1 + 'information are given below:' + 'Name: ' + name1 + 'Email:id: ' + email_v + 'Phone No: ' + phone + 'Check in time: ' + dt_string + '. Hope you have a great meeting.'
    
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
                    'manthankeim7@gmail.com',
                    email,
                    msg
                    
                    )
    flash("You are now Checked in" , 'success')
    return render_template('postcheckin.html', name12 = name1 + " Successfully Checked in on" + dt_string)



@app.route('/checkout',methods=['POST'])
def checkout():
    cur = mysql.connection.cursor()
    
    vis2= cur.execute("SELECT name from visitors")
    vis = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    
    
    return render_template('checkout.html', visit = vis)
    
    
    
@app.route('/checkout/submit',methods=['POST'])
def submit_out():
    now = datetime.now()
    out_time = now.strftime("%d/%m/%Y %H:%M:%S")
    print(out_time)
    cur = mysql.connection.cursor()
    
    vis2= cur.execute("SELECT name from visitors")
    vis = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    
    out_name = request.form.get("outlist")
    
    return render_template('postcheckout.html', name13 = out_name +  'Successfully checked out on' + out_time )
    


if __name__ == "__main__":
#    app.run(port = 8010, debug=True)
    app.secret_key=b'\xfc\xed6x\x12u\xe3\xf2\x7f07Z\\\xd6\x83\xe3'
    app.run(port=8096)
    
