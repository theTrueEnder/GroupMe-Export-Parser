from datetime import datetime
def unix_to_dt(time):
    return datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')

class events():
    def __init__(self, events):
        self.type = events['type']
        self.empty = False

        if self.type == 'None':
            self.empty = True
        elif self.type == 'membership.nickname_changed':
            self.nickname_changed(events['data'])
        elif self.type == 'membership.announce.joined':
            self.user_joined(events['data'])
        elif self.type == 'membership.notifications.exited':
            self.user_exited(events['data'])
        elif self.type == 'membership.notifications.removed':
            self.user_removed(events['data'])
        elif self.type == 'membership.notifications.autokicked':
            self.user_autokicked(events['data'])
        elif self.type == 'group.avatar_change':
            self.group_avatar_change(events['data'])
        elif self.type == 'group.like_icon_set':
            self.like_icon_change(events['data'])
        elif self.type == 'group.name_change':
            self.group_name_change(events['data'])
        elif self.type == 'poll.created':
            self.poll_created(events['data'])
        elif self.type == 'poll.reminder':
            self.poll_reminder(events['data'])
        elif self.type == 'poll.finished':
            self.poll_finished(events['data'])
        elif self.type == 'message.deleted':
            self.message_deleted(events['data'])
        else:
            print('Unknown event type: ' + self.type)

    def nickname_changed(self, event_data):
        self.user = event_data['user']
        self.new_name = event_data['name']

    def user_joined(self, event_data):
        self.user = event_data['user']

    def user_added(self, event_data):
        self.user = event_data['adder_user']
        self.added_users = event_data['added_users']

    def user_exited(self, event_data):
        self.placeholder = 'X'
        self.charmap = event_data['charmap']

    def user_removed(self, event_data):
        self.user = event_data['remover_user']
        self.removed_user = event_data['removed_user']

    def user_autokicked(self, event_data):
        self.user = event_data['user']

    def group_avatar_change(self, event_data):
        self.user = event_data['user']
        self.url = event_data['avatar_url']

    def like_icon_change(self, event_data):
        self.user = event_data['user'] 
        self.like_icon = [event_data['pack_id'], event_data['icon_index']]
        # like_icon->type is ignored

    def group_name_change(self, event_data):
        self.user = event_data['user'] 
        self.new_name = event_data['name']

    '''POLL EVENTS'''

    def poll_created(self, event_data):
        self.user = event_data['user'] 
        self.conversation = event_data['conversation']
        self.poll = event_data['poll']

    def poll_reminder(self, event_data):
        self.conversation = event_data['conversation']
        self.poll = event_data['poll']
        self.expiration = unix_to_dt(event_data['expiration'])

    def poll_finished(self, event_data):
        self.conversation = event_data['conversation']
        self.raw_options = event_data['options']
        self.options = []
        for opt in self.raw_options:
            temp_option = {
                "id": None,
                "title": None,
                "votes": None,
                "voter_ids": None
            }
            temp_option["id"] = opt["id"]
            temp_option["title"] = opt["title"]
            try:
                temp_option["votes"] = opt["votes"]
                temp_option["voter_ids"] = opt["voter_ids"]
            except:
                temp_option["votes"] = 0
                temp_option["voter_ids"] = []
            self.options.append(temp_option)


    '''MISC EVENTS'''

    def message_deleted(self, event_data):
        self.message_id = event_data['message_id']
        self.deleted_at = unix_to_dt(event_data['deleted_at'])
        self.deleted_at_ts = event_data['deleted_at']
        self.deletion_actor = event_data['deletion_actor']
        self.deleter_id = event_data['deleter_id']