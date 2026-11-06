import pytest
from streams import take, drop, sliding_window, factorial_stream, naturals

def test_take_basic():
    assert take(5, naturals(1)) == [1, 2, 3, 4, 5]

def test_take_zero():
    assert take(0, naturals(1)) == []

def test_take_negative():
    with pytest.raises(ValueError):
        take(-1, naturals(1))

def test_drop_basic():
    it = drop(5, naturals(1))
    assert take(3, it) == [6, 7, 8]

def test_sliding_window_basic():
    assert list(sliding_window([1, 2, 3, 4], 3)) == [(1, 2, 3), (2, 3, 4)]

def test_sliding_window_empty_or_small():
    assert list(sliding_window([1, 2], 3)) == []

def test_factorial_stream():
    assert take(5, factorial_stream()) == [1, 1, 2, 6, 24]

def test_laziness():
    computed = []
    
    def side_effect_generator():
        for i in range(100):
            computed.append(i)
            yield i
            
    gen = side_effect_generator()
    result = take(5, gen)
    
    assert result == [0, 1, 2, 3, 4]
    assert len(computed) == 5
