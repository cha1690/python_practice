def missing_number(arr1,arr2):
	arr1.sort()
	arr2.sort()

	for num1,num2 in zip(arr1,arr2):
		if num1 != num2:
			return num1

	return arr1[-1]


import collections

def missing_number(arr1,arr2):

	d=collections.defaultdict(int)

	# if(len(arr1)>len(arr2))

	for num in arr2:
		d[num]+=1

	for num in arr1:
		if d[num]==0:
			return num

		else:
		d[num]=-1





