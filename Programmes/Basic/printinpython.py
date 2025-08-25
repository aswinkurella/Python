"""You are given two variables, a and b. Your task is to print these variables in the following formats:
With space: Print a and b in a single line, separated by a space, followed by a newline.
Without newline: Print a and b separated by a space, but do not end the output with a newline.
With separator: Print a and b separated by a specified separator, followed by a newline.
Without space: Print a and b in a single line, with no spaces between them, followed by a newline. """
#sep is a new keyword we will use 
#end is a new keyword 
a = input()
b = input()
c = input()
print(a,b,sep=" ")
print(a,b, end="")
print(a,b,sep=c)
print(a,b,sep="")