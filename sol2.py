def num_complete_rows(n):
    complete_rows = 0
    coins_needed = 0
    
    for i in range(1, n+1):
        coins_needed += i
        if coins_needed > n:
            break
        complete_rows += 1
    
    return complete_rows
n = 5
print(num_complete_rows(n))