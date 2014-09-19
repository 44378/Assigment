#Jack Scaife
#16/09/2014
#Garden area and costs

length = float(input("Please enter the length of your garden in metres"))
width = float(input("Please enter the width of your garden in metres"))

area1 = length*width
length2 = length-1
width2 = width-1
area_inner = length2*width2

cost_inner = area_inner*10

print("The area of your garden in total is {0} metres squared, the cost of turfing this area with a 1 metre internal border is {1}".format(area1,cost_inner))
