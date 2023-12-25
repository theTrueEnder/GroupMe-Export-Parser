EMOJI_PLACEHOLDER = '<emoji>'

class attachment():
    def __init__(self, attachments):
        self.type = attachments['type']
        self.empty = False

        if self.type == 'None':
            self.empty = True
        elif self.type == 'image':
            self.image(attachments)
        elif self.type == 'image_edited':
            self.image_edited(attachments)
        elif self.type == 'video':
            self.video(attachments)
        elif self.type == 'emoji':
            self.emoji(attachments)
        elif self.type == 'reply':
            self.reply(attachments)
        elif self.type == 'mentions':
            self.mentions(attachments)
        elif self.type == 'autokicked_member':
            self.autokicked_member(attachments)
        elif self.type == 'poll':
            self.poll(attachments)
        elif self.type == 'location':
            self.location(attachments)
        elif self.type == 'file':
            self.file(attachments)
        elif self.type == 'split':
            self.split(attachments)
        else:
            print('Unknown attachment type: ' + self.type)

    def image(self, attachments):
        self.image_url = attachments['url']
        if self.image_url is None: # if no profile image, use groupme logo (from logo fandom website)
            self.image_url = 'https://logos.fandom.com/wiki/File:GroupMeAppIcon.png'
            self.width = '150'
            self.height = '150'
            self.style = 'width: ' + self.width + 'px; height: ' + self.height + 'px;'
        else:
            i = [x.isdigit() for x in self.image_url].index(True)
            i2 = self.image_url.index('.', i)
            temp = self.image_url[i:i2]
            self.width = temp[:temp.index('x')]
            self.height = temp[temp.index('x')+1:]
            self.style = 'width: ' + self.width + 'px; height: ' + self.height + 'px;'

    def image_edited(self, attachments):
        self.image_url = attachments['url']
        self.url = attachments['source_url']
        i = [x.isdigit() for x in self.image_url].index(True)
        i2 = self.image_url.index('.', i)
        temp = self.image_url[i:i2]
        self.width = temp[:temp.index('x')]
        self.height = temp[temp.index('x')+1:]
        self.style = 'width: ' + self.width + 'px; height: ' + self.height + 'px;'

    def video(self, attachments):
        self.url = attachments['url']
        i = self.url[:-4].rindex('.') + 1
        i2 = self.url.rindex('.')
        temp = self.url[i:i2]
        self.video_width = temp[:temp.index('x')]
        self.video_height = temp[temp.index('x')+1 : temp.index('r')]
        try:
            self.resolution = temp[temp.index('r')+1:]
        except:
            self.resolution = 'N/A'

        self.preview_url = attachments['preview_url']
        i = self.preview_url[:-4].rindex('.') + 1
        i2 = self.preview_url.rindex('.')
        temp = self.preview_url[i:i2]
        self.width = temp[:temp.index('x')]
        self.height = temp[temp.index('x')+1 : temp.index('r')]
        self.style = 'width: ' + self.width + 'px; height: ' + self.height + 'px;'


    def emoji(self, attachments):
        self.placeholder = EMOJI_PLACEHOLDER
        self.charmap = attachments['charmap']

    def reply(self, attachments):
        self.user_id = attachments['user_id']
        self.reply_id = attachments['reply_id']
        self.base_reply_id = attachments['base_reply_id']

    def mentions(self, attachments):
        self.mentioned_ids = attachments['user_ids']
        self.loci = attachments['loci']

    def autokicked_member(self, attachments):
        self.user_id = attachments['user_id']

    def poll(self, attachments):
        self.poll_id = attachments['poll_id']

    def location(self, attachments):
        self.name = attachments['name']
        self.lat = attachments['lat']
        self.lng = attachments['lng']

    def file(self, attachments):
        self.file_id = attachments['file_id']

    def split(self, attachments):
        self.token = attachments['token']