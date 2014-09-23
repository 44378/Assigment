#Jack Scaife
#23/09/2014
#Spot Check 1

pool_w = int(input("Please insert the width of the pool in integer form : "))
pool_l = int(input("Please insert the length of the pool in integer form : "))
pool_d = int(input("Please insert the depth of the pool in integer form : "))

rec_vol = pool_l*pool_w*pool_d

circle_r = pool_w/2
circle_a = 3.14 * (circle_r**2)
circle_volume_half = circle_a/2
circle_volume_half2 = circle_volume_half * pool_d

pool_v = rec_vol + circle_volume_half2

print("The overall volume of the pool is {0}".format(pool_v))
