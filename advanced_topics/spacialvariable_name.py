import functions_file # we will get hello fromthis file
def fun():
    print("hi", __name__)
    print("welcome")
    
if __name__ == "__main__":
    fun() # if you run from this file you will get main
#if you import this file in other, it will print file name.