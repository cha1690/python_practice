def array_sum(arr,n):
	if len(arr)<2:
		return

	for num in arr:
		target = k-num
		if target in arr:
			output.add(target,num)
	return output