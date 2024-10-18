def count_digits(n):
    if(-10 <n< 10):
        return 1
    return  1+count_digits(n//10)

def get_max(l1,n,j):
    if(n==len(l1)-1):
        return l1[j]
    if(l1[j]>l1[n+1]):
        return l1[j] and get_max(l1,n+1,j)
    else: j=n
    return get_max(l1,n+1,j+1) # two variables advance together and j is like the max

def count_tag_occurrences(html_code, tag):
    # Base case: if the tag is not found in the HTML code, return 0
    opening_tag = f"<{tag}>"
    closing_tag = f"</{tag}>"
    
    # Find the index of the first occurrence of the opening tag
    open_index = html_code.find(opening_tag)
    
    # If no more opening tags are found, return 0
    if open_index == -1:
        return 0

    # Find the corresponding closing tag after the opening tag
    close_index = html_code.find(closing_tag, open_index + len(opening_tag))

    # Once an opening and closing tag pair is found, count it as 1
    # Then, recursively search the remaining part of the HTML after the closing tag
    return 1 + count_tag_occurrences(html_code[close_index + len(closing_tag):],tag)
html_code = """
<html>
<head>
<title>My Website</title>
</head>
<body>
<h1>Welcome to my website!</h1>
<p>Here you'll find information about me and my hobbies</p>
<h2>Hobbies</h2>
<ul>
<li>Playing guitar</li>
<li>Reading books</li>
<li>Traveling</li>
<li>Writing cool h1 tags</li>
</ul>
</body>
</html>
"""

print ("1.count digits \n 2.find max \n 3.find tag \n exit")
a=int(input("enter a choice: "))
if(a==1):
    n=int(input("enter an int: "))
    print(count_digits(n))
elif(a==2):
     a=(int(input(" enter a nb to the list: ")))  # i dont know how to let the user insert a list so i did this
     c=[]
     if(a<0):
       a=int(input("invalid input, add a positive integer: "))
     else: c.append(a)
     while (a>0):
          c.append(a)
          a=int(input(" enter another nb to the list, enter 0 or a negative nb to stop: "))
     print(get_max(c,0,0))
elif(a==3):
    n=input("enter tag: ")
    print(count_tag_occurrences(html_code,n))
else: quit


    
    

    
