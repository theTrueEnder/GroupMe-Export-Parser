EMOJI_PLACEHOLDER = '?'

class attachments():
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

    def image_edited(self, attachments):
        self.image_url = attachments['url']
        self.url = attachments['source_url']

    def video(self, attachments):
        self.url = attachments['url']
        self.preview_url = attachments['preview_url']

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