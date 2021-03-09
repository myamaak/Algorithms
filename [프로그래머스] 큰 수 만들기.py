def solution(number, k):
    answer = ''
    max_num = '-1'
    max_ind = 0
    for i in range(k):
        if max_num < number[i]:
            max_num = number[i]
            max_ind = i
    
    stack = []
    left_num = len(number) -k -1
    for i in range(max_ind+1,len(number)):
        # print(stack, number[i], len(number)-i-1, left_num)
        if not stack:
            stack.append(number[i])
            left_num-=1
        else:
            if len(number)-i-1 >= left_num:
                before = stack.pop()
                if before < number[i]:
                    stack.append(number[i])
                else:
                    stack.append(before)
            #테스트 케이스 3번을 위한 코드였는데 잘 안됐다. 이하 코드를 실행하려면
            #if len(number)-i-1 > left_num: 로 두어야 한다
            #위의 코드임...
            # elif len(number)-i-1 == left_num:
            #     if i+1<= len(number)-1:
            #         if number[i] > number[i+1]:
            #             stack.append(number[i])
            #             left_num-=1
            #         else:
            #             before = stack.pop()
            #             if before < number[i]:
            #                 stack.append(number[i])
            #             else:
            #                 stack.append(before) 
            #     else:
            #         before = stack.pop()
            #         if before < number[i]:
            #             stack.append(number[i])
            #         else:
            #             stack.append(before)      
            else:
                stack.append(number[i])
                left_num-=1
        
    answer = max_num+ ''.join(stack)
    return answer