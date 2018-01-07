# Шахов Кирилл
# ИВТ 2 КУРС 

from sort import sort
import pytest


@pytest.mark.parametrize("a, result", [(range(10, 100), ['14', '28', '29', '35', '41',
                                                         '53', '67', '76', '82', '92'])])

def test_sort(a, result):
    assert sort(a) == result
