class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __str__(self):
        return f"Test(a={self.a}, b={self.b})"
    
    def add(self):
        return self.a + self.b
    def subtract(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b