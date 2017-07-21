
import pandas as pd
import numpy as np

import scipy
def plot_close(tickr):
    df=pd.read_csv("toflask.csv", sep=',')
    s=df[df['country']==tickr]
    #score=s.Rating
    #output_notebook()
    #p = Line(y, title="Closing Price/ Day in May",width=500, height=400,xlabel='Dates', ylabel='Closing Price')
    #output_file("templates\closing.html", title="Closing Price in May")
    return s.player.tolist()[0]

print plot_close("United States")
