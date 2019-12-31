# nth to the last node using doubly linked list

def nth_tolast(n,head):

	right_pointer=head
	left_pointer=head

	if not right_pointer.nextnode:
            raise LookupError('Error: n is larger than the linked list.')

    for i in range(n-1):
		right_pointer=right_pointer.nextnode

	while right_pointer.nextnode:
		right_pointer=right_pointer.nextnode
		left_pointer=left_pointer.nextnode

	return left_pointer
