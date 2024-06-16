
def recur(cup_str, k,cases):
    idx = cup_str.find('o')
    if k ==0:
        cases[idx]+=1
    else:
        if idx == 0 or idx == 2:
            recur(".o.", k-1,cases)
        else:
            recur("o..",k-1,cases)
            recur("..o",k-1,cases)

cup_str, k = input().split()
k = int(k)

cases = [0,0,0]
recur(cup_str, k,cases)
ans = cases.index(max(cases))

print(f"#1 {ans}")



# recursion으로 풀면 시간초과가 발생한다. 따라서 다른 방법을 사용해야한다.(규칙을 찾아야한다.)
for test_case in range(1, T + 1):
    cup_str, k = input().split()
    k = int(k)
    if k == 0:
        ans = cup_str.find('o')
    else:
        if k %2 ==0:

            if cup_str == ".o.":
                ans = 1
            else:

                ans = 0
        else:

            if cup_str == ".o.":
                ans = 0
            else:
                ans = 1
    
    #cases = [0,0,0]
    #recur(cup_str, k,cases)
    #ans = cases.index(max(cases))
    
    print(f"#{test_case} {ans}")