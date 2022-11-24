import json
import math
from sqlite3 import Timestamp
import matplotlib.pyplot as plt
import numpy


def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def format_data(data, type, axis_x, axis_y, axis_z):
    x_arr = []
    y_arr = []
    z_arr = []
    t_arr = []
    for it in data[type]:
        x_arr.append(it[axis_x])
        y_arr.append(it[axis_y])
        z_arr.append(it[axis_z])
        time = it["timeStamp"]-data[type][0]["timeStamp"]
        #print(time)
        t_arr.append(time)
    return x_arr, y_arr, z_arr, t_arr

def visualize_single_plt(data):
    plt.plot(data[3], data[0], 'r--', data[3], data[1], 'b--')
    plt.ylabel('Yaw "r"/Delta "b"')
    plt.show()

def visualize_multiple_plt(data):
    plt.figure()
    # plt.subplot(221)
    # plt.plot(data[3], data[0], 'r--')
    # plt.ylabel('X axis')
    # plt.subplot(222)
    plt.plot(data[3], data[1], 'b--')
    plt.ylabel('Delta')
    plt.show()

def meanCalc(data):
    firstTime = input("First mean start: ")
    lastTime = input("First mean end: ")        
    delta = data[1]
    first = find_nearest(data[3], firstTime)
    last = find_nearest(data[3], lastTime)
    newDelta = delta[int(first):int(last)]
    mean = numpy.mean(newDelta)
    print("Mean value: ", mean)
    return mean

def finalValue(data):
    print("Calculate mean start: ")
    meanStart = meanCalc(data)
    print("Calculate mean end: ")
    meanEnd = meanCalc(data)
    if(meanStart<0):
        meanFinal = meanEnd - meanStart
    else:
        meanFinal = meanEnd + meanStart
    print("Final value",meanFinal)

def find_nearest(array, value):
    array = numpy.asarray(array)
    idx = (numpy.abs(array - float(value))).argmin()
    return idx

if __name__ == "__main__":
    data = load_json("test.json")
    data = format_data(data, "rotDeg", "yaw", "delta", "pitch")
    #visualize_single_plt(data)
    visualize_multiple_plt(data)
    finalValue(data)
    

