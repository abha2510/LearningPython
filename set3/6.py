from queue import LifoQueue

def stack_operations(operations):
    stack = LifoQueue()
    output = []
    for op in operations:
        if op.startswith('push'):
            _, value = op.split('(')
            value = int(value.rstrip(')'))
            stack.put(value)
        elif op == 'pop()':
            if stack.empty():
                output.append('None')
            else:
                output.append(str(stack.get()))
    print(', '.join(output))

# Example usage
operations = ['push(1)', 'push(2)', 'pop()', 'push(3)', 'pop()', 'pop()']
result = stack_operations(operations)
#print(result)
