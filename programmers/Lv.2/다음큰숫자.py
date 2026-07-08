## 풀이 : bin(n).count("1")을 통해 조건에 만족하는 수를 찾기

def solution(n):
    find = bin(n).count("1")
    while(True):
        n += 1
        if bin(n).count("1") == find:
            break
    return n

solution(15)