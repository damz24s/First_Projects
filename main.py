from package_1.s_network import social_network
from package_1.v_network import vnetwork


def main():
  sn = social_network()
  vn = vnetwork(sn)
  while True:
    print("\n   |   WELCOME TO THE SOCIAL NETWORK MAIN PAGE   |")
    print("             ~~~Choose an option 1-6~~~\n")
    print("1) Add a user")
    print("2) Add connection between users")
    print("3) Delete a user")
    print("4) Delete connection between users")
    print("5) **Next page (View Network)**")
    print("6) Exit")
    choice = str(input("Enter choice here:"))   
    
    if choice == '6':
        print("\n--Goodbye--")
        break
        
    elif choice == '1':
        sn.add_user()
        
    elif choice == '2':
        sn.add_connection()
        
    elif choice == '3':
        sn.remove_user()
        
    elif choice == '4':
        sn.remove_connection()

    elif choice == '5':
        print("\n    ---Moving to Next page---\n\n")
        sn.view_network()
        
    elif choice not in ['1', '2', '3', '4', '5', '6']:
        print("\n---Invalid Input, Try again---")

main()


