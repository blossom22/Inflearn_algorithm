# 배열 & 연결리스트 & 데크
# 문제2_합격생
# 입력의 크기 n이 100,000은 되어야지 시간복잡도를 체크하는 문제이다. 이거보다 작으면 굳이 효율성 따지는 것은 아님
# 그냥 간단하게 순차탐색하면 된다. 
def sol(score, k):
    answer = 0
    for i in score:
        if i>=k:
            answer+=1
    return answer

print(sol([60, 50, 80, 90, 55, 70, 65, 45], 60))
print(sol([10, 20, 30, 40, 50], 60))
print(sol([50, 65, 75, 87, 90, 55, 78, 93, 100], 70))
print(sol([99, 30, 50, 55, 68, 70, 90, 100], 80))