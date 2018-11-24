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


def find_closest_neighbour(current_node, all_legs):
    shortest_dist = np.inf
    print('current_node: {}'.format(current_node))
    # print('all_legs: {}'.format(all_legs))

    relevant_legs = []
    for leg in all_legs:
        print('this leg: {}, {}, {}'.format(leg.startNode, leg.endNode, leg.distance))
        # print('leg start node: {}'.format(leg.startNode))
        if leg.startNode == current_node:
            relevant_legs.append(leg)

    # relevant_legs = [leg for leg in all_legs if leg.startNode==current_node]

    print(relevant_legs)


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
    dist_to_finish = {node: 'inf' for node in unvisited_nodes}
    current = args.origin

    # Set distance from startpoint as zero
    dist_to_finish[current] = 0

    find_closest_neighbour(current, all_legs)

    # route_nodes = find_best_route(parser.filename, parser.origin, parser.destination)
    # print(route_nodes)

    # else:
    #     print("I'm afraid there has been a problem, please "
    #           "use 'python env_browser.py --help' to check the arguments you "
    #           "have given me.")


if __name__ == '__main__':
    main()