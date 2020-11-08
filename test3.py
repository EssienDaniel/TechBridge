"""
given a list [12,24,111,45,25,19,10,134,114,117]
print out the mean of the list in float
print out the mean of the list as an integer
you are to use strictly list functions
print out the median and mode
print out the mean of the first four items in the list
print out the mean of the last 7 items in the list
"""

x = [12,24,111,45,25,19,10,134,114,117]
mean_float = sum(x)/len(x)
mean4 = sum(x[:4])/4
mean7 = sum(x[-7:])/7
print("The mean in float is {}".format(mean_float))
print("The mean in int is {}".format(int(mean_float)))
print("The maximum number is {}".format(max(x)))
print("The minimum number is {}".format(min(x)))
print("mean of the first four is {}".format(mean4))
print("mean of the last seven is {}".format(mean7))