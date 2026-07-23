from datetime import datetime

class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self, user_id):
       self.sessions[user_id] = {
           "logged_in_at": datetime.now()}

    def end_session(self, user_id):
        if user_id in self.sessions:
            del self.sessions[user_id]


    def is_logged_in(self, user_id):
        return user_id in self.sessions