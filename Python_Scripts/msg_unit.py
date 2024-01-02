from attachments import Attachment
from events import Event
# from helper import clean_text

from datetime import datetime, timezone, timedelta
def unix_to_dt(etime, local_tz):
    # dt = datetime.utcfromtimestamp(etime)
    
    dt = datetime.fromtimestamp(etime, tz=local_tz)    
    s = dt.strftime('%Y-%m-%d %H:%M:%S')
    return s


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
        self._local_tz = None

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
    
    ''' USER_ID '''
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

    ''' AVATAR IMAGE '''
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
    
    ''' FAVORITE COUNT '''
    @property
    def favorite_count(self):
        return self._favorite_count
    @favorite_count.setter
    def favorite_count(self, value):
        self._favorite_count = value
    @favorite_count.deleter
    def favorite_count(self):
        del self._favorite_count

    ''' NICKNAME '''
    @property
    def nickname(self):
        return self._nickname
    @nickname.setter
    def nickname(self, value):
        self._nickname = value
    @nickname.deleter
    def nickname(self):
        del self._nickname
        
    ''' TIMEZONE '''
    @property
    def local_tz(self):
        return self._local_tz
    @local_tz.setter
    def local_tz(self, utc_offset):
        if abs(utc_offset) > 24:
            utc_offset %= 24
        hours_from_utc = timedelta(hours=utc_offset)
        self._local_tz = timezone(hours_from_utc)
    @local_tz.deleter
    def local_tz(self):
        del self._local_tz
        
        
    def parse(self, json, cvn, tz):
        self._avatar_url = json['avatar_url']
        self._group_id = json['group_id']
        self._msg_id = json['id']
        self._name = json['name']
        self._sender_id = json['sender_id']
        self._senderType = json['sender_type']
        self._sourceGUID = json['source_guid']
        self._system = json['system']
        self._text = json['text']
        self._user_id = json['user_id']
        self._platform = json['platform']
        self._created_at = json['created_at']
        self._favorited_by = json['favorited_by']

        self._avatar_image = Attachment({'type': 'image', 'url': self._avatar_url})
        if json['attachments'] is not None:
            for a in json['attachments']:
                if(a['type'] == 'image' and a['url'] is  None):
                    print("Error: image attachment has no url", self.msg_id)
                self._attachments.append(Attachment(a))
        if 'events' in json and json['events'] is not None:
            for e in json['events']:
                self._events.append(Event(e))
        self._favorite_count = len(self._favorited_by)

        self.local_tz = tz
        self.time = unix_to_dt(self.created_at, self.local_tz)
        
        thisuser = cvn.get_member_by_id(self._sender_id)
        if thisuser is None:
            self._nickname = "Deleted User"
        else:
            self._nickname = thisuser.nickname
        # except Exception as e:
        #     print("Tried sender id:", self._sender_id)
        #     print("Message:", self._text)
        #     print(thisuser)
        #     raise e
    

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