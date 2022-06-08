class NotFoundException(Exception):
    def __init__(self, item: str):
        super().__init__()
        self.status_code = 404
        self.msg = f'{item} not found'
