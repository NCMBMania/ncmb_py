class NCMBUser(NCMBObject):
  def __init__(self):
    super('users')
  def self.login(self, user_name, password):
    req = NCMBRequest()
    queries = {
      userName: user_name,
      password: password
    }
    data = req.get('/login', queries)
    user = NCMBUser()
    user.sets(data)
    self.NCMB.session_token = data.sessionToken
    return user
