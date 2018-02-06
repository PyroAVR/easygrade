import generic_target
class target(generic_target.target):
    def __init__(self):
        self.clean_target   = None  #which unicode cleaner?
        self.files          = list()
        self.workdir        = ''
        self.name           = 'java clean & preprocess'
        self.run_type       = 'immediate'
        self.priority       = 0

    def set_work_dir(self, path):
        self.workdir = path + '/'

    def add_file(self, file_in, file_out=''):
        file_out = file_in if file_out == '' else file_out
        self.files.append((file_in, file_out))


    def set_clean_level(self, level):
        if 'unicode_sanitize' not in globals():
            import unicode_sanitize
        if level == 'all':
            self.clean_target = unicode_sanitize.clean_all_non_ascii
        else:
            self.clean_target = unicode_sanitize.scan_zero_space

    def clone(self):
        t = target()
        t.clean_target  = self.clean_target
        t.files         = [f for f in self.files]
        t.name          = self.name
        t.workdir       = self.workdir
        t.run_type      = self.run_type
        t.priority      = self.priority
        return t

    def make(self):
        # I am so sorry to whomever has to see this
        # it just calls unicode_sanitize.scan_zero_space or .clean_all_non_ascii
        # also this function runs immediately
        for file_in, file_out in self.files:
            self.clean_target(self.workdir + file_in, self.workdir + file_out)
