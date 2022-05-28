import numpy as np
import matplotlib.pyplot as plt
import sys
from os import walk

def main():
    data_path = sys.argv[1]
    graph_option = sys.argv[2]
    graph_type = data_path.split('./data/')[1]
    config_dict = set_configuration(graph_type)
    file_path = get_file(data_path)
    if graph_option == 'line chart':
        draw_line_chart(file_path, data_path, config_dict)
    elif graph_option == 'cdf':
        draw_cdf_chart( file_path, data_path, config_dict )

def draw_cdf_chart(file_path, data_path, config_dict):
    for file in file_path:
        with open(data_path + '/' + file) as f:
            lines = f.readlines()
        data_set = lines[0][1:-1].split(", ")
        axis_x = [float(i) for i in data_set]
        for i in range(1, len(axis_x)):
            axis_x[i] = axis_x[i] + axis_x[i-1]
        print(axis_x)
        axis_y = [i/(len(axis_x)-1) *100 for i in range(len(axis_x))]
        plt.plot(axis_x,axis_y,label=file.split('.')[0])
        plt.ylim( ymin=0 )
        plt.xlim( xmin=0)
    plt.title(config_dict['graph_name'])
    plt.xlabel(config_dict['axis_x'])
    plt.ylabel(config_dict['axis_y'])
    plt.legend()
    plt.grid()
    plt.savefig( "./result/" + config_dict['save_to'] + ".eps", format='eps' )
    plt.show()


def draw_line_chart(file_path, data_path, config_dict):
    for file in file_path:
        with open(data_path + '/' + file) as f:
            lines = f.readlines()
        axis_x = []
        axis_y = []
        based_value = float(lines[1].split(" ")[2].strip("\n"))
        for key, value in enumerate(lines[1:]):
            datalist = value.split(" ")
            axis_y.append(float(datalist[1]))
            axis_x.append(float(datalist[2].strip("\n")) - based_value)
        plt.plot( axis_x, axis_y, label=file.split('.')[0])
    plt.title(config_dict['graph_name'])
    plt.xlabel(config_dict['axis_x'])
    plt.ylabel(config_dict['axis_y'])
    plt.legend()
    plt.grid()
    plt.savefig( "./result/" + config_dict['save_to'] + ".eps", format='eps' )
    plt.show()


def set_configuration(graph_type):
    """
    set configuration for graph within configure.txt
    :return:
    """
    config_dict = {}
    with open("./configure.txt") as f:
        lines = f.readlines()
    flag = 0
    for config in lines:
        if flag == '//' + graph_type:
            flag = 1
            continue
        if config[:2] == '//':
            flag = 0
            continue
        key, value = config.strip("\n").split(" = ")
        config_dict[key] = value
    return config_dict

def get_file(data_path):
    """
    get file in data folder
    :param data_path:
    :return:
    """
    file_path = []
    for (dirpath, dirnames, filenames) in walk(data_path):
        file_path += filenames
    return file_path


if __name__ == "__main__":
    main()