class Matrix:
  def __init__(self, a, b, c, d):
    self.a = a
    self.b = b
    self.c = c
    self.d = d

  def __add__(self, m):
    a = self.a + m.a
    b = self.b + m.b
    c = self.c + m.c
    d = self.d + m.d
    return Matrix(a, b, c, d)

  def __sub__(self, m):
    a = self.a - m.a
    b = self.b - m.b
    c = self.c - m.c
    d = self.d - m.d
    return Matrix(a, b, c, d)

  def __matmul__(self, m):
    return self.a * m.a + self.b * m.b + self.c * m.c + self.d * m.d

  def __repr__(self):
    return "[{a}, {b} \n {c}, {d}]".format(a=self.a, b=self.b, c=self.c, d=self.d)

if __name__ == "__main__":
  # adding
  m1 = Matrix(1, 2, 3, 4)
  m2 = Matrix(1, 2, 3, 4)
  m3 = m1 + m2
  print(m3)

  # subtracting
  m5 = m1 - m2
  print(m5)

  # dot product
  m4 = m1 @ m2
  print(m4)