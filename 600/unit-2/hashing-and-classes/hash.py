class Hash():

  def __init__(self, size):
    self.buckets = []
    self.size = size

  def setup_buckets(self):
    for i in xrange(self.size):
      empty_bucket = []
      self.buckets.append(empty_bucket)

  def hash_interger(self, element):
    return element % self.size

  def insert(self, element):
    hashed = self.hash_interger(element)
    
    if self.buckets[hashed] == None:
      self.buckets[hashed] = []

    self.buckets[hashed].append(element)

  def auto_populate_buckets(self, limit):
    for x in xrange(limit):
      self.insert(x)

  def find_element_in_constant_time(self, element):
    hashed = self.hash_interger(element)
    return self.buckets[hashed]

  def __str__(self):
    return str(self.buckets)


size = 30
h = Hash(size)
h.setup_buckets()
print 'initial buckets: \n', h
intergers = 100
h.auto_populate_buckets(intergers)
print 'populated buckets with %d integers: \n' % intergers,
for x in range(len(h.buckets)):
  print h.buckets[x]

print 'finding bucket for the integer 57 in constant time: ',
print h.find_element_in_constant_time(57)