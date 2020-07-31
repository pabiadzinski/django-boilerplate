class AppException(Exception):
    default_code = "error"
    default_title = "Произошла ошибка"
    default_message = "Произошла ошибка"

    def __init__(self, code=None, title=None, message=None, data=None):
        self.code = code or self.default_code
        self.title = title or self.default_title
        self.message = message or self.default_message
        self.data = data or {}