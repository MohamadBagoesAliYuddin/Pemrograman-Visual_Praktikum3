#Nama   : Mohamad Bagoes Ali Yuddin
#Nim    : 20051397048
#Kelas  : 2020 B
#Prodi  : Manajemen Informatika

class Stack(list):
    push = list.append

def modify_stack(symbolString):
    stack=Stack()
    result = []
    for character in symbolString:
        if character != '*':
            stack.push(character)
        else:
            result.append(stack.pop())
    return ''.join(result)
print(modify_stack('EAS*Y*QUE***ST***IO*N***'))
