"""

  DOUBLY LINKED LIST ADT (DLL)
  
"""

# Function to create a node:
# Each node is a dictionary 
def create_node(data):
    
    node={
        "prev":None, # pointer to previous node
        "next":None, # pointer to next node
        "data":data  # data that is stored in the node
    }
    
    return node # node is returned after being created
    

# Function to create an empty doubly linked list
def create_list():
    # Initialize a dictionary to represent the doubly linked list
    current={
        "head":None,      # pointer to the first node in the list
        "tail":None,      # pointer to the last node in the list
        "size": 0         # counter to track the number of nodes in the list
    }

    return current  # return the initialized list structure


# Function to insert a new node at the end of the list
def insertEnd(lst,data):
    
    
    node=create_node(data)
     
    if lst["head"]==None: # if there are no nodes yet, assign head and tail to this new node
        
        lst["head"]=node
        lst["tail"]=node
        
        
    else: # otherwise append after current tail and update the tail pointer
       
        node["prev"]=lst["tail"]
        lst["tail"]["next"]=node
        lst["tail"]=node
        
    lst["size"]+=1 # increment size after insertion




# Function to insert a new node at the start of the list
def insertStart(lst,data):
    
    
    node=create_node(data)
    
    if lst["head"]==None: # if list is empty, new node becomes both head and tail
        
        lst["head"]=node
        lst["tail"]=node
        
        
    else: # otherwise link new node before current head and update head pointer
       
        node["next"]=lst["head"]
        lst["head"]["prev"]=node
        lst["head"]=node
        
    lst["size"]+=1 # increment size after insertion


# Function to insert a new node after a specified target node
def insertMiddle(lst,data,target):
    
    
    if target==lst["tail"]:
        
        insertEnd(lst,data) # insert at end when target is tail
        return
    
    else:    
        
        node=create_node(data)
        
        node["next"]=target["next"] # connect new node to target's successor
        node["prev"]=target # set previous pointer to target
        target["next"]["prev"]=node # update successor to point back to new node
        target["next"]=node # insert new node after target
    
    
    lst["size"]+=1 # update size after insertion
        
    



# Function to delete a node from the list
def delete_node(lst,node):
    
        
    if node==None:
        print("Nothing to delete")
        return
    
    if lst["size"]==1: # if list has one node, clear the list
        lst["head"]=None
        lst["tail"]=None
    
    if node==lst["tail"]: # removing the last node
        
        lst["tail"]=node["prev"]
        lst["tail"]["next"]=None
        
    elif node==lst["head"]: # removing the first node
        
        lst["head"]=node["next"]
        lst["head"]["prev"]=None
        
    else: # removing a node from the middle

        node["prev"]["next"]=node["next"]
        node["next"]["prev"]=node["prev"]
        
    lst["size"]-=1 # decrement size after deletion
    



# Function to traverse the list from head to tail
def traverse(lst):
    
    current=lst["head"]
    
    
    if lst["size"]!=0:
    
        while True:
            
            print(current["data"]) # print current node data
            
            if current==lst["tail"]:
                break
            current=current["next"] # move to next node in forward direction
        

# Function to traverse the list from tail to head
def traverseback(lst):
    
    current=lst["tail"]
    
    if lst["size"]!=0:
    
        while True:
            
            print(current["data"]) # print current node data in reverse order
            
            if current==lst["head"]:
                break
            current=current["prev"] # move to previous node in backward direction
        


# Function to search for a node by key/value
def search(lst,key,value):
    
    current=lst["head"]
    
    if lst["size"]!=0:
    
        while True:
            
            if current["data"][key]==value:
                return current # return node when key/value pair matches
        
            if current==lst["tail"]:
                break
                
            current=current["next"] # move to next node to continue searching
            
    return None




# # create a list and add 3 songs
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



