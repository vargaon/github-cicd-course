def square_area(a: int) -> int:
    """Counts an area of of square."""
    return a*a

def fib(n: int) -> int:
    """Count a fibonacci number n."""
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    
    return a

def test_square_area() -> None:
    assert square_area(5) == 25
    assert square_area(0) == 0

def test_fib() -> None:
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(5) == 5
    assert fib(10) == 55
    