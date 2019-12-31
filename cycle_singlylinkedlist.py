def check_cycle(node):

	marker1=node
	marker2=node

	if marker1.nextnode!= None and marker1!= None:

		marker1=marker1.nextnode
		marker2=marker2.nextnode

		if marker2==marker1:
			return True

	return False