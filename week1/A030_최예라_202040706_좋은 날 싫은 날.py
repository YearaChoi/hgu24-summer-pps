N, now = map(int, input().split())
l = list(map(float, input().split()))
bad = 0.0
good = 0.0

if now == 0:
    good = 1.0
else:
    bad = 1.0
    
g_g = l[0] #좋은날이고 또 좋은날일 확률
g_b = l[1] #좋은날인데 나쁜날일 확률
b_g = l[2] #나쁜날인데 좋은날을 확률
b_b = l[3] #나쁜날이고 또 나쁜날일 확률

for i in range(N):
    prev_good = good
    good = good * g_g + bad * b_g
    bad = prev_good * g_b + bad * b_b

print(int(good * 1000))
print(int(bad * 1000))

# (좋은날이고 또 좋은날이 될 확률) + (나쁜날이었지만 다음이 좋을 확률) 