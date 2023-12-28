class User:
    def __init__(self, userid, nickname, avatarurl, id, name):
        self._user_id = userid
        self._nickname = nickname
        self._avatar_url = avatarurl
        self._id = id
        self._name = name

    """ NICKNAME """

    @property
    def nickname(self):
        if self._nickname != "":
            return self._nickname
        else:
            return self._name

    @nickname.setter
    def nickname(self, value):
        self._nickname = value

    @nickname.deleter
    def nickname(self):
        del self._nickname

    """ USERID """

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @user_id.deleter
    def user_id(self):
        del self._user_id

    """ NAME """

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self.name = value

    @name.deleter
    def name(self):
        del self._name
