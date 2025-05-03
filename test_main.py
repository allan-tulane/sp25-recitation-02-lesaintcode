from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650

def test_work():
	assert work_calc(10, 2, 2, lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300


def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work

	work_fn1 = lambda n: work_calc(n, 2, 2, lambda x: x)
	work_fn2 = lambda n: work_calc(n, 2, 2, lambda x: x*x)

	res = compare_work(work_fn1, work_fn2)

	print(res)

	
def test_compare_span():
	span_fn1 = lambda n: span_calc(n, 2, 2, lambda x: x**0.5)
	span_fn2 = lambda n: span_calc(n, 2, 2, lambda x: x)

	res = compare_span(span_fn1, span_fn2)
	print_results(res)
