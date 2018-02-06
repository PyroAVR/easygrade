from gradeitem import gradeitem

class grade:
    def __init__(self):
        self.max_score      = 100
        self.total_points   = 0
        self.score          = 0
        self.items          = dict()

    def add_grade_item(self, item):
        self.items[item.name] = item
        self.total_points += item.total_points

    def get_points_earned(self):
        self.score = 0
        for item in self.items:
            self.score += items[item].get_points_earned()
        return self.score

    def get_percentage_grade(self):
        points = self.get_points_earned()
        return points/self.total_points

    def clone(self):
        g = grade()
        g.max_score     = self.max_score
        g.total_points  = self.total_points
        g.score         = 0
        g.items         = dict([item.clone() for item in self.items]) #deep
        return g
