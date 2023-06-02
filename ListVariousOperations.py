
N = int(input())
list = []
for i in range(N):
    cmd = input().split()
    for i in range(1,len(cmd)):
        cmd[i] = int(cmd[i])
            
    if cmd[0]=='insert':
        list.insert(cmd[1],cmd[2])
    elif cmd[0]=='print':
        print(list)
    elif cmd[0]=='remove':
        list.remove(cmd[1])
    elif cmd[0]=='append':
        list.append(cmd[1])
    elif cmd[0]=='sort':
        list.sort()
    elif cmd[0]=='pop':
        list.pop()
    elif cmd[0]=='reverse':
        list.reverse()
          
            
                
         