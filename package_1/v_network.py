from .common import commonclassA
import networkx as nx
from matplotlib import pyplot as plt

ca = commonclassA()

class vnetwork:
  
  def __init__(self, snetwork_instance):
    self.snetwork_instance = snetwork_instance #
    G = self.snetwork_instance.G               #creates instance of graph to be used in different module
    adj_list = snetwork_instance.adj_list      #creates instance of adjacency list to be used in different module

  
  def entire_network(self):
    from .s_network import social_network
    sn = social_network()
    G = self.snetwork_instance.G
    nx.draw(G, with_labels = True, node_color = 'yellow') #creates graph
    nx.spectral_layout(G) #changes layout of graph to be spectral
    plt.show() #visualises the graph
 

  def view_users(self):
    adj_list = self.snetwork_instance.adj_list
    G = self.snetwork_instance.G
    if adj_list:
      print("All users in the network:{0}".format(list(G.nodes)))
      choice = str(input("Back to viewing page? 'yes' or 'no':"))
      if choice == 'yes':
        return
      
      elif choice == 'no':
        self.view_users()
      
      else:
        print("   \n***Invalid input***\n")
      

  def view_edges(self):
    adj_list = self.snetwork_instance.adj_list
    G = self.snetwork_instance.G
    if adj_list:
      print("All connections in the network:{0}".format(list(G.edges)))
      choice = str(input("Back to viewing page? 'yes' or 'no':"))
      if choice == 'yes':
        return
      
      elif choice == 'no':
        self.view_users()
      
      else:
        print("   \n***Invalid input***\n")


  def shortest_path(self):
    adj_list = self.snetwork_instance.adj_list
    G = self.snetwork_instance.G

    print("\nAll users in the network:{0}".format(list(G.nodes)))
    user1 = str(input("Enter first user:"))
    if user1 in adj_list:
      user2 = str(input("Enter second user:"))
      if user2 in adj_list:

        path = nx.shortest_path(G,user1 , user2, weight="weight")
        print(path)
        # Create a list of edges in the shortest path
        path_edges = list(zip(path, path[1:]))

        # Create a list of all edges, and assign colors based on whether they are in the shortest path or not
        edge_colors = [
            "red" if edge in path_edges or tuple(reversed(edge)) in path_edges else "black"
            for edge in G.edges()]

        # Visualize the graph
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_edges(G, pos, edge_color=edge_colors)
        nx.draw_networkx_labels(G, pos)
        plt.show()
      else:
        print("{0}, doesnt exist" .format(user2))
        self.shortest_path()
    else:
      print("{0}, doesnt exist" .format(user1))
      self.shortest_path()

  def user_network(self):
    adj_list = self.snetwork_instance.adj_list
    G = self.snetwork_instance.G

    user = str(input("Enter user here to see their conections:"))
    if user in adj_list:
      nx.all_neighbors(G, user)
      nx.draw(G, with_labels = True, node_color = 'yellow')
      plt.show()

    else:
      print("{0}, does not exist" .format(user))
      self.user_network()



