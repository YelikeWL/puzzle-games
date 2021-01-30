'''A school has 100 lockers and 100 students. All lockers are closed on
the first day of school. As the students enter, the first student, denoted S1, opens every 
locker. Then the second student, S2, begins with the second locker, denoted L2, and closes
every other locker. Student S3 begins with the third locker and changes every third locker
(closes it if it was open, and opens it if it was closed). Student S4 begins with locker L4 and
changes every fourth locker. Student S5 starts with L5 and changes every fifth locker, and
so on, until student S100 changes L100.
After all the students have passed through the building and changed the lockers, which
lockers are open?

= = = 
Answer analysis:
The i-th locker condition will always be changes (False -> True -> False). Thus we can analize it 
by counting each number appearance in other locker factors.'''

# Prompt locker condition False = Closed
locker = [False] * 100

# main
def numberOfFactors(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return(int(count))
    
print("The opened lockers are:")
for i in range(100):
    if numberOfFactors(i) % 2 == 1:
        print(i, end=' ')
        locker[i-1] = True
print(locker)
