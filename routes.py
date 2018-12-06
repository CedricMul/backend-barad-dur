"""
Graph search to find shortest path between two cities.

A road map is represented as a directed graph.
Edges represent road segments and are labeled with distances.
Nodes represent cities.
We use depth first search to find the shortest distance
between two cities. During the depth-first search from
start to end, we compute a 'shortest known distance to here from start'
attribute for each node.  After completion of depth first search,
destination city should be labeled with the shortest distance from
the start city.
"""
__author__ = "???"

import argparse


def read_distances(map_file):
    """Read a distance table from a named file into a dict
       mapping sources to lists of (destination, distance) pairs.
    Args:
       map_file: A readable text file in which each line either
           begins with #  (indicating a comment line) or is of the form
           from location, to location, distance or time, for example
              Minis Tirith,Cair Andros,5
           indicating one can travel from Minis Tirith to Cair Andros in 5.0 hours.
    Returns:
        Dict in which each entry d[from] is a list [(to, cost), (to, cost), ... ]
        where from is a location name, to is a location name, and cost is time
        or distance as a floating point number.  If x,y,z appears in the input file,
        then we should have both d[x] contains (y,z) and d[y] contains (x,z), i.e.,
        we assume that roads are bi-directional.
    """
    connections = dict()
    raise NotImplementedError("Implement this function")
    return connections


def show_roads(roads):
    """Print roads from dict (for debugging).
       Args:
         roads:  A dict in which
                roads[Chicago] == [("Atlanta", 30.0), ("Austin", 25.0)]
              means that there is a 30.0 mile road from Chicago to Atlanta and a
              25.0 mile road from Chicago to Austin.
       Returns:
            nothing
       Effects:
            Prints a textual representation of the road connections
    """
    for from_place in roads:
        print(from_place + ":")
        for hop in roads[from_place]:
            to_place, dist = hop
            print("\t->" + to_place + " (" + str(dist) + ")")


def dfs(place, dist_so_far, roads, distances):
    """Depth-first search, which may continue from from_place if dist_so_far
        is the shortest distance at which it has yet been reached.
       Args:
          place: Currently searching from here
          dist_so_far:  Distance at which from_place has been reached
              this time (which may not be the shortest path to from_place)
          roads:  dict mapping places to lists of hops of the form (place, hop-distance)
          distances: dict mapping places to the shortest distance at which they
               have been reached so far (up to this time).
    """
    raise NotImplementedError("Implement this function")


def main():
    """
    Main program gets city pair and map file name,
    reports distance or reports lack of connectivity.
    """
    parser = argparse.ArgumentParser(
        description="Find shortest route in road network")
    parser.add_argument('from_place',
                        help="Starting place (quoted if it contains blanks)")
    parser.add_argument('to_place',
                        help="Destination place (quoted if it contains blanks)")
    parser.add_argument('map_file', type=argparse.FileType('r'),
                        help="Name of file containing road connections and distances")
    args = parser.parse_args()
    start_place = args.from_place
    destination = args.to_place
    roads = read_distances(args.map_file)

    if start_place not in roads:
        print("Start place {} is not on the map".format(start_place))
        exit(1)
    if destination not in roads:
        print("Destination {} is not on the map".format(destination))
        exit(1)

    distances = {}

    dfs(
        place=start_place,
        dist_so_far=0.0,
        roads=roads,
        distances=distances
    )

    if destination in distances:
        print("Distance from {} to {} is {}".format(
            start_place, destination, distances[destination]))
    else:
        print("You can't get from {} to {}".format(start_place, destination))


if __name__ == "__main__":
    main()
