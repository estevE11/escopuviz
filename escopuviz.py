import json
from sqlite3 import Timestamp
import matplotlib.pyplot as plt

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
        t_arr.append(time)
    return x_arr, y_arr, z_arr, t_arr

def visualize_single_plt(data):
    plt.plot(data[3], data[0], 'r--', data[3], data[1], 'b--', data[3], data[2], 'g--')
    plt.ylabel('XYZ')
    plt.show()

def visualize_multiple_plt(data):
    plt.figure()
    plt.subplot(221)
    plt.plot(data[3], data[0], 'r--')
    plt.ylabel('X axis')
    plt.subplot(222)
    plt.plot(data[3], data[1], 'b--')
    plt.ylabel('Y axis')
    plt.subplot(223)
    plt.plot(data[3], data[2], 'g--')
    plt.ylabel('Z axis')
    plt.show()

if __name__ == "__main__":
    data = load_json("test.json")
    data = format_data(data, "rotDeg", "yaw", "delta", "pitch")
    visualize_single_plt(data)
    visualize_multiple_plt(data)
