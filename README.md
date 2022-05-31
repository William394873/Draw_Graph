# Suzy Graphs

## To get line chart:

(1) python3 draw_graph.py ./data/memory line

(2) python3 draw_graph.py ./data/thread line

## To get CDF:

(1) python3 draw_graph.py ./data/time cdf

## To get Venn:

(1) python3 draw_graph.py ./data/venn venn

## Configure:

graph_name = "name of graph"

axis_x = "name of x axis"

axis_y = "name of y axis"

save_to = "name of output file"

    for Venn graph, save_to can be save_to_0, save_to_1, ... depending on the number of data in the folder

legend = "location of legend, [best or outside]"