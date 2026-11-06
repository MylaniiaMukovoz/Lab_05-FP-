"""
Модуль для роботи з лінивими обчисленнями (генератори та itertools).
"""
from typing import Iterable, Iterator, TypeVar, Tuple
from itertools import islice, count, accumulate
from collections import deque
import operator

T = TypeVar("T")

def take(n: int, it: Iterable[T]) -> list[T]:
    """Взяти перші n елементів."""
    if n < 0:
        raise ValueError("n не може бути від'ємним")
    return list(islice(it, n))

def drop(n: int, it: Iterable[T]) -> Iterator[T]:
    """Пропустити перші n елементів і повернути ітератор на решту."""
    if n < 0:
        raise ValueError("n не може бути від'ємним")
    it = iter(it)
    next(islice(it, n, n), None)
    return it

def sliding_window(it: Iterable[T], k: int) -> Iterator[Tuple[T, ...]]:
    """Повертає ковзне вікно розміру k."""
    if k <= 0:
        raise ValueError("Розмір вікна k має бути більше 0")
    it = iter(it)
    dq: deque[T] = deque(maxlen=k)
    for _ in range(k):
        try:
            dq.append(next(it))
        except StopIteration:
            return
    yield tuple(dq)
    for x in it:
        dq.append(x)
        yield tuple(dq)

def naturals(start: int = 1) -> Iterator[int]:
    """Нескінченний генератор натуральних чисел."""
    yield from count(start)

def factorial_stream() -> Iterator[int]:
    """
    Лінивий нескінченний потік факторіалів: 0!, 1!, 2!, 3!, ...
    Використовується count() та accumulate(operator.mul) для уникнення повторних обчислень.
    """
    yield 1  
    yield from accumulate(naturals(1), operator.mul)
