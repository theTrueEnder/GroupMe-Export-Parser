from datetime import datetime
def unix_to_dt(time):
    return datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')


class msg_unit():
    '''
    def __init__(self, msg):
        self.msg = msg
        self.id = msg['id']
        self.type = msg['type']
        self.sender = msg['name']
        self.sender_id = msg['sender_id']
        self.avatar_url = msg['avatar_url']
        self.text = msg['text']
        self.attachments = msg['attachments']
        self.favorited_by = msg['favorited_by']
        self.created_at = msg['created_at']
        self.group_id = msg['group_id']
        self.system_message = msg['system_message']
        self.favorited_by = msg['favorited_by']
        self.attachments = msg['attachments']
        self.mentions = msg['mentions']
        self.urls = msg['urls']
        self.emoji_counts = msg['emoji_counts']
        self.reactions = msg['reactions']
        self.client_id = msg['client_id']
        self.group_name = msg['group_name']
        self.group_image_url = msg['group_image_url']
        self.group_creator_id = msg['group_creator_id']
        self.group_creator_name = msg['group_creator_name']
        self.group_creator_avatar_url = msg['group_creator_avatar_url']
        self.group_description = msg['group_description']
        self.group_large_image_url = msg['group_large_image_url']
        self.group_small_image_url = msg['group_small_image_url']
        self.group_join_type = msg['group_join_type']
        self.group_creator_user_id
    '''
    def __init__(self):
        self.time = None
        
        self._created_at = None
        self._favorited_by = []
        self._avatarUrl = None
        self._groupID = None
        self._msgID = None
        self._name = None
        self._senderID = None
        self._senderType = None
        self._sourceGUID = None
        self._system = False
        self._text = None
        self._userID = None
        self._platform = None

    ''' AVATAR URL '''
    @property
    def avatarUrl(self):
        return self._avatarUrl   
    @avatarUrl.setter
    def avatarUrl(self, value):
        self._avatarUrl = value 
    @avatarUrl.deleter
    def avatarUrl(self):
        del self._avatarUrl


    ''' GROUP ID '''
    @property
    def groupID(self):
        return self._groupID
    @groupID.setter
    def groupID(self, value):
        self._groupID = value
    @groupID.deleter
    def groupID(self):
        del self._groupID
    
    ''' MSG ID '''
    @property
    def msgID(self):
        return self._msgID
    @msgID.setter
    def msgID(self, value):
        self._msgID = value
    @msgID.deleter
    def msgID(self):
        del self._msgID

    ''' NAME '''
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @name.deleter
    def name(self):
        del self._name

    ''' SENDER ID '''
    @property
    def senderID(self):
        return self._senderID
    @senderID.setter
    def senderID(self, value):
        self._senderID = value
    @senderID.deleter
    def senderID(self):
        del self._senderID

    ''' SENDER TYPE '''
    @property
    def senderType(self):
        return self._senderType
    @senderType.setter
    def senderType(self, value):
        self._senderType = value
    @senderType.deleter
    def senderType(self):
        del self._senderType
    
    ''' SOURCE GUID '''
    @property
    def sourceGUID(self):
        return self._sourceGUID
    @sourceGUID.setter
    def sourceGUID(self, value):
        self._sourceGUID = value
    @sourceGUID.deleter
    def sourceGUID(self):
        del self._sourceGUID
    
    ''' SYSTEM '''
    @property
    def system(self):
        return self._system
    @system.setter
    def system(self, value):
        value = bool(value)
        if value != True and value != False:
            print("Error: system must be True or False, instead got ", value)
            return
        self._system = value
    @system.deleter
    def system(self):
        del self._system
    
    ''' TEXT '''
    @property
    def text(self):
        return self._text
    @text.setter
    def text(self, value):
        tmp = ''
        if "´" or "’" or "`" in tmp:
            tmp.replace("´", "'")
            tmp.replace("’", "'")
            tmp.replace("`", "'")
        self._text = tmp
    @text.deleter
    def text(self):
        del self._text
    
    ''' USERID '''
    @property
    def userID(self):
        return self._userID
    @userID.setter
    def userID(self, value):
        self._userID = value
    @userID.deleter
    def userID(self):
        del self._userID
    
    ''' PLATFORM '''
    @property
    def platform(self):
        return self._platform
    @platform.setter
    def platform(self, value):
        self._platform = value
    @platform.deleter
    def platform(self):
        del self._platform

    ''' CREATEDAT '''
    @property
    def created_at(self):
        return self._created_at
    @created_at.setter
    def created_at(self, value):
        self._created_at = value
    @created_at.deleter
    def created_at(self):
        del self._created_at

    ''' FAVORITEDBY '''
    @property
    def favorited_by(self):
        return self._favorited_by
    @favorited_by.setter
    def favorited_by(self, value):
        self._favorited_by = value
    @favorited_by.deleter
    def favorited_by(self):
        del self._favorited_by
    
    def parse(self, json):
        self._avatarUrl = json['avatar_url']
        self._groupID = json['group_id']
        self._msgID = json['id']
        self._name = self.clean(json['name'])
        self._senderID = json['sender_id']
        self._senderType = json['sender_type']
        self._sourceGUID = json['source_guid']
        self._system = json['system']
        self._text = self.clean(json['text'])
        self._userID = json['user_id']
        self._platform = json['platform']
        self._created_at = json['created_at']
        self._favorited_by = json['favorited_by']

        self.time = unix_to_dt(self.created_at)

    def clean(self, s):
        o = s
        if s is not None:
            s.strip()
            if "´" or "’" or "`" in s:
                s.replace("´", "'")
                s.replace("’", "'")
                s.replace("`", "'")
        
        if o != s:
            print("Warning: ", o, " changed to ", s)
        return s

    def simple_export(self):
        return {
            'message': self.text,
            'sender': self.senderID,
            'time': self.time
        }

    def s_simple_export(self):
        return f'message: {self.text} \nsender: {self.senderID} \ntime: {self.time}'

    def __str__(self):
        s = self.name + " at " + unix_to_dt(self.createdt) + ": " + self.text
        print(f"${s:20}")

        ''' 
        TODO
        Likedby list
        '''
        #return "msg: " + self.msg + "\nsender: " + self.sender + "\ntime: " + self.time + "\n"

class reply(msg_unit):
    def reply(self, msg, sender, time):
        self.__init__(self, msg, sender, time)
        self.replyID = None
        self.baseReplyID = None

class image(msg_unit):
    def image(self, msg, sender, time):
        self.__init__(self, msg, sender, time)
        self.url = [] #vector <string>