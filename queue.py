class PriorityQueue(object):
  def __init__(self):
    self.queue = []


  def __str__(self):
    return ' '.join([str(i) for i in self.queue])


  def is_empty(self):
    return len(self.queue) == 0


  def insert(self, data):
    self.queue.append(data)


  def delete(self):
    if(self.is_empty() == False):
      max_value_index = 0

      for i in range(0, len(self.queue), 1):
        if(self.queue[i] > self.queue[max_value_index]):
          max_value_index = i

      item = self.queue[max_value_index]
      del self.queue[max_value_index]
      return item
    else:
      return None




q = PriorityQueue()
q.insert(12)
q.insert(1)
q.insert(14)
q.insert(7)
q.insert(12)
q.insert(1)
q.insert(14)
q.insert(7)
print(q)

while not q.is_empty():
  print(q.delete())

q.delete()
