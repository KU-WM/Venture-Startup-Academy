def solution1(nums):
    return len(nums) / 2 if (len(nums) / 2 < len(set(nums)) ) else len(set(nums))

def solution2(participant, completion):
#     입력 리스트를 알파벳 순으로 정렬합니다.
    participant.sort()
    completion.sort()
    
#     각 리스트를 순서대로 비교하여 차이가 나는 부분을 찾습니다.
    for i in range(len(participant) - 1): 
        if (participant[i] != completion[i]):
#             서로 다른 부분이 나타나면 참가자 명단에서 그 이름을 출력합니다.
            return participant[i]
#         모두 같다면 마지막 참가자가 없는것 임으로 마지막 참가자를 출력합니다.
    return participant[len(participant) - 1]