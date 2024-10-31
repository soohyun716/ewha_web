from flask import Flask, render_template, request
import sys

application = Flask(__name__)


@application.route("/")
def hello():
  return render_template("index.html") 

@application.route("/ccc")
def view_category():
  return render_template("ccc.html")

@application.route("/letter")
def view_review():
  return render_template("letter.html")

@application.route("/instargram")
def view_mypage():
  return render_template("instargram.html")