
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
print("""1.Garlic bread🍞            Rs.250
2.Vanilla icecream🍨        Rs.100
3.Pastry🍰                  Rs.150
4.Noodles🍝                 Rs.150
5.Sandwitch🥪               Rs.100
6.Coffee☕                  Rs.100
7.Cheez pizza🍕             Rs.200
8.Chicken biryani sp.🍗     Rs.300
""")
#ask for the order
order=input("What do you want to order?>>>").capitalize()
price=0 
while True:
    if order in menu:
        price += menu[order]
        yn = input("Do you want to order something else? (yes/no):").strip().lower()
        if yn == "yes":
            order = input("Place your next order?>>>").capitalize()
        else:
            break
    else:
        print(f"{order} is not available now!")
        yn = input("Do you want to order something else? (yes/no):").strip().lower()
        if yn == "yes":
            order = input("Place your next order?>>>").capitalize()
        else:
            break

# print(f"Your total bill is Rs.{price}")
# print("THANK YOU FOR ORDERING WITH US!\nHAVE A NICE DAY DEAR CUSTOMER😊!")
      