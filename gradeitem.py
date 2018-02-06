from runner import runner
class gradeitem:

    def __init__(self, name):
        self.name           = name
        self.total_points   = 0
        self.points_earned  = 0
        self.tests          = runner()


    def add_subitem(self, target, points):
        self.total_points += points
        self.tests.add_target(target)  # a breakthrough

    def score(self):
        self.tests.run_targets()

    # def del_subitem(self, name):
    #     if name not in self.targets: pass
    #     points = self.targets[name][1]
    #     del self.targets[name]
    #     self.total_points -= points

    def get_points_earned(self):
        self.points_earned = 0
        for target in self.targets:
            self.points_earned += target[0]
        return self.points_earned

    def get_percentage_grade(self):
        return self.get_points_earned()/self.total_points

    def clone(self):
        g = gradeitem()
        g.name          = self.name
        g.total_points  = self.total_points
        g.points_earned = 0 #this one is potentially important to have as zero
        g.targets       = dict([target.clone() for target in self.targets]) #deep
        return g
