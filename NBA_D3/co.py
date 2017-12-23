#encoding:utf-8
from flask import Flask, request, render_template, jsonify, send_from_directory
import MySQLdb
import urllib2

app=Flask(__name__)
db = MySQLdb.connect(user='root',db='nbadata',passwd='zxb2011',host='127.0.0.1',charset='utf8')

def con_db():
	cursor = db.cursor()
	return cursor

@app.route('/', methods=["GET"])
def index():
    return render_template("zhu.html")

@app.route('/getAll',methods=['GET'])
def getAll():
    cursor = con_db()
    cursor.execute("SELECT Player,INP,TOV,S,EV,IM from nba_min")
    Data = cursor.fetchall()
    return jsonify(Data)

@app.route('/get/<title>/<year>',methods=['GET'])
def get(title,year):
    cursor = con_db()
    cursor.execute("SELECT * from nba_min where Y='%s'"%year+" order by %s asc limit 10"%title)
    Data = cursor.fetchall()
    return jsonify(Data)

@app.route('/getTowPlayerData/<name>/<year>',methods=['GET'])
def getTowPlayerData(name,year):
    cursor = con_db()
    cursor.execute("SELECT * from nba_min where Player='%s'"%name+" and Y='%s'"%year)
    Data = cursor.fetchone()
    return jsonify(Data)

@app.route('/getHead',methods=['GET'])
def getHead():
    cursor = con_db()
    cursor.execute("select COLUMN_NAME from information_schema.COLUMNS where table_name ='nba_min'")
    Data = cursor.fetchall()
    return jsonify(Data)

@app.route("/test/<id>")
def test(id):
    response = urllib2.urlopen("http://www.stat-nba.com/image/playerImage/"+id+".jpg")  # 传入一个URL,协议是HTTP协议
    data=response.read()
    return data


if __name__ == "__main__":
    app.run(debug=True)