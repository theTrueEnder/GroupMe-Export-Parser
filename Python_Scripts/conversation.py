from user import User

class Conversation:
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
        # self.like_icon = None

    # takes in dictionary, assumes json parsing happens above
    def parse(self, json):
        self.id = json["id"]
        self.group_id = json["group_id"]
        self.name = json["name"]
        self.description = json["description"]
        self.image_url = json["image_url"]
        self.created_at = json["created_at"]
        self.msg_count = json["messages"]["count"]
        self.share_url = json["share_url"]
        member_list = json["members"]
        # self.like_icon =   json['like_icon']

        for member in member_list:
            self.members.append(
                User(
                    member["user_id"],
                    member["nickname"],
                    member["image_url"],
                    member["id"],
                    member["name"],
                )
            )

    """ Return a user object given their user_id """
    def get_member_by_id(self, user_id):
        for member in self.members:
            if member.user_id == user_id:
                return member
        return None

    """ Return conversation data as a string """
    def export(self):
        s = "Group:       " + self.name
        s += "\nDescription: " + self.description
        s += "\nDetails:" + self.description
        s += "\n\t" + str(self.msg_count) + " messages"
        s += "\n\t" + str(len(self.members)) + " members"
        s += "\n"
        s.replace('\\"', '\"')
        return s
