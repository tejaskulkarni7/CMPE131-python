def doubler(x_func):
	def wrapped(*args,**kwargs):
		x_func(*args, **kwargs)
		x_func(*args, **kwargs)
	return wrapped
