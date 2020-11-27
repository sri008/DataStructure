# Inheritance

######################################################
# Case 1

# class Animal:
#     name = ""
#     category = ""
#
#     def __init__(self, name):
#         self.name = name
#
#     def set_category(self, category):
#         self.category = category
#
# class Turtle(Animal):
#     category="reptile"
#
# class Snake(Animal):
#     category="reptile"
#
# # Compositiom
# class Zoo:
#     def __init__(self):
#         self.current_animals = {}
#
#     def add_animal(self, animal):
#         self.current_animals[animal.name] = animal.category
#
#     def total_of_category(self, category):
#         result = 0
#         for animal in self.current_animals.values():
#             if animal == category:
#                 result += 1
#         return result
#
#
# zoo = Zoo()
# turtle = Turtle("Turtle") #create an instance of the Turtle class
# snake = Snake("Snake") #create an instance of the Snake class
#
# zoo.add_animal(turtle)
# zoo.add_animal(snake)
#
# print(zoo.total_of_category("reptile")) #how many zoo animal types in the reptile category

######################################################
# Case 2

# we'll create a few classes to simulate a server that's taking connections from the outside and then a load balancer that ensures that there are enough servers to serve those connections.
# To represent the servers that are taking care of the connections, we'll use a Server class. Each connection is represented by an id, that could, for example, be the IP address of the computer connecting to the server. For our simulation, each connection creates a random amount of load in the server, between 1 and 10.

# Begin Portion 1#
import random
class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random() * 10 + 1
        # Add the connection to the dictionary with the calculated load
        self.connections[connection_id]=connection_load

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
        if connection_id in self.connections:
            del self.connections[connection_id]

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        # Add up the load for each of the connections
        for key in self.connections:
            total+=self.connections[key]
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())

# End Portion 1#
# create a Server instance and add a connection to it
# server = Server()
# server.add_connection("192.168.1.1")
#
# print(server.load())  # Output 0
#
# # At this point close_connection method gives output 0
# server.close_connection("192.168.1.1")
# print(server.load())


# Begin Portion 2#
class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        # Add the connection to the dictionary with the selected server
        # Add the connection to the server
        self.connections[connection_id]= server

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        # Find out the right server
        # Close the connection on the server
        # Remove the connection from the load balancer

    def avg_load(self):
        """Calculates the average load of all servers"""
        sum = 0
        for server in self.servers:
            sum += server.load()
        return sum / len(self.servers)
        # Sum the load of each server and divide by the amount of servers

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        pass

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))

# End Portion 2#

l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print(l.avg_load())

l.servers.append(Server())
print(l.avg_load())

for connection in range(20):
    l.add_connection(connection)
print(l)

print(l.avg_load())

######################################################