class NCMBQuery:
  NCMB = None
  def __init__(self, class_name):
    self.class_name = class_name
    self.where = None
    self.limit = None
    self.skip = None
    self.order = None
    self.include = None

  def equal_to(self, key, value):
    return self.set_operand(key, value)
  
  def set_operand(self, key, value, ope = None):
    if self.where is None:
      self.where = {}
    if ope is None:
      self.where[key] = value
      return self
    if key not in self.where:
      self.where[key] = {}
    self.where[key][ope] = value
    return self

  def fetch_all(self):
    req = NCMBRequest()
    queries = {}
    for key in ['where', 'limit', 'skip', 'order', 'include']:
      if self[key] is not None:
        queries[key] = self[key]
    ary = req.get(self.class_name, queries)
    results = []
    for params in ary:
      o = self.NCMB.Object(class_name)
      o.sets(params)
      results.add(o)
    return results
