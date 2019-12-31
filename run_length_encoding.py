def run_length_encoding(str1):
	if len(str1)==1:
		return str1+"1"

	count=1
	i=1
	new_str=""

	while i<len(str1):
		if str1[i]==str1[i-1]:
			count+=1
		else:
			new_str=new_str+str1[i-1]+str(count)
			count=1
		i+=1

	new_str=new_str+str1[i-1]+str(count)
	return new_str
