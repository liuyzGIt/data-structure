
def heap_sort(elems):  # small-big
	def shiftdown(elems, e, begin, end):
		i, j = begin, begin * 2 + 1
		while j < end:
			if j+1 < end and elems[j] < elems[j+1]:  # max child
				j += 1
			if elems[j] < e:  # e is biggest
				break			
			elems[i] = elems[j]  # change
			i, j = j, j * 2 + 1			
		elems[i] = e
	
	end = len(elems)
	for i in range(len(elems)//2, -1, -1):  # build heap O(n)
		shiftdown(elems, elems[i], i, end)
	
	for i in range(end-1, -1, -1):
		e = elems[i]
		elems[i] = elems[0]  # sort
		shiftdown(elems, e, 0, i)


if __name__ == "__main__":
	elems = [1001,122,33,49,500]
	heap_sort(elems)
	print(elems)
