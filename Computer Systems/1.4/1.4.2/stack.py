# Stack implementation in python, not practical, purly theoretical
stack = []
pointer = -1
CAPACITY = 5

def check_empty():
    if pointer == -1:
        return True
    else:
        return False

def check_full():
    if pointer == CAPACITY - 1:
        return True
    else:
        return False

def push_stack(pointer, item):
    if check_full():
        print("Stack overflow")
    else:
        stack.append(item)
        pointer += 1
        print("pushed item: " + str(item))
    return pointer

def pop_stack(pointer):
    if check_empty():
        print
    else:
        pointer -= 1
        item = stack.pop()
        print("popped item: " + str(item))
        return pointer, item

def view_stack():
    if pointer == -1:
        print("empty")
    else:
        print("stack:")
        for i in range(pointer+1):
            print(stack[i])
            
view_stack()
pointer = push_stack(pointer, 1)
pointer = push_stack(pointer, 1)
pointer = push_stack(pointer, 1)
pointer = push_stack(pointer, 1)
pointer = push_stack(pointer, 1)
pointer = push_stack(pointer, 1)
pointer, item = pop_stack(pointer)
view_stack()
