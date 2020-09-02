# AtCoder Beginner Contest 133
# C - Remainder Minimization 2019
L,R=map(int,input().split())

mod=2019
ans=20000

for i in range (L,min(R,L+mod)):
    for j in range (L+1,min(R+1,L+mod+1)):
        tempans=(i%mod)*(j%mod)
        tempans%=mod
        if tempans<ans:
            ans=tempans

print(ans)