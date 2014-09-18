#Jack Scaife
#18/09/2014
#Denary to Hexidecimal through binary

denary = int(input("Please enter a denary number:"))
binary_string = ""
while denary > 0:
    binary_string=str(denary%2)+binary_string
    denary = denary/2
print("The binary equivalent is : {0} ".format(binary_string))
