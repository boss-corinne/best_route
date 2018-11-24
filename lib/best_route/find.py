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

import numpy as np


def read_network(network):
    # all_legs is a list of named tuples (legs)
    all_legs = []
    # all_nodes is a list of every single start and end node
    all_nodes = []
    # leg is a named tuple with all info for each leg
    leg = collections.namedtuple('leg', 'startNode endNode distance')
    for line in open(network, 'r'):
        start = line.split(' ')[0]
        all_nodes.append(start)

        end = line.split(' ')[1]
        all_nodes.append(end)

        dist = int(line.split(' ')[2])
        newleg = leg(start, end, dist)

        all_legs.append(newleg)

    return all_legs, all_nodes


def find_closest_neighbour(nodes_and_distances, current_node, all_legs, unvisited, visited):
    dist_so_far = nodes_and_distances[current_node]
    print('current_node: {}'.format(current_node))

    # Get a set of neighbours of this node:
    valid_legs = []
    for leg in all_legs:
        if leg.startNode == current_node and leg.endNode in unvisited:
            valid_legs.append(leg)
        else:
            # TODO: What does this imply?
            pass

    # Cycle through each leg and choose the closest one
    shortest_distance = np.inf
    for leg in valid_legs:
        this_distance = dist_so_far + leg.distance
        if (this_distance) < shortest_distance:
            best_leg = leg
            shortest_distance = this_distance
            next_node = best_leg.endNode

    nodes_and_distances[next_node] = shortest_distance

    print(shortest_distance)
    print(best_leg)
    print(nodes_and_distances[next_node])

    unvisited.remove(current_node)
    visited.append(current_node)

    return next_node


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('filename',
                        help='The filename of the network you wish to use')
    parser.add_argument('origin',
                        help='code for origin node')
    parser.add_argument('destination',
                        help='code for destination node')

    args = parser.parse_args()

    # Create collections of nodes and legs and stuff
    all_legs, all_nodes = read_network(args.filename)
    if args.origin not in all_nodes:
        msg = 'Your start node is not in your requested network.  ' \
              'Please try a different node or network.'
        raise ValueError(msg)
    elif args.destination not in all_nodes:
        msg = 'Your end node is not in your requested network.  ' \
              'Please try a different node or network.'
        raise ValueError(msg)

    unvisited_nodes = set(all_nodes)
    visited_nodes = set()
    dist_to_finish = {node: np.inf for node in unvisited_nodes}
    current = args.origin

    # Set distance from startpoint as zero
    dist_to_finish[current] = 0

    find_closest_neighbour(dist_to_finish, current, all_legs, unvisited_nodes, visited_nodes)

    # route_nodes = find_best_route(parser.filename, parser.origin, parser.destination)
    # print(route_nodes)

    # else:
    #     print("I'm afraid there has been a problem, please "
    #           "use 'python env_browser.py --help' to check the arguments you "
    #           "have given me.")


if __name__ == '__main__':
    main()