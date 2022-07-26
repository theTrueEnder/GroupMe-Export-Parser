
class user:
  def __init__(self, userid, nickname, avatarurl, id, name):
      self._user_id = userid
      self._nickname = nickname
      self._avatar_url = avatarurl
      self._id = id
      self._name = name

  ''' NICKNAME '''
  @property
  def nickname(self):
    if self._nickname != '':
      tmp = self._nickname
      if "´" or "’" or "`" in tmp:
        tmp.replace("´", "'")
        tmp.replace("’", "'")
        tmp.replace("`", "'")
        self._nickname = tmp
      return self._nickname
    else:
      tmp = self._name
      if "´" or "’" or "`" in tmp:
        tmp.replace("´", "'")
        tmp.replace("’", "'")
        tmp.replace("`", "'")
        self._name = tmp
      return self._name
  @nickname.setter
  def platform(self, value):
      self._nickname = value
  @nickname.deleter
  def nickname(self):
      del self._nickname

  ''' USERID '''
  @property
  def user_id(self):
      return self._user_id
  @user_id.setter
  def user_id(self, value):
      self._user_id = value
  @user_id.deleter
  def user_id(self):
      del self._user_id

  ''' NAME '''
  @property
  def name(self):
      return self._name
  @name.setter
  def name(self, value):
      self.name = value
  @name.deleter
  def name(self):
      del self._name


class conversation:
  def __init__(self):
    self.id = None
    self.group_id = None
    self.name = None
    self.description = None
    self.image_url = None
    self.created_at = None
    self.msg_count = None
    self.share_url = None
    self.members = []
    #self.like_icon = None

  #takes in dictionary, assumes json parsing happens above
  def parse(self, json):
    self.id =           json['id']
    self.group_id =     json['group_id']
    self.name =         json['name']
    self.description =  json['description']
    self.image_url =    json['image_url']
    self.created_at =   json['created_at']
    self.msg_count =    json['messages']['count']
    self.share_url =    json['share_url']
    member_list =      json['members']
    #self.like_icon =   json['like_icon']

    for member in member_list:
      self.members.append( 
        user(
          member['user_id'], 
          member['nickname'], 
          member['image_url'], 
          member['id'], 
          member['name']
        )
      )

  def get_member_by_id(self, user_id):
    for member in self.members:
      if member.user_id == user_id:
        return member
    return None

  def export(self):
    s =    'Group:       ' + self.name
    s += '\nDescription: ' + self.description
    s += '\nDetails:' + self.description
    s += '\n\t' + str(self.msg_count) + ' messages'
    s += '\n\t' + str(len(self.members)) + ' members'
    s += '\n'
    return s
