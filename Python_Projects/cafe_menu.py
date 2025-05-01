
#creating a dictionary
menu={
      "Garlic bread":250,
      "Vanilla icecream":100,
      "Pastry":150,
      "Noodles":150,
      "Sandwitch":100,
      "Coffee":100,
      "Cheez pizza":200,
      "Chicken biryani sp.":300
 }
#print the menu, the list of food
print('\n'"**OUR MENU**"'\n')
print("1.Garlic bread🍞            Rs.250\n2.Vanilla icecream🍨        Rs.100\n3.Pastry🍰                  Rs.150\n4.Noodles🍝                 Rs.150\n5.Sandwitch🥪               Rs.100\n6.Coffee☕                  Rs.100\n7.Cheez pizza🍕             Rs.200\n8.Chicken biryani sp.🍗     Rs.300"'\n')
#ask for the order
order=input("What do you want to order?>>>")
order_item=0 
if order in menu:
     order_item+=menu[order] 
     #print("Your total bill is",order_item)
     yn=input("Do you want to order something as? (yes/no):") 
     for i in range(20):
         if yn in "yes":
            order=input("Place your next order?>>>")
            if order in menu:
              order_item+=menu[order] 
              #print("Your total bill is",order_item)
              #a=input("Do you want to order something as? (yes/no):")
            else:
               print(f"{order} is not available now!")  
            a=input("Do you want to order something as? (yes/no):")
            if a in "no":
                break
            

else:
     print(f"{order} is not available now!")
     yn=input("Do you want to order something as? (yes/no):") 
     for i in range(20):
         if yn in "yes":
            order=input("Place your next order?>>>")
            if order in menu:
              order_item+=menu[order] 
              #print("Your total bill is",order_item)
              #a=input("Do you want to order something as? (yes/no):")
            else:
               print(f"{order} is not available now!")  
            a=input("Do you want to order something as? (yes/no):")
            if a in "no":
                break
     
print('\n'"Your total bill is",order_item)
print("THANK YOU FOR YOUR ORDER!")