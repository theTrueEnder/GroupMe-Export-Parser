import attachments
import events
from helper import clean_text

from datetime import datetime
def unix_to_dt(time):
    return datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')



class msg_unit():
    def __init__(self):
        self._avatar_url = None
        self._group_id = None
        self._msg_id = None
        self._name = None
        self._sender_id = None
        self._senderType = None
        self._sourceGUID = None
        self._system = False
        self._text = None
        self._user_id = None
        self._platform = None
        self._created_at = None
        self._favorited_by = []

        self._avatar_image = None
        self._attachments = []
        self._events = []
        self._favorite_count = 0

        self.time = None

    ''' AVATAR URL '''
    @property
    def avatar_url(self):
        return self._avatar_url   
    @avatar_url.setter
    def avatar_url(self, value):
        self._avatar_url = value 
    @avatar_url.deleter
    def avatar_url(self):
        del self._avatar_url

    ''' GROUP ID '''
    @property
    def group_id(self):
        return self._group_id
    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @group_id.deleter
    def group_id(self):
        del self._group_id
    
    ''' MSG ID '''
    @property
    def msg_id(self):
        return self._msg_id
    @msg_id.setter
    def msg_id(self, value):
        self._msg_id = value
    @msg_id.deleter
    def msg_id(self):
        del self._msg_id

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
    def sender_id(self):
        return self._sender_id
    @sender_id.setter
    def sender_id(self, value):
        self._sender_id = value
    @sender_id.deleter
    def sender_id(self):
        del self._sender_id

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
    
    ''' USER_id '''
    @property
    def user_id(self):
        return self._user_id
    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @user_id.deleter
    def user_id(self):
        del self._user_id
    
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

    ''' AVATAR IMAGE'''
    @property
    def avatar_image(self):
        return self._avatar_image
    @avatar_image.setter
    def avatar_image(self, value):
        self._avatar_image = value
    @avatar_image.deleter
    def avatar_image(self):
        del self._avatar_image

    ''' ATTACHMENTS '''
    @property
    def attachments(self):
        return self._attachments
    @attachments.setter
    def attachments(self, value):
        self._attachments = value
    @attachments.deleter
    def attachments(self):
        del self._attachments
    
    ''' EVENTS '''
    @property
    def events(self):
        return self._events
    @events.setter
    def events(self, value):
        self._events = value
    @events.deleter
    def events(self):
        del self._events
    
    ''' FAVORITE COUNT'''
    @property
    def favorite_count(self):
        return self._favorite_count
    @favorite_count.setter
    def favorite_count(self, value):
        self._favorite_count = value
    @favorite_count.deleter
    def favorite_count(self):
        del self._favorite_count


    def parse(self, json):
        self._avatar_url = json['avatar_url']
        self._group_id = json['group_id']
        self._msg_id = json['id']
        self._name = clean_text(json['name'])
        self._sender_id = json['sender_id']
        self._senderType = json['sender_type']
        self._sourceGUID = json['source_guid']
        self._system = json['system']
        self._text = clean_text(json['text'])
        self._user_id = json['user_id']
        self._platform = json['platform']
        self._created_at = json['created_at']
        self._favorited_by = json['favorited_by']

        self._avatar_image = attachments.attachment({'type': 'image', 'url': self._avatar_url})
        if json['attachments'] is not None:
            for a in json['attachments']:
                if(a['type'] == 'image' and a['url'] is  None):
                    print("Error: image attachment has no url", self.msg_id)
                self._attachments.append(attachments.attachment(a))
        if 'events' in json and json['events'] is not None:
            for e in json['events']:
                self._events.append(events.event(e))
        self._favorite_count = len(self._favorited_by)

        self.time = unix_to_dt(self.created_at)

    

    # returns the msg_unit's message, sender, and time in a dict
    def simple_export(self):
        return {
            'message': self.text,
            'sender': self.sender_id,
            'time': self.time
        }

    # returns the msg_unit's message, sender, and time in a string
    def s_simple_export(self):
        return f'message: {self.text} \nsender: {self.sender_id} \ntime: {self.time}'

    def __str__(self):
        s = self.name + " at " + unix_to_dt(self.createdt) + ": " + self.text
        print(f"${s:20}")

    def get_attachments(self):
        return self._attachments

    def get_events(self):
        return self._events