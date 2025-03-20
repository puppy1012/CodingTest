import sys
'''
input_data=sys.stdin.readline().rstrip()
print(input_data)
'''
n=int(input())
for i in range(n):
    result=map(int,sys.stdin.readline().rstrip().split())
    print(result)