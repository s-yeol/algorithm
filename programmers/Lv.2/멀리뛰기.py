'''
효진이가 끝에 도달하는 방법이 몇 가지인지 알아내, 여기에 1234567를 나눈 나머지를 리턴하는 함수??
마지막은 무엇일까

해결
단순하게 순열로 경우의 수를 구하면 나올줄 알았는데
1이나 2를 더하여 n이 나오는 경우의 수를 구해야한다.

그래서 DFS + 메모이제이션 적용 했으나 재귀함수 깊이 초과로
런타임 에러 발생
'''
def solution(n):
    memo = {}
    def dfs(total):
        
        if total in memo:
            return memo[total]
        
        if total == n:
            return 1

        if total > n:
            return 0

        memo[total] = dfs(total + 1) + dfs(total + 2)
        return memo[total]
    
    return dfs(0) % 1234567