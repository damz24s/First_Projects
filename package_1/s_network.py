import networkx as nx
from matplotlib import pyplot as plt
from .common import commonclassB

cb = commonclassB


class social_network:

  def __init__(self, name=None):
    self.name = name
    self.adj_list = {} #adjacency lsit to store all values
    self.G = nx.Graph() #initialising graph


  def add_user(self):
    self.name = str(input("Enter name here or type 'exit' to leave:"))
    if self.name == 'exit':
      return
    #if user enters 'exit', end function

    if self.name in self.adj_list:
      print("\nName already exists pick again")
      self.add_user()
      #if 'self.name' already in adjecancy list, recursively call function
    else:
      self.adj_list[self.name] = []
      self.G.add_node(self.name) #creating a node in 'networkx'
      print("\n***New user added!***")
      #else initialise 'self.name' with a 'list' for values

      xtra_node = str(input("\nAdd another user? 'yes' or 'no':"))
      if xtra_node == 'yes':
        self.add_user()         #if extra node to be added, recursively call function
                                # 
      elif xtra_node == 'no':   #else end function
        return
      
      else:
        print("!!!Invalid Input, try again!!!")
        self.add_user()

  
  def add_connection(self):
    print("Current users in the system:{0}".format(self.adj_list.keys())) 
    name1 = str(input("\nEnter first user to connect or type 'exit' to leave:"))
    if name1 == 'exit':
      return
    #prints out all keys in adjaceny list
    #if user enters 'exit', end function

    if name1 in self.adj_list:
      name2 = str(input("\nEnter second user to connect or type 'exit' to leave:"))
      if name2 == 'exit':
        return
      #if user enters 'exit', end function

      if name2 in self.adj_list:
        if name2 in self.adj_list[name1]:
            if name1 in self.adj_list[name2]:
              print("\n***Connection already exists between {0} and {1}***\n" .format(name1, name2))
              self.add_connection()
            #if name2 is already a value in name1's list vice versa, print the following

        else:
          self.adj_list[name1].append(name2) #adds name2 to name1 list of values
          self.adj_list[name2].append(name1) #adds name1 to name1 list of values
          self.G.add_edge(name1, name2) #creates edge in graph
          print("\n***{0} and {1} are now connected!***\n" .format(name1, name2))

          xtra_edge = str(input("Create another connection? 'yes' or 'no':"))
        
          if xtra_edge == 'yes':
            self.add_connection()

          elif xtra_edge == 'no':
            return
          
          elif xtra_edge not in ['yes', 'no']:
            print("\n***invalid input***\n")
          #allows extra connection to be made if user says yes, else ends function

      else:
        print("{0}, doesnt exist" .format(name2))
        self.add_connection()
    else:
      print("{0}, doesnt exist" .format(name1))
      self.add_connection()

    
  def remove_user(self):
    print("Current users in the system:{0}".format(self.adj_list.keys()))
    name1 = str(input("\nEnter name of user to delete:"))

    if name1 in self.adj_list:   
      del self.adj_list[name1]   #delete name1 as a key
      self.G.remove_node(name1)  #removes name1 as a node from the graph
      print("\n***{0}, has been removed from the network***\n" .format(name1))

      for k in self.adj_list:           #iterates through adjacency list 'keys'
        if name1 in self.adj_list[k]:   #checks if name1 is a value to any of the keys
          self.adj_list[k].remove(name1)#removes name1 as a value
        
      
    else:
      print("\n***{0}, doesnt exist***\n" .format(name1))
      retry = str(input("Would you like to try again? 'yes' or 'no':"))
      if retry == 'yes':
        self.remove_user()

      elif retry == 'no':
        return
      
      elif retry not in ['yes', 'no']:
        print("\n***invalid input***\n")


  def remove_connection(self):
    print("All connections in the network:{0}".format(list(self.G.edges)))#prints out current connections
    name1 = str(input("Enter name of first user:"))
    if name1 in self.adj_list:
      name2 = str(input("Enter name of second user:"))
      if name2 in self.adj_list:
        self.adj_list[name1].remove(name2) #deletes name2 from name1 list of values
        self.adj_list[name2].remove(name1) #deletes name1 from name2 list of values
        self.G.remove_edge(name1, name2)
        print("\n*** Connection between {0} and {1}, successfuly removed ****" .format(name1, name2))
      else:
        print("{0}, does not exist" .format(name2))
    else:
        print("{0}, does not exist" .format(name2))


  def view_network(self):
    from .v_network import vnetwork
    vn = vnetwork(self)
    while True:
      print("\n\n\n          |   NETWORK VIEWING PAGE   |")
      print("            ~~~Choose an option 1-6~~~\n")
      print("1) View entire network")
      print("2) View all users")
      print("3) View all connections")
      print("4) Shortest path between users")
      print("5) Search for specific users")
      print("6) Previous page")
      choice = str(input("Enter choice here:"))

      if choice == '6':
        print("\n   ---Returning to previous page---\n\n\n")
        break
        
      elif choice == '1':
        vn.entire_network()

      elif choice == '2':
        vn.view_users()

      elif choice == '3':
        vn.view_edges()

      elif choice == '4':
        vn.shortest_path()

      elif choice == '5':
        vn.user_network()
      elif choice not in ['1', '2', '3', '4', '5']:
          print("\n---Invalid Input, Try again---")


