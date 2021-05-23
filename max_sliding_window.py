def max_sliding_window(nums, i):
	position =0
	while (position <=len(nums)-i):
		current = nums[position:position+i]
		current_max= max(current)
		print(f'{current}, max is {current_max}')
		position +=1


max_sliding_window([-4, 2, -5, 3, 6], 3)