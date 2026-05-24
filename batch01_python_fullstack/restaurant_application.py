'''
 Wellcome to Thinka AI Hotel
 1. Order
 2. Display menu
 3. exit

foods = ['Dosa,'Idli','Poori','Pongal']
          0     1       2      3
price = [60 , 20,     40 ,   80]

foods[0]  what is dosa price ?
    price[0]
'''
###################################################################

foods = ['Dosa', 'Idli', 'Poori', 'Pongal']
price = [60, 20, 40, 80]
foods_dictionary = {'Dosa': 60, 'Idli': 20, 'Poori': 40, 'Pongal': 80}
option = 0

while option != 3:

    print("***************Wellcome to Thinka AI Hotel*****************")
    option = int(input("1. Order\n3. exit\n"))

    if option == 1:

        isOrder = True
        total_bill = 0
        ordered_foods = {}

        while isOrder:
            print("Available Foods : ")

            for i in foods_dictionary:
                print(i, foods_dictionary[i])

            food = input("Please enter your food : ")

            if food in foods_dictionary:
                quantity = int(input("How much you want ? "))

                ordered_foods[food] = quantity
                total_bill += foods_dictionary[food] * quantity
            else:
                print("Sorry this food Not available !!!")

            condition_yes_or_no = (input("Want to order more ? "))

            if condition_yes_or_no == "yes":
                isOrder = True
            else:
                isOrder = False
                for i in ordered_foods:
                    print(i , ordered_foods[i])
                print("Your total bill is : ", total_bill)







