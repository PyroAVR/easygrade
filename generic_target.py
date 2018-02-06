class target:
    def __init__(self):
        self.run_type = ''
        self.priority = -1
        self.name     = ''
        raise NotImplementedError('dude this class is abstract')
    def set_work_dir(self, path):
        raise NotImplementedError('stop')
    def clone(self):
        raise NotImplementedError('dude wtf')
    def make(self):
        raise NotImplementedError('S T O P how did you even get here')
