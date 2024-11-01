def sum_tup(tup1,tup2):
    if(len(tup1)!=len(tup2)):
        return "error, diff length"
    result=[]
    for i in range(len(tup1)):
        result.append(tup1[i]+tup2[i])
    return tuple(result)
   
def exp_ja(dictionary, filename):
    with open(filename, 'w') as file:
        file.write("{\n")
        items = list(dictionary.items())  
        print(items)
        for i in range(len(items)):
            key, value = items[i] 
            if i < len(items) - 1:
                file.write(f'  "{key}": "{value}",\n')
            else:
                file.write(f'  "{key}": "{value}"\n')
        file.write("}\n")

def imp_ja(filename):
    with open(filename,"r") as file:
        content=file.readlines()
        content.pop(0)
        content.pop(-1)
        result=[]
        for line in content:
                line = line.strip().replace('"', '').replace(',', '')  # Clean the line
                key, value = line.split(": ")  # Split into key and value
                result.append({key: value})  # Append the dictionary
    return result

while True:
    print("1.sum tuples \n 2.export Json \n 3.import Json")
    n=input("enter a choice: ")
    if(n=='1'):
        b=input("enter numbers seperated by commas: ")
        q=b.split(",")
        c=input("enter numbers seperated by commas: ")
        w=c.split(",")
      
        for i in range(len(q)):
            q[i]=int(q[i])
              
        for i in range(len(w)):
            w[i]=int(w[i])
          
        z=tuple(q)
        x=tuple(w)
        print(sum_tup(z,x))
        n=input("enter a choice: ")
    elif(n=='2'):
        dc={}
        while True:
            t=input("enter key or type done to finish: ")
            if(t=="done"):
                break
            value=input("enter value: ")
            dc[t]=value
        filename=input("enter file name : ")
        print(exp_ja(dc,filename)) 
        n=input("enter a choice: ")
    elif(n=='3'):
        s=input("enter filename: ")
        print(imp_ja(s))
        n=input("enter a choice: ")
    elif(n=='4'):
        break
        
'''a. 1/6N+8000N3+24 O(N3)
b. 1/6N3             O(LOGN)
c. 1/6N! +200N4      O(N4)
d. NlogN +1000       O(NLOGN)
e. logN +N           O(N)
f. 1⁄2N(N-1)         O(N2)
g. N2+220NlogN2+3N+9000 O(N2)
h. N!+3N+2N+N3+N2      O(N!)
    '''
