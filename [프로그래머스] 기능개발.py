def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    done = []
    for i in range(n):
        days = 0
        prog = progresses[i]
        speed = speeds[i]
        while prog < 100:
            prog+=speed
            days+=1
        done.append(days)
    
    count = 1
    max_day = done[0]
    to_deploy = 1
    while count < n:
        if max_day < done[count]:
            answer.append(to_deploy)
            to_deploy = 1 
            #이부분에서 약간 헤맸다. 
            #to_deploy를 1이 아니라 0으로 초기화 했기 때문.
            max_day = done[count]
            count+=1
        else:
            count+=1
            to_deploy+=1
    answer.append(to_deploy)
    return answer