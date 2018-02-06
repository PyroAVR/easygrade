import generic_target
class target(generic_target.target):

    def __init__(self, name='dummy', classpath='',sourcepath='.',\
                 destination='.', javac='javac'):
        self.run_type       = 'system'
        self.priority       = 1
        self.name           = name
        self.classpath      = classpath
        self.sourcepath     = sourcepath
        self.destination    = destination
        self.javac          = javac
        self.java_home      = ''

    def set_work_dir(self, path):
        self.set_source_path(path)

    def set_name(self, name):
        self.name = name

    def set_source_path(self, sourcepath):
        self.sourcepath = sourcepath

    def set_class_path(self, classpath):
        self.classpath = classpath

    def set_destination(self, destination):
        self.destination = ' -d ' + destination

    def set_javac(self, javac):
        self.javac = javac

    def set_java_home(self, home):
        self.java_home = home

    def clone(self):
        t = target()
        t.run_type       = self.run_type
        t.priority       = self.priority
        t.name           = self.name
        t.classpath      = self.classpath
        t.sourcepath     = self.sourcepath
        t.destination    = self.destination
        t.javac          = self.javac
        t.java_home      = self.java_home
        return t


    def make(self):
        r = self.javac + ' -d \'' + self.sourcepath + '\'/' + self.destination
        if self.classpath != '':
            r += ' -classpath ' + self.classpath

        r += ' -sourcepath \'' + self.sourcepath + '\' '\
        + '\'' + self.sourcepath + '\'' + '/' + self.name
        print(r)
        return r
