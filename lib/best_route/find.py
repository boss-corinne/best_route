"""
Python module for finding the shortest route between two given locations

"""
# TODO: Find algorithm for finding ther shortest distance between two points
# TODO: Record source of algorithm in README
# TODO: Get algorithm working locally according to test parameters (implement it)
# TODO: Write some tests (from test cases supplied)
# TODO: Update README instructions accordingly
# TODO: Work out how to submit this entire package to github, and which repo to sumbit it to.

import argparse
import collections
# from collections import OrderedList

import numpy as np


class network():
    def __init__(self, network_args):
        self.origin = network_args.origin
        self.destination = network_args.destination

        self.all_legs = []
        self.all_nodes = []

        leg = collections.namedtuple('leg', 'startNode endNode distance')
        for line in open(network_args.filename, 'r'):
            start = line.split(' ')[0]
            self.all_nodes.append(start)

            end = line.split(' ')[1]
            self.all_nodes.append(end)

            dist = int(line.split(' ')[2])
            newleg = leg(start, end, dist)

            self.all_legs.append(newleg)

        self.unvisited_nodes = set(self.all_nodes)
        self.visited_nodes = []
        self.dist_to_finish = {node: np.inf for node in self.unvisited_nodes}
        self.dist_to_finish[self.origin] = 0


    def find_closest_neighbour(self, current):
        if current != self.origin:
            self.unvisited_nodes.remove(current)
            self.visited_nodes.append(current)

        dist_so_far = self.dist_to_finish[current]
        print('current_node: {}'.format(current))

        # Get a set of neighbours of this node, or exit if a
        # neighbour is the destination node:
        valid_legs = []
        for leg in self.all_legs:
            if leg.startNode == current:
                if leg.endNode == self.destination:
                    self.visited_nodes.append(leg.endNode)
                    return self.visited_nodes
                elif leg.endNode in self.unvisited_nodes:
                    valid_legs.append(leg)

        if len(valid_legs) < 1:
            try:
                # Try again from beginning, missing all nodes tried so far:
                return self.find_closest_neighbour(self.origin)
            except:
                msg = "Looks like that's just not possible, sorry.  " \
                      "Maybe try a different pair of nodes."
                raise ValueError(msg)

        # Cycle through each leg and choose the closest one
        # TODO: Find a better tentative value for shortest_distance
        shortest_distance = np.inf
        for leg in valid_legs:
            this_distance = dist_so_far + leg.distance
            if (this_distance) < shortest_distance:
                best_leg = leg
                shortest_distance = this_distance
                next_node = best_leg.endNode

        self.dist_to_finish[next_node] = shortest_distance

        current_node = next_node
        route = self.find_closest_neighbour(current_node)

        return route


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('filename',
                        help='The filename of the network you wish to use')
    parser.add_argument('origin',
                        help='code for origin node')
    parser.add_argument('destination',
                        help='code for destination node')

    args = parser.parse_args()

    # Create network object using input args:
    route_map = network(args)

    if args.origin not in route_map.all_nodes:
        msg = 'Your start node is not in your requested network.  ' \
              'Please try a different node or network.'
        raise ValueError(msg)
    elif args.destination not in route_map.all_nodes:
        msg = 'Your end node is not in your requested network.  ' \
              'Please try a different node or network.'
        raise ValueError(msg)

    route_nodes = route_map.find_closest_neighbour(args.origin)
    print([node for node in route_nodes])


if __name__ == '__main__':
    main()