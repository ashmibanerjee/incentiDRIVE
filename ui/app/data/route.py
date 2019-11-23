from app.data.user import User
from app.data.performance import Performance

class Route(object):

    def __init__(self, rid, name, distance):
        self.rid = rid
        self.name = name
        self.distance = distance

    def leaderboard_list(self):
        return [LeaderboardEntry(User(1, "Jim"), "Sept 2019", Performance(1.2)),
                LeaderboardEntry(User(0, "John"), "Oct 2019", Performance(1.3))]

class LeaderboardEntry(object):

    def __init__(self, user, time, performance):
        self.user = user
        self.time = time
        self.performance = performance
