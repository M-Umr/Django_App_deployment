from django.shortcuts import render
from django.http import HttpResponse
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO
import requests


TEMPLATE_DIRS = {
    'os.path.join(BASE_DIR, "templates"),'
}

def index(request):
    num = request.GET
    print(num)
    if len(num) != 0:
        num = list(num.items())
        for i in num:
            num_of_rows = i[1]#This is the number of rows
        print(num_of_rows) 
    else:
        num_of_rows = 0
    """
    This Dataset is cleaned and these are only 5000 rows
    """ 
    if num_of_rows != 0:
        df = pd.read_csv("./Full_stack.csv")
        df = df.head(int(num_of_rows))
        df = df.drop(['Unnamed: 0.1','Unnamed: 0', '_id', 'Error'], axis=1)
        df.Function.nunique() #Number of unique
        unique_function = df.Function.unique() #unique values in an array
        df = df[['time_stamp', 'Function', 'Time']]
        df = df.set_index('time_stamp')

        """
            Visualizing only one chart
        """
        plt.figure(figsize=(18, 25))
        plt.subplots_adjust(hspace=1)
        plt.suptitle("BigData Visualization", fontsize=30, y=0.8)

        # set number of columns (use 3 to demonstrate the change)
        ncols = 4
        # calculate number of rows
        nrows = len(df) // ncols + (len(df) % ncols > 0)

        # add a new subplot iteratively
        ax = plt.subplot(1, 1, 1)
        # filter df and plot ticker on the new subplot axis
        df[df["Function"] == unique_function[0]].plot(ax=ax)
          # chart formatting
        ax.set_title(unique_function[0], fontsize=20)
        ax.set_xlabel('time_stamp', fontsize=20)
        ax.set_ylabel('Time', fontsize=20)

        plt.tight_layout()
        fig  = plt.show()

        # """
        #     Visualizing charts with loop
        #       For some reason loop charts are showing memory buffer out of range error so I am only showing one Graph
        # """
        # plt.switch_backend('TkAgg')
        # plt.figure(figsize=(200, 600))
        # ncols = 2
        # # calculate number of rows
        # nrows = len(df) // ncols + (len(df) % ncols > 0)
        # for n, each_function in enumerate(unique_function):

        #   # add a new subplot iteratively
        #   ax = plt.subplot(nrows, ncols, n + 1)
        #   # filter df and plot ticker on the new subplot axis
        #   df[df["Function"] == each_function].plot(ax=ax)
        #     # chart formatting
        #   ax.set_title(each_function, fontsize=20)
        #   ax.set_xlabel('time_stamp', fontsize=20)
        #   ax.set_ylabel('Time', fontsize=20)
        # #plt.tight_layout()
        # plt.xticks(rotation=45)
        
        
        # fig = plt.show()
        # plt.clf()

        return render(request, "index.html", {"fig":fig})
    else:
        return render(request, "index.html")


