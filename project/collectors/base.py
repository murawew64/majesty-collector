

class BaseCollector:
    '''
    Origins:
    <...url...>
    <...description...>
    '''

    async def collect(self):
        await self.pull()
        if await self.check_changes():
            await self.push()

    async def pull(self):
        assert "Overload me!"

    async def push(self):
        assert "Overload me!"

    async def check_changes(self):
        assert "Overload me!"
