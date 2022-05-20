#let -1 be a NULL pointer
tree = [["D",1,2],["B",3,4],["F",5,6],["A",-1,-1],["C",-1,-1],["E",-1,-1],["G",-1,-1]]

def preorder(pointer):
    if pointer != -1:
        print(tree[pointer][0])                 #Visit the node pointed to by p
        preorder(tree[pointer][1])              #recursion for the left side
        preorder(tree[pointer][2])              #recursion for the right side

def postorder(pointer):
    if pointer != -1:
        postorder(tree[pointer][1])             #recursion for the left side
        postorder(tree[pointer][2])             #recursion for the right side
        print(tree[pointer][0])                 #Visit the node pointed to by p
        
def inorder(pointer):
    if pointer != -1:
        inorder(tree[pointer][1])               #recursion for the left side
        print(tree[pointer][0])                 #Visit the node pointed to by p
        inorder(tree[pointer][2])               #recursion for the right side

preorder(0)
postorder(0)
inorder(0)
