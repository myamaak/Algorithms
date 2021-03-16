def solution(number, k):
    answer = ''

    stack = []
    
    for (ind, num) in enumerate(number):
        
        while stack and k>0 and stack[-1] < num:
            stack.pop() #더 작은 숫자는 스택에서 빼버린다
            k-=1 #뺄 수 있는 숫자를 -1 
            
        if k == 0 : #굳이 해당 조건을 넣어주지 않아도 되지만 더 계산이 빨라진다.
            stack+=number[ind:]
            break
            
        stack.append(num)
    
    if k>0: #제거할 수가 아직 남은 경우 #스택에 담긴 수가 비교되는 수보다 같거나 큰 경우
        stack = stack[:-k] 
        #순차적으로 큰 값이 담겨있을 경우에만 해당 조건문이 성립하므로 
        #앞에서부터 n개의 숫자로 잘라도 된다.
        
        
    answer = ''.join(stack)
    return answer