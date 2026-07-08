'''
 귤을 크기별로 분류했을 때 서로 다른 종류의 수를 최소화

 count로 각 크기의 귤 갯수를 센 뒤 제일 작은거부터 없애기?
 서로 다른 종류의 수를 구하고 테스트케이스로 상황을 나누기?
 귤의 크기에 대하여 count함수를 쓴다면 어떻게 입력해야하는가?
'''
'''
*해결
카운터 도구를 이용해서 크기에 따른 귤의 갯수를 튜플로 만들고
갯수로 내림차순 정렬해서 갯수가 많은 순서대로 ans가 k를 넘어서면 반복문 종료하여
값을 출력한다.
Counter - 값의 갯수를 튜플로 정리
values - 갯수만 정리
'''
from collections import Counter
def solution(k, tangerine):
    cnt = Counter(tangerine)
    sort_cnt = sorted(cnt.values(),reverse=True)
    ans = 0
    i = 0
    while(k > ans):
        ans += sort_cnt[i]
        i += 1
    return i
