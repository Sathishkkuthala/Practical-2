fh = open("prac 2.txt",'w')
l=int(input("enter length : "))
w=int(input("enter width : "))
area=l*w
perimeter=2*(l+w)
fh.write("area of rectangle is: "+ str(area)+"\n")
fh.write("perimeter of rectangle is: "+ str(perimeter))
fh.close()