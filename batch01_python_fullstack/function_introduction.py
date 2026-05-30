# write once use more

# GST 18%

def calculate_gst(amount):
    GST = 18
    total_amount = amount + (amount * GST/100)
    return total_amount

def pie_value():
    return 3.14


def print_pattern(pattern):
    for i in range(10):
        print(pattern,end=" ")

print_pattern("#")

# function with argument with return type
# function without argument without return type
# function with argument without return type
# function without argument with return type


print(calculate_gst(400))

print(calculate_gst(1000))

# [] list  {} dictionary ()  tuple

# Set {}


data = ("Sanjive",45,14,65)

print(data[0])

print(type(data))


print(data)

set = {23,23,34,56,32,11,23}


print(set) # un ordered so you can't access by index


'''
   for(int i=0;i<5;i++){
       
   
   }
'''

for i in set:
    print(i)