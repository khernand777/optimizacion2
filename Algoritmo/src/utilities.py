! git clone https://github.com/khernand777/optimizacion.git
import sys
import os
sys.path.append('optimizacion')
from optimizacion.Algoritmo.src.entities import Instance, Node

def read_instance(filename, filepath =os.path.dirname(os.getcwd()) + "/data/"):
    """
    Read the data of the instances

    See the template doc file to understand the structure of the file

    Parameters:
        filename (str): name of the file to read including extension
        filepath (str, optional): path to the directory
            default is "data" folder in project env
    """

    # Creates instance object
    instance = Instance()
    f = open(filepath + filename, "r")
    # Read first line -> name
    f1 = f.readline()
    splitted_line = f1.split()
    instance.name = splitted_line[1]
    # Omit second line
    f1 = f.readline()
    # Read third line -> number of nodes
    f1 = f.readline()
    splitted_line = f1.split()
    instance.nNodes = int(splitted_line[1])
    # Omit next line
    f1 = f.readline()
    # Read nodes information
    for i in range(instance.nNodes):
        f1 = f.readline()
        splitted_line = f1.split()
        node = Node(int(splitted_line[0]),
                    float(splitted_line[1]),
                    float(splitted_line[2]))
        instance.nodes.append(node)

    return instance