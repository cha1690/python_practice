def max_cont_sum(arr):
	if(len(arr))<1:
		max_sum=arr[0]

	max_sum=current_sum=arr[0]

	for num in range(arr[1:]):
		current_sum= max(current_sum+num, num)

		max_sum=max(max_sum,current_sum)

	return max_sum