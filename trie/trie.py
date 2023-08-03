class Trie:
  def __init__(self, is_end = False):
    self.children = {} # str Trie
    self.is_end = is_end # bool


  # time O(n)
  def insert(self, string):
    node = self
    for letter in string:
      if(letter not in node.children):
        # print(string, letter)
        node.children[letter] = Trie()
      node = node.children[letter]
    node.is_end = True


  # time O(n)
  def search(self, string):
    node = self
    for letter in string:
      if(letter not in node.children):
        # print(string, letter)
        return False
      node = node.children[letter]
    if(node.is_end == True):
      return True
    else:
      return False


  # time O(n)
  def delete(self, string):
    def rec(node, string, i):
      if(i == len(string)):
        node.is_end = False
        return len(node.children) == 0
      else:
        next_deletion = rec(node.children[string[i]], string, i + 1)
        if next_deletion:
          del node.children[string[i]]
        return next_deletion and not node.is_end and len(node.children) == 0
    if self.search(string):
      rec(self, string, 0)


  # time O(n)
  def get_all_words(self):
    def rec(node, string, strings):
      if node.is_end:
        strings.append("".join(string))
      for letter in node.children:
        string.append(letter)
        rec(node.children[letter], string, strings)
        string.pop()

    strings = []
    rec(self, [], strings)
    return strings


  def get_words_with_prefix(self, prefix):
    node = self

    for letter in prefix:
      if(letter not in node.children):
        return []
      node = node.children[letter]

    words = []

    if(node.is_end == True):
      words.append(prefix)

    queue = []

    queue.append((node.children, prefix))

    while(len(queue) != 0):
      front = queue.pop(0)
      current = front[0]
      previous = front[1]

      for key in current.keys():
        temp = current[key]
        if(temp.is_end == True):
          words.append(previous + key)
        queue.append((temp.children, previous + key))

    return words


  def count_words(self):
    return len(self.get_all_words())


t = Trie()

t.insert('bear')
t.insert('bell')
t.insert('bid')
t.insert('bull')
t.insert('buy')
t.insert('sell')
t.insert('stock')
t.insert('stop')
t.insert('book')
t.insert('bookmark')

# print(t.search('bell'))
# print(t.search('book'))
# print(t.search('bookmark'))

# print(t.delete('bookmark'))
# print(t.search('bookmark'))
print(t.get_all_words())
print(t.get_words_with_prefix('st'))

# print(t.count_words())
