from circular_dlinked_list import Node, CircularDoublyLinkedList

def display(carousel) :
    x = carousel.get_current()
    y = carousel.get_nexts()  # Data of the next node
    a = carousel.get_prevs()  # Data of the prev node
    
     
    display = """
                                 ↓↓
     __________    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|    __________
               |   |                            |   |          
               |   |                            |   |          
     {}        |   |             {}             |   |        {}
               |   |                            |   |          
     __________|   |                            |   |__________
                   |____________________________|
    
    """.format(a,x,y)
    print(display)
    
def single_display(carousel):
    current_data = carousel.get_current()
    x = current_data
    single_display = """

                                 ↓↓
                   |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|    
                   |                            |          
                   |                            |        
                   |            {}              |       
                   |                            |         
                   |                            |  
                   |____________________________|
    
                                 
    """.format(x)
    print(single_display)

def delete(carousel) :
    
    x = carousel.get_current()
    y = carousel.get_nexts()  # Data of the next node
    a = carousel.get_prevs()  # Data of the prev node
    delete = """
                                 /\ 
     __________    |‾‾‾‾‾‾‾‾‾‾‾‾/  \‾‾‾‾‾‾‾‾‾‾‾‾|    __________
               |   |           /    \           |   |                   
               |   |          /_    _\          |   |                   
     {}        |   |            |  |            |   |        {}        
               |   |            |  |            |   |                  
     __________|   |            |  |            |   |__________
                   |____________|  |____________|
                                |__|
    """.format(a,y)
    return (delete)

def initial_delete() :
    
    initial_delete = """
                                 /\ 
                   |‾‾‾‾‾‾‾‾‾‾‾‾/  \‾‾‾‾‾‾‾‾‾‾‾‾|   
                   |           /    \           |                    
                   |          /_    _\          |           
                   |            |  |            |       
                   |            |  |            |                  
                   |            |  |            |   
                   |____________|  |____________|
                                |__|
                                 
    """
    return (initial_delete)

def move_right(carousel) :
    x = carousel.get_current()
    y = carousel.get_nexts()  # Data of the next node
    a = carousel.get_prevs()  # Data of the prev node
    move_right = """
    
                                         |
 __________    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| \     __________
           |   |                         |  \   |                   
           | |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    \  |                   
 {}        | |            Right               | |        {}        
           | |___________________________    /  |                  
 __________|   |                         |  /   |__________
               |_________________________| /
                                         |/
""".format(a,y)
    return (move_right)

def add_right(carousel) :
    x = carousel.get_current()
    y = carousel.get_nexts()  # Data of the next node
    a = carousel.get_prevs()  # Data of the prev node
    add_right = """
    
                                             |
     __________    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| \     __________
               |   |                         |  \   |                   
               | |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    \  |                   
     {}        | |        Adding Right            | |        {}        
               | |___________________________    /  |                  
     __________|   |                         |  /   |__________
                   |_________________________| /
                                             |/
                                 
    """.format(a,y)
    return (add_right)

def add_right_initial() :
    
    add_right_initial = """
    
                                             |
                   |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| \  
                   |                         |  \          
                 |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    \          
                 |        Adding Right            |    
                 |___________________________    /    
                   |                         |  /  
                   |_________________________| /
                                             |/
                                 
    """
    return (add_right_initial)
    
def move_left(carousel) :
    x = carousel.get_current()
    y = carousel.get_nexts()  # Data of the next node
    a = carousel.get_prevs()  # Data of the prev node
    move_left = """
                     /|                      
     __________     / |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|    __________
               |   /  |                         |   |                   
               |  /    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| |                   
     {}        | |              Left              | |        {}        
               |  \    ___________________________| |                  
     __________|   \  |                         |   |__________
                    \ |_________________________|
                     \|                      
    """.format(a,y)
    return (move_left)

def add_left (carousel) :
    x = carousel.get_current()
    y = carousel.get_nexts()  # Data of the next node
    a = carousel.get_prevs()  # Data of the prev node
    add_left = """
                     /|                      
     __________     / |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|    __________
               |   /  |                         |   |                   
               |  /    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| |                   
     {}        | |           Adding Left          | |        {}        
               |  \    ___________________________| |                  
     __________|   \  |                         |   |__________
                    \ |_________________________|
                     \|                      
                                 
    """.format(a,y)
    return (add_left)

def add_left_initial() :
    
    add_left_initial = """
                     /|                      
                    / |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|   
                   /  |                         |          
                  /    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|      
                 |           Adding Left          |       
                  \    ___________________________|             
                   \  |                         |   
                    \ |_________________________|
                     \|                      
                                 
    """
    
    return (add_left_initial)
def initial_add() :
    
    initial_add = """
                                |‾‾|
                   |‾‾‾‾‾‾‾‾‾‾‾‾|  |‾‾‾‾‾‾‾‾‾‾‾‾|   
                   |            |  |            |                   
                   |            |  |            |                    
                   |           _|  |_           |   
                   |          \      /          |                
                   |           \    /           |   
                   |____________\  /____________|
                                 \/
                                
    """
    return initial_add

