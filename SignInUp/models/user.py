class User:
    def __init__(self, user_id, username, password_hash, membership_id, trainer):
        self.user_id = user_id
        self.username = username
        self.password_hash = password_hash
        self.membership_id = membership_id
        self.trainer = trainer
