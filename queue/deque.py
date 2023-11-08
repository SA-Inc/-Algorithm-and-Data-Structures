# deque can be implemented as array or linked list
# array easier, but has low performance (need shift, copy elements)
# list has better performance
class Deque:
  def __init__(self):
    self.deque = []

  def is_empty(self):
    return len(self.deque) == 0

  # push to left side (rear)
  def push_back(self, value):
    self.deque.append(value)

  # push to right side (front)
  def push_front(self, value):
    self.deque.insert(0, value)

  # pop from right side (front)
  def pop_front(self):
    return self.deque.pop(0)

  # pop from left side (rear)
  def pop_back(self):
    return self.deque.pop()

  def size(self):
    return len(self.deque)


d = Deque()
print(d.is_empty())

d.push_back(8)
d.push_back(5)

d.push_front(7)
d.push_front(10)

print(d.is_empty())
print(d.deque)
print(d.size())

print(d.pop_back())
print(d.pop_front())
print(d.deque)
