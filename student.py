from grade import grade
from gradeitem import gradeitem
from runner import runner

class student:
    def __init__(self, first, last):
        self.first      = first
        self.last       = last
        self.name       = first + ' ' + last
        self.grade      = None
        self.score      = 0
        self.builder    = runner()

    def add_build_step(self, target):
        self.builder.add_target(target.clone())

    def register_grade(self, grade):
        self.grade = grade.clone()

    def build(self):
        self.builder.set_work_dir(self.last + ', ' + self.first)
        self.builder.run_targets()

    def grade(self):
        self.score = self.grade.score()

def name_from_dir(dirent):
    name = dirent.name
    last,first = name.split(', ')
    last = last.strip()
    first = first.strip()
    return first,last
