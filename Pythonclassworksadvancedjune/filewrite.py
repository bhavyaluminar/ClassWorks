#writing content to a text file

f=open('k.txt','w') #if file k.txt already exists it will erase the content and
                    # return its reference to f
                    #else it will create an empty file and return its reference to f.

content="""Lorem Ipsum is simply dummy text of the printing
       and typesetting industry. Lorem Ipsum has been the 
       industry's standard dummy text ever since the 1500s,
       when an unknown printer took a galley of type and 
     scrambled it to make a type specimen book. 
     It has survived not only five centuries, 
     but also the leap into electronic typesetting, 
     remaining essentially unchanged. 
     It was popularised in the 1960s with the release of
     Letraset sheets containing Lorem Ipsum passages, 
     and more recently with desktop publishing software 
     like Aldus PageMaker including versions of Lorem Ipsum"""

f.write(content)


# f.write('hello python')

#f.writelines(list)
# f.writelines(['hello\n','python\n','java'])
