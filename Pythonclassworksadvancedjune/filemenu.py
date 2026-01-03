#FILE MENU OPERATIONS

#
# 1.File Write
# 2.File Read
# 3.File Append
# 4.File Search
# 5.File Delete
#
def file_write():
    file_name=input("Enter the filename")
    f=open(file_name,'w')
    content=input("Enter the content")
    f.write(content)
def file_read():
    #try ---except
    try:
        file_name=input("Enter the filename")
        f=open(file_name,'r')
        content=f.read()
        print(content)
    except:
        print("File does not exist")

def file_append():
    file_name=input("Enter the filename")
    f=open(file_name,'a')
    content=input("Enter the content")
    f.write(content)

def file_search():
    file_name=input("Enter the filename")
    f=open(file_name,'r')
    content=f.read()
    word=input("Enter the word to be searched")
    if  word in content:
        print("Word",word,"is present")
    else:
        print("not present")
def file_delete():
    import os
    file_name = input("Enter the filename")
    os.remove(file_name)
    print("file",file_name,"is deleted")
while(1):
    print("File Operations")
    print('1.File Write')
    print('2.File Read')
    print('3.File Append')
    print('4.File Search')
    print('5.File Delete')
    print('6.Exit')

    ch=int(input("Enter the choice"))
    if ch==1:
        file_write()
    elif ch==2:
        file_read()

    elif ch==3:
        file_append()

    elif ch==4:
        file_search()
    elif ch==5:
        file_delete()
    else:
        exit()

