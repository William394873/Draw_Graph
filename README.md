# Suzy Graphs

## To get line chart:

(1) python3 draw_graph.py ./data/memory line

(2) python3 draw_graph.py ./data/thread line

## To get CDF:

(1) python3 draw_graph.py ./data/time cdf

## To get Venn:

(1) python3 draw_graph.py ./data/venn_large venn

## To get Bar chart:

(1) python3 draw_graph.py ./data/code_cov_bar bar

## Configure:

graph_name = "name of graph"

axis_x = "name of x axis"

axis_y = "name of y axis"

save_to = "name of output file"

legend = "location of legend, [best or outside]"

## Misc

To change marker frequency, change "markevery" in plt.