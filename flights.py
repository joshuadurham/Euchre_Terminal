
class AirTrafficControl(object):
	# Initialize your object in preparation for computing the shortest paths.
	#
	# @param routes, a list of routes. Each route is a Route struct with:
	# start: a string airport code, like 'JFK'
	# end: a string airport code, like 'LGA'
	# distance: an int distance, like 12
	#
	# A note: routes have direction. Example: a route start 'JFK' to end 'LGA' 
	# does not necessarily imply start 'LGA' to end 'LGA' is valid.
	#
	# @param airports, a list of all unique string airport codes. Example: ['ORD', 'PHL', ...]
	#
    def prepare(self, routes, airports):
        self.adjacencyList = []
        self.airports = []
        self.distances = []
        self.visited = []
        self.sourceRoute = []
        self.destRoute = []
        self.costRoute = []
        self.maxDistance = 0
        for elem in routes:
            if (elem[2] > self.maxDistance):
                self.maxDistance = elem[2]
        for airport in airports:
            self.airports.append(airport)
            self.distances.append(self.maxDistance + 1)
            self.visited.append(False)
        for route in routes:
            self.sourceRoute.append(route[0])
            self.destRoute.append(route[1])
            self.costRoute.append(route[2])

	# Computes the shortest path and distance between each source airport and destination
	# airport. For the purposes of this problem, a path is a sequence of airport codes where
	# each pair of airport codes has a route from start to end. In other words, the path 
	# ['JFK', 'PHL', 'LGA'] is valid if there are routes 'JFK' -> 'PHL' and 'PHL' -> 'LGA'.
	#
	# @param source_airports: a list of string airport codes for each source. Example: ['ORD', 'PHL']
	# @param destination_airport: a string airport code for the destination. Example: 'LGA'
	#
	# @return a list of distances. Return 1 distance for each valid route between a source airport and destination
	#
	# If there is no valid path (the destination is not reachable from the source), skip the path
	#
	# For an end to end example, consider the source airports ['JFK', 'ORD', 'AAA'] and destination 'LGA',
	# and also consider that 'AAA' does not have a valid path to 'LGA'.
	# This function might return something like:
	# [ 
	#   10, // The distance of the path ['JFK', 'LGA']
	#   123 // The distance of the path ['ORD', 'LGA']
	# ]
    def shortest_paths(self, source_airports, destination_airport):
        result = []
        destinationIdx = self.airports.index(destination_airport)
        for sourceAirport in source_airports:
            sourceIdx = self.airports.index(sourceAirport)
            currentNode = sourceIdx
            self.distances[currentNode] = 0
            while(True):
                neighbors = []
                print(currentNode)
                print(self.airports[currentNode])
                distanceToNeighbors = []
                for i in range(len(self.sourceRoute)):
                    if (self.sourceRoute[i] == self.airports[currentNode]):
                        neighbors.append(self.destRoute[i])
                        distanceToNeighbors.append(self.costRoute[i])
                
                for i in range(len(neighbors)):
                    airportIdx = self.airports.index(neighbors[i])
                    if(self.distances[currentNode] + distanceToNeighbors[i] < self.distances[airportIdx]):
                        self.distances[airportIdx] = self.distances[currentNode] + distanceToNeighbors[i]

                self.visited[currentNode] = True
                if(self.visited[destinationIdx] == True):
                    result.append(self.distances[destinationIdx])
                    break
                indicesOfUnvisited = []
                shortestDistanceIdx = -1
                shortestDistance = self.maxDistance + 1
                for i in range(len(self.visited)):
                    if(self.visited[i] == False):
                        indicesOfUnvisited.append(i)
                        if(self.distances[i] < shortestDistance):
                            shortestDistance = self.distances[airportIdx]
                            shortestDistanceIdx = airportIdx
                someLessThanInfty = False
                for idx in indicesOfUnvisited:
                    if(self.distances[idx] < self.maxDistance + 1):
                        someLessThanInfty = True
                        break
                if(not someLessThanInfty):
                    break
                if(len(neighbors) == 0):
                    break
                currentNode = shortestDistanceIdx
            for i in range(len(self.distances)):
                self.distances[i] = self.maxDistance
                self.visited[i] = False
        print(result)
        return result


controller = AirTrafficControl()
controller.prepare([('A','C',2),('D','A',1),('D','C',3),('E','C',4),('C','E',5),('C','B',6),('F','B',7),('E','F',8),('B','F',9)], ['A','B','C','D','E','F','G'])

# Test the shortest path on a known route
JFK_to_LGA = controller.shortest_paths(['A','B','C','D','E','F'], "F")