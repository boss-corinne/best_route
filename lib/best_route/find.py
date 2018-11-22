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

def read_network(network):
    all_legs = []
    leg = collections.namedtuple('leg', 'startNode endNode distance')
    for line in open(network, 'r'):
        leg.startnode = line.split(' ')[0]
        leg.endnode = line.split(' ')[1]
        leg.distance = line.split(' ')[2]
        all_legs.append(leg)





def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('filename',
                        help='The filename of the network you wish to use')
    parser.add_argument('origin',
                        help='code for origin node')
    parser.add_argument('destination',
                        help='code for destination node')

    args = parser.parse_args()

    route_nodes = find_best_route(parser.filename, parser.origin, parser.destination)
    print(route_nodes)
    # else:
    #     print("I'm afraid there has been a problem, please "
    #           "use 'python env_browser.py --help' to check the arguments you "
    #           "have given me.")


if __name__ == '__main__':
    main()