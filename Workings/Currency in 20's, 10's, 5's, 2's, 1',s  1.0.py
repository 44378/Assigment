#Jack Scaife
#19/09/2014
#Conversion £20, £10 ect 1

currency_1 = int(input("Please enter a whole number of currency :£"))
c_twenty = currency_1 % 20
c_twenty1 = currency_1 //20
c_ten = c_twenty % 10
c_ten1 = c_twenty //10
c_five = c_ten % 5
c_five1 = c_ten //5
c_two = c_five % 2
c_two1 = c_five //2
c_one = c_two % 1
c_one1 = c_two //1

print("This can be made by : {0} £20's, {1} £10's, {2} £5's, {3} £2's and {4} £1's".format(c_twenty1,c_ten1,c_five1,c_two1,c_one1))
