# Шахов Кирилл 
# Несколько тестов на нахождение nod

import pytest
import nod

def factory(a, b, c):
	def test():
		assert nod.nod(a, b) == c
	return test

test1 = factory(1, 2, 1)
test2 = factory(66, 6, 6)
test3 = factory(100, 10, 10)
