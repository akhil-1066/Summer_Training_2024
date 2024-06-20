def hcf(m, n):
    if not m%n:
        return n
    return hcf(n, m%n)
def is_coprime(m, n):
    if n>m:
        m, n = n, m
    if hcf(m, n) == 1:
        return True
    return False