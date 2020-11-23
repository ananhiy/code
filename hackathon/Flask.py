from flask import Flask,request
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField
import selenium.webdriver as sw
import win32com.client as w
import webbrowser
app=Flask(__name__)
@app.route('/')
def mainpage():
    return(render_template('mainpage.html'))
@app.route('/why_tripton')
def why_trip():
    return(render_template('why_tripton.html'))
@app.route('/Logged_in_successful')
def login():
    return(render_template('login.html'))
if __name__=="__main__":
    app.run(debug=True,use_reloader=False)
