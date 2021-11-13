def dividers(n):
	res = []
	for i in range(1, abs(n) + 1):
		if not n%i:
			res += [i, -i]
	return res
	
def find_root(a, arr):
		tmp = arr[0]
		for i in range(1, len(arr)):
			tmp = tmp*a + arr[i]
		return tmp == 0
			
		
n = int(input("степень многочлена "))
aa = 0
arr = []

for i in range(n + 1):
	arr.append(int(input("коэффициент  ==  ")))
to_choose = dividers(arr[-1])
print("       ", *arr)

for a in to_choose:
	if find_root(a, arr):
		aa = a
		break
print("a = ", aa)		
tmp = arr[0]
print(tmp, end=" ")
for i in range(1, n+1):
	tmp = tmp*aa + arr[i]
	print(tmp, end=" ")
	