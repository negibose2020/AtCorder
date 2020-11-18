'''
from line_profiler import LineProfiler
import os
from contextlib import redirect_stdout

class Num(object):
    def __init__(self,n=1):
        self.num=n
    def sum(self,n):
        ans=self.num
        for i in range (n):
            ans+=i
        return ans
def f(n):
    return n
def g(n):
    return f(n)
def h(n):
    return g(n)

def main():
    a=Num(0)
    a.sum(10**6)
    ans=[0]*4
    for _ in range (10**6):
        ans[0]+=_
    for i in range (10**6):
        ans[1]+=f(i)
    for j in range (10**6):
        ans[2]+=g(j)
    for k in range (10**6):
        ans[3]+=h(k)


if __name__=='__name__':
    main()

prof = LineProfiler()
prof.add_function(main)
with redirect_stdout(open(os.devnull,'w')):
    prof.runcall(main)
prof.print_stats()
'''

a="DDDIDDDIDDDIDDIDDDDDDDDIRUUUIUUUUUUIUIUUIUIUUIUIUUUDDDDDDDDDDDDDDDDDDDRUUUUUUUUUUIUUUUIUUUIUUDDDDDDDDDDDDDDDDDDDRUIUUUIUIUIUUUUUUUIUUIUUUIUDDDDDDDDDDDDDDDDDDDRUUUIUIUIUIUUUUUUIUUUUIUUUDDDDDDDDDDDDDDDDDDDRUUUIUUUUUUIUUUIUUUUUUUDDDDDDDDDDDDDDDDDDDRUUUUUUUUUUUIUIUUUIUUUUDDDDDDDDDDDDDDDDDDDRUUUUUUUUIUUUIUUIUIUUUUUDDDDDDDDDDDDDDDDDDDRUUUUIUIUUIUIUUUUUUUUUUIUDDDDDDDDDDDDDDDDDDDRIUUIUIUUIUUUIUUUUUUUUUUIUDDDDDDDDDDDDDDDDDDDRUIUIUUUUUIUUIUUIUUUIUUUUIUDDDDDDDDDDDDDDDDDDDRUUUIUUIUIUUUIUUUUUIUUIUUUDDDDDDDDDDDDDDDDDDDRUIUUUIUIUUUUUUUUUIUUIUUUDDDDDDDDDDDDDDDDDDDRIUUUUUIUUUUUUUIUUUUUUUDDDDDDDDDDDDDDDDDDDRUUIUUUUUUUUUIUUUUUUUUDDDDDDDDDDDDDDDDDDDRUUUIUIUIUUUUIUUUUUUUUUUDDDDDDDDDDDDDDDDDDDRIUUUIUUUIUUUUUUUUUIUUUIUDDDDDDDDDDDDDDDDDDDRUUUUUIUUIUIUUUUIUIUUIUUUUIDDDDDDDDDDDDDDDDDDDRUUUUUIUIUUUUIUIUIUUIUUIUIUUDDDDDDDDDDDDDDDDDDDRUUUIUUUIUUUUUUUIUUUIDDDLLLLLLLLLLLLLLLLIODDLLLIOUUUUUURRRRRRIODDDDDRIOURRIOULLLLLLLIOUURRRRRRIODDIODLLIOUUIOUURRIODDDDDLLLLIOUUUUUULLLLIODDRRIOUUIODDDDDDDDLLIOUUUUUUURRRRRRRIOUULLLLLLLIORRRIODDDDDDDDRRRRRIOUUULIOUULLIOUURRRRIOULIODDDDDDDLLIOUUUUUUULLIODDRRRRRIODDDDDIOUUUULLLLLIODDDDDDRRIOUIOUUUUURIODDDDDLLLLLLIOUUUUUURRRIOUULLLIODDDDRRRRRRRRIODDLIOUULLLLLIODDDRRRRRIODDIOLLLLLLLIOUUUUUURRRRRRRRIODDDDDIOUUUULLLLLLLIORRRRRIODDDDLLLLLIOUUURRRRIODDDDRIOUUUULLLIODLLIODLLIODDRRRRRRRRRIOUUUUUUUUUIODDLLLLLLLLLIODDRRRRRRRRIODDDLLLLLLIOUUULLIOURRRIOLLLIODRRRRRIODLLLLIOUIOUUURRRIODDDDDDLLLIOUUUUUURRRRRRRIODDLLIOUUIODDDDRRRIODDDDLLLLLLIOUUURIOUUIOUUURIODDLLLLIOUUURIORRRRRIODDDDDDLLIOUUUUULLIODIODDDDLLLIODRRRIOUUUUULIODDDDDDDIORRRIOUIOUUUUUUUUIODLLLLIORRRRRRIODDDDDDDLLLIOUURRRIODDLLLLIORRRRIOUUULLIODLLLLIOUUUUUURRRRRIODDLLLLLIODDDRRIODDRRIOUUUUUIODDDDDDDLIOUUUULLLLIO"

print(len(a))
print(a.count("D"))
print(a[857])