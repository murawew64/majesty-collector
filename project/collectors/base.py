

class BaseCollector:
    '''
    Origins:
    <...url...>
    <...description...>
    '''

    def collect(self):
        self.pull()
        if self.check_changes():
            self.push()

    def pull(self):
        assert "Overload me!"

    def push(self):
        assert "Overload me!"

    def check_changes(self):
        assert "Overload me!"
