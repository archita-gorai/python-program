#you are climbing a staircase with n steps, with each move u can move 1 step or 2 step, you have to reach n steps, in how many distinct ways can you do that

def stair(a,memo={}):
    if a in memo:
        return memo[a]
    if a==0 or a==1:
        return 1
    memo[a]=stair(a-1,memo)+stair(a-2,memo)
    return memo[a]
a=(int)(input("Enter number of steps:"))
print("Number of ways:",stair(a))    