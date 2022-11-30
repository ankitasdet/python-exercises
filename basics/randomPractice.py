def my_function():
    print("Hello")
my_function()

# arguments
def my_function(xyz):
    print(xyz + 'abc')

my_function("ankita")
my_function("karteek")

def my_function(fname, lname):
  print(fname + "--- " + lname)

my_function("Emil", "Refsnes")

def my_function(*kids):
    print("the youngest child is " + kids[0])
my_function("Emil","tobas","linux")

def my_function(*kids):
    print("my kids names are  " + kids[0], kids[1] ,'and', kids[2])
my_function("Emil","tobas","linux")



