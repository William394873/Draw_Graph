import numpy as np
import matplotlib.pyplot as plt
import sys
from os import walk
from matplotlib_venn import venn2, venn3, venn3_circles
import random


def main():
    """
    argv[1]: path to data, argv[2]: 'line' or 'cdf' or 'venn'
    :return:
    """
    data_path = sys.argv[1]
    graph_option = sys.argv[2]
    graph_type = data_path.split('./data/')[1]
    config_dict = set_configuration(graph_type)
    file_path = get_file(data_path)
    if graph_option == 'line':
        draw_line_chart(file_path, data_path, config_dict)
    elif graph_option == 'cdf':
        draw_cdf_chart( file_path, data_path, config_dict )
    elif graph_option == 'venn':
        draw_venn_chart(file_path, data_path, config_dict)

def draw_venn_chart(file_path, data_path, config_dict):

    for index, file in enumerate( file_path ):
        with open(data_path + '/' + file) as f:
            lines = f.readlines()
        data = [int(i.strip("\n")) for i in lines]
        venn2( data, (config_dict['group1'], config_dict['group2']) )
        plt.savefig( "./result/" + config_dict['save_to_' + str(index)] + ".eps", format='eps' )
        plt.show()


def draw_cdf_chart(file_path, data_path, config_dict):
    line_style = get_line_style(len(file_path))
    for index, file in enumerate(file_path):
        with open(data_path + '/' + file) as f:
            lines = f.readlines()
        data_set = lines[0][1:-1].split(", ")
        axis_x = [float(i) for i in data_set]
        axis_x.sort()
        axis_y = [i/(len(axis_x)-1) *100 for i in range(len(axis_x))]
        plt.plot(axis_x,axis_y,label=file.split('.')[0], dashes=line_style[index])
        plt.ylim( ymin=0 )
        plt.xlim( xmin=0)
    # plt.title(config_dict['graph_name'])
    plt.xlabel(config_dict['axis_x'], fontsize=16)
    plt.ylabel(config_dict['axis_y'], fontsize=16)
    plt.legend(loc=config_dict['legend'])
    plt.grid()
    plt.savefig( "./result/" + config_dict['save_to'] + ".eps", format='eps' )
    plt.show()


def draw_line_chart(file_path, data_path, config_dict):
    line_style = get_line_style(len(file_path))
    for index, file in enumerate(file_path):
        with open(data_path + '/' + file) as f:
            lines = f.readlines()
        axis_x = []
        axis_y = []
        based_value = float(lines[1].split(" ")[2].strip("\n"))
        for key, value in enumerate(lines[1:]):
            datalist = value.split(" ")
            axis_y.append(float(datalist[1]))
            axis_x.append(float(datalist[2].strip("\n")) - based_value)
        plt.plot( axis_x, axis_y, label=file.split('.')[0], dashes=line_style[index])
    # plt.title(config_dict['graph_name'])
    plt.xlabel(config_dict['axis_x'], fontsize=16)
    plt.ylabel(config_dict['axis_y'], fontsize=16)
    plt.legend(loc=config_dict['legend'])
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
        if config.strip('\n') == '//' + graph_type:
            flag = 1
            continue
        elif config[:2] == '//':
            flag = 0
            continue
        elif flag == 0:
            continue
        key, value = config.strip("\n").split(" = ")
        config_dict[key] = value
    return config_dict

def get_line_style(line_num):
    """
    line_num line style
    :return:
    """
    # line1.set_dashes([2, 2, 10, 2])  # 2pt line, 2pt break, 10pt line, 2pt break

    style = []
    for i in range(line_num):
        tmp = []
        for j in range(4):
            tmp.append(random.randint(1,10))
        style.append(tmp)
    return style
    # return [(5,2),(2,2),(4,6),(3,3,2,2),(5,2,20,2)]

def get_file(data_path):
    """
    get file in data folder
    :param data_path:
    :return:
    """
    file_path = []
    for (dirpath, dirnames, filenames) in walk(data_path):
        filenames = [i for i in filenames if not i.startswith(".")]
        file_path += filenames
    return file_path


if __name__ == "__main__":
    main()