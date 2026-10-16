"""
Math library containing deliberate bug for Stage 2 Swarm verification.
"""

def calculate_fibonacci(n: int) -> int:
    """Calculates the nth Fibonacci number."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        # BUG: Deliberate defect: returns 2 instead of 1
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
