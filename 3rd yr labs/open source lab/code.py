#file = open("newfile.txt", "w")

#print f.read()

def fun(f):
  
  for line in f:
    s=[]
    line=line.strip("\n")
    s=line.split(" ")
    #str1 = "this is string example....wow!!!"
  # str2 = " <input type="

  # if(line.find(str2)!=-1 ):
  #   print line
    print s[0]

if __name__ == '__main__':
  f=open("file2.txt")
  fun(f)
  f.close()
  
