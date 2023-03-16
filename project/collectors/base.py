

class BaseCollector:
    '''
    Origins:
    <...url...>
    <...description...>
    '''

    async def init_tables(self):
        '''
        Create all tables to store data in database.
        '''
        assert "Overload me!"

    async def collect(self):
        await self.init_tables()
        await self.pull()
        if await self.check_changes():
            await self.push()

    async def pull(self):
        '''
        Collect data from api and sources.
        '''
        assert "Overload me!"

    async def push(self):
        '''
        Save data in database.
        '''
        assert "Overload me!"

    async def check_changes(self):
        '''
        Check data changes before save new data.
        '''
        assert "Overload me!"
