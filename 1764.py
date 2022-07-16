n, m = map(int, input().split())

db = set()
real = set()

for i in range(n):
    db.add(input())

for j in range(m):
    real.add(input())

result = sorted(list(db & real)) # set끼리의 교집합을 구하고 리스트로 변형

print(len(result))

for k in result:
    print(k)