import generic_target
from os import system
class runner:
    def __init__(self):
        self.targets = list()
        self.workdir = '.'

    def set_work_dir(self, path):  # DO THIS FIRST
        self.workdir = path
        for target in self.targets:
            target.set_work_dir(path)

    def add_target(self, target):
        target.set_work_dir(self.workdir)
        self.targets.append(target)

    def run_targets(self):
        self.targets.sort(key=lambda t:t.priority)
        for target in self.targets:
            if not isinstance(target, generic_target.target):
                print('skipping invalid target ' + str(target))
            if target.run_type == 'immediate':
                target.make()
            if target.run_type == 'system':
                # figure out how to set environment vars
                # also figure out how to do it cleanly
                system(target.make())
