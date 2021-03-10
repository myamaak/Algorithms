
# def maximizeProfit(nums):
#     max_prof = 0
#     prev = nums[0]
#     rec =[]
#     for i in range(1,len(nums)):
#         if nums[i] < prev:
#             if max_prof > 0 :
#                 rec.append(max_prof)
#             prev = nums[i]
#             max_prof = 0
#         else:
#             max_prof += (nums[i]-prev)
#             prev = nums[i]
#         rec.append(max_prof)
        
#     if not rec:
#         return max_prof
#     else:
#         return max(rec)
# 일부에서만 정답이 나온다. 아래 방법을 쓰는게 맞음.
# 왜 오답이 나오는지는 고민해봐야 할 것 같다.

def maximizeProfit(nums):
    max_prof = 0
    prev = nums[0]
    
    for i in range(1,len(nums)):
        prof = nums[i]-prev
        if prof > max_prof:
            max_prof = prof
        if nums[i] < prev:
            prev = nums[i]
    return max_prof
    