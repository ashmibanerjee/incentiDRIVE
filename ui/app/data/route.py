class Route(object):

    def __init__(self, route_id, name, path):
        self.route_id = route_id
        self.name = name
        self.path = path
        self.participations = []

    def set_participations(self, participations):
        self.participations = participations

class Path(object):

    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def length(self):
        return 42.0

class Participation(object):

    def __init__(self, user_id, user_name, num_tries, total_consumption):
        self.user_id = user_id
        self.user_name = user_name
        self.num_tries = num_tries
        self.total_consumption = total_consumption
