import os
from geopy.distance import distance, geodesic, great_circle

class Instance:
    """
    A class used that keeps all the information of the instance

    Attributes:
        name (str): Name of the instance including extension
        nNodes (int): Number of nodes
        nodes (:obj:`list` of :obj:`Nodes`): List of nodes
        distances (:obj:`dict` of :obj:`Nodes`): Dictionary of distances
    """

    def __init__(self):
        self.name = " " # name of the instance
        self.nNodes = 0 # Number of nodes
        self.nodes = []  # List of nodes
        self.distances = {}  # Matrix of distances

    def compute_dist(self, dist_function):
        """
        A method to compute the distances between each pair of nodes

        It uses a dictionary of distance functions.
        The user chooses one function type

        Args:
            dist_function (str): Define the type of distance to be computed
                default
                geodesic

        Attributes:
            functions: (:obj:'dict' of :obj:'Node'): Dictionary of type of distance functions
        """

        def default_dist(coord1, coord2):
            """
            A function to compute the distances between each pair of nodes
            using the default distance type

            Args:
                coord1 (long): latitude
                coord2 (long): longitude

            Returns:
                d (long): distance
            """

            d = distance((node1.lat, node1.long), (node2.lat, node2.long)).m
            return d

        def geodesic_dist(coord1, coord2):
            """
            A function to compute the distances between each pair of nodes
            using the geodesic type

            Args:
                coord1 (long): latitude
                coord2 (long): longitude

            Returns:
                d (long): distance
            """

            d = geodesic((node1.lat, node1.long), (node2.lat, node2.long)).m
            return d

        functions = {
            'default':  default_dist,
            'geodesic': geodesic_dist
        }

        # computes the distance for each pair of nodes
        for node1 in self.nodes:
            for node2 in self.nodes:
                d = functions[dist_function]((node1.lat, node1.long), (node2.lat, node2.long))
                key = (node1.id, node2.id)
                self.distances[key] = d

    def read_dist(self, filename, filepath =os.path.dirname(os.getcwd()) + "/data/"):
        """
            Write code  here to read distances from file
        """


class Node:
    """
    A class used that represent a node or point of demand

    Attributes:
        id (int): Consecutive number that identify the nodes
        lat (int): Latitude
        long (int): Longitude
    """

    def __init__(self, id, lat=0, long=0, demand = 0):
        self.id = id
        self.lat = lat
        self.long = long