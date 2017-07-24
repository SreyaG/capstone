# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 21:12:14 2017

@author: srghosh
"""
from flask import Flask, render_template, request, redirect
import quandl as qd
import pandas as pd
import numpy as np
from bokeh.charts import Line,output_file, show
from bokeh.embed import components
import scipy

def plot_close(tickr):
    df=pd.read_csv("toflask.csv", sep=',')
    s=df[df['country']==tickr]
    return s

app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/index')
app.var={}
@app.route('/index',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index_working.html')
    else:
        tickr=request.form['countries']
        s=plot_close(tickr)
        print s.player.tolist()[0]
        return render_template("index1.html", Ticker=tickr, player1=s.player.tolist()[0],player2=s.player.tolist()[1],
        player3=s.player.tolist()[2],player4=s.player.tolist()[3],player5=s.player.tolist()[4],
        img1=s.image.tolist()[0],img2=s.image.tolist()[1],
        img3=s.image.tolist()[2],img4=s.image.tolist()[3],img5=s.image.tolist()[4])

@app.route('/about',methods=['GET','POST'])
def about():
    if request.method == 'GET':
        return render_template('about.html')
    else:
        tickr=request.form['countries']
        s=plot_close(tickr)
        print s.player.tolist()[0]
        return render_template("index1.html", Ticker=tickr, player1=s.player.tolist()[0],player2=s.player.tolist()[1],
        player3=s.player.tolist()[2],player4=s.player.tolist()[3],player5=s.player.tolist()[4],
        img1=s.image.tolist()[0],img2=s.image.tolist()[1],
        img3=s.image.tolist()[2],img4=s.image.tolist()[3],img5=s.image.tolist()[4])

@app.route('/result',methods=['GET','POST'])
def result():
    if request.method == 'GET':
        return render_template('result.html')
    else:
        tickr=request.form['countries']
        s=plot_close(tickr)
        print s.player.tolist()[0]
        return render_template("index1.html", Ticker=tickr, player1=s.player.tolist()[0],player2=s.player.tolist()[1],
        player3=s.player.tolist()[2],player4=s.player.tolist()[3],player5=s.player.tolist()[4],
        img1=s.image.tolist()[0],img2=s.image.tolist()[1],
        img3=s.image.tolist()[2],img4=s.image.tolist()[3],img5=s.image.tolist()[4])

@app.route('/visualization',methods=['GET','POST'])
def visualization():
    if request.method == 'GET':
        return render_template('visualizations.html')
    else:
        tickr=request.form['countries']
        s=plot_close(tickr)
        print s.player.tolist()[0]
        return render_template("index1.html", Ticker=tickr, player1=s.player.tolist()[0],player2=s.player.tolist()[1],
        player3=s.player.tolist()[2],player4=s.player.tolist()[3],player5=s.player.tolist()[4],
        img1=s.image.tolist()[0],img2=s.image.tolist()[1],
        img3=s.image.tolist()[2],img4=s.image.tolist()[3],img5=s.image.tolist()[4])

@app.route('/future',methods=['GET','POST'])
def future():
    if request.method == 'GET':
        return render_template('future.html')
    else:
        tickr=request.form['countries']
        s=plot_close(tickr)
        print s.player.tolist()[0]
        return render_template("index1.html", Ticker=tickr, player1=s.player.tolist()[0],player2=s.player.tolist()[1],
        player3=s.player.tolist()[2],player4=s.player.tolist()[3],player5=s.player.tolist()[4],
        img1=s.image.tolist()[0],img2=s.image.tolist()[1],
        img3=s.image.tolist()[2],img4=s.image.tolist()[3],img5=s.image.tolist()[4])

if __name__ == '__main__':
    #app.run(port=1234)
  #port = int(os.environ.get("PORT", 5000))
     app.run(host='0.0.0.0', port=5000)
