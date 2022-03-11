import time

def calculate_time(x_func):
	def wrapped():
		start = time.time()
		x_func()
		end = time.time()
		print(f"Total time {(end-start)}")
		return x_func()
	return wrapped
