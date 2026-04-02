"""

  DOUBLY LINKED LIST ADT (DLL)
  
"""

def create_node(data):
    
    node={
        "prev":None,
        "next":None,
        "artist_prev":None,
        "artist_next":None,
        "data":data   
    }
    
    return node
    
    
    

def create_list():
    
    current={
        "head":None,
        "tail":None,
        "size": 0,
        "artist_head":{},
        "artist_tail": {}
    }

    return current




def insertEnd(lst,data):
    
    
    node=create_node(data)
     
    if lst["head"]==None: #if there are no nodes yet, we will assign head and tail to be the node that's being inserted
        
        lst["head"]=node
        lst["tail"]=node
        
        
    else: #else it advances tail and inserts the node at the end.
       
        node["prev"]=lst["tail"]
        lst["tail"]["next"]=node
        lst["tail"]=node
        
    lst["size"]+=1




def insertStart(lst,data):
    
    
    node=create_node(data)
    
    if lst["head"]==None: #if there are no nodes yet, we will assign head and tail to be the node that's being inserted
        
        lst["head"]=node
        lst["tail"]=node
        
        
    else: #else it advances head and inserts the node at the beginning.
       
        node["next"]=lst["head"]
        lst["head"]["prev"]=node
        lst["head"]=node
        
    lst["size"]+=1




def insertMiddle(lst,data,target):
    
    
    if target==lst["tail"]:
        
        insertEnd(lst,data)
        return
    
    else:    
        
        node=create_node(data)
        
        node["next"]=target["next"]
        node["prev"]=target
        target["next"]["prev"]=node
        target["next"]=node
    
    
    lst["size"]+=1
        
    


def delete_node(lst,node):
    
        
    if node==None:
        
        print("Nothing to delete")
        return
    
    if lst["size"]==1:
        
        lst["head"]=None
        lst["tail"]=None
        lst["size"]-=1
        return #the return is here because it crashes if the list is empty and we go on to check if node==lst["tail"] because now tail has nothing
    
    if node==lst["tail"]:
        
        lst["tail"]=node["prev"]
        lst["tail"]["next"]=None
        
    elif node==lst["head"]:
        
        lst["head"]=node["next"]
        lst["head"]["prev"]=None
        
    else:

        node["prev"]["next"]=node["next"]
        node["next"]["prev"]=node["prev"]
        
    lst["size"]-=1
    



def traverse(lst):
    
    current=lst["head"]
    
    
    if lst["size"]!=0:
    
        while True:
            
            print(current["data"])
            
            if current==lst["tail"]:
                break
            current=current["next"]


        

def traverseback(lst):
    
    current=lst["tail"]
    
    if lst["size"]!=0:
    
        while True:
            
            print(current["data"])
            
            if current==lst["head"]:
                break
            current=current["prev"]
        



def search(lst,key,value):
    
    current=lst["head"]
    
    if lst["size"]!=0:
    
        while True:
            
            if current["data"][key]==value:
                return current
        
            if current==lst["tail"]:
                break
                
            current=current["next"]
            
    return None




# create a list and add 3 songs
# playlist = create_list()
# insertEnd(playlist, {"title": "What lurks in the Forest", "artist": "Akira Yamaoka"})
# insertEnd(playlist, {"title": "In my time of need", "artist": "Opeth"})
# insertEnd(playlist, {"title": "Opiate^2", "artist": "TOOL"})
# insertEnd(playlist, {"title": "Hope Leaves", "artist": "Opeth"})

# # should print A, B, C
# traverse(playlist)

# # should print C, B, A
# traverseback(playlist)

# # should return Song B's node
# result=search(playlist, "artist", "TOOL")

# print(result["data"])

# # delete Song B then traverse, should print A, C
# delete_node(playlist, result)

# result=search(playlist, "artist", "Opeth")
# delete_node(playlist, result)

# traverse(playlist)

# # size should be 2
# print(playlist["size"])


"""

  DOUBLY LINKED LIST ADT (DLL)
  
"""



def merge(arr,left,mid,right,field):
 
    n1=mid-left+1
    n2=right-mid

    L=[0]*n1
    R=[0]*n2

    for i in range(n1):
        L[i]=arr[left+i]
    for j in range(n2):
        R[j]=arr[mid+1+j]
        
    i=0  
    j=0  
    k=left  

    while i<n1 and j<n2:
        if L[i][field]<=R[j][field]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1

    while i<n1:
        arr[k]=L[i]
        i+=1
        k+=1

    while j<n2:
        arr[k]=R[j]
        j+=1
        k+=1
    
def mergeSort(arr,left,right,field):

    if left<right:

        mid=(left+right)//2

        mergeSort(arr,left,mid,field)
        mergeSort(arr,mid+1,right,field)
        merge(arr,left,mid,right,field)
