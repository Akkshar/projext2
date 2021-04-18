import statistics
import csv
import plotly.figure_factory as ff
import plotly.express as px
import random
import pandas as pd

from google.colab import files
data_to_load = files.upload()

df = pd.read_csv("temperature.csv")
data = df["temp"].tolist()


mean = statistics.mean(data)
stdev = statistics.stdev(data)

def show_fig():
    figure = ff.create_distplot([data], ["temp"], show_hist = False)
    figure.show()

def random_mean(counter):
    dataset = []
    for i in range(0,100):
        randompick = random.randint(0,len(data))
        value = data[randompick]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def repeat():
    mean_list = []
    for i in range(1,100):
        set_mean = random_mean(30)
        mean_list.append(set_mean)
    show_fig(mean_list)   