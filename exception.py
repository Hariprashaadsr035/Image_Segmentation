import sys

def error_message_detail(error_message, error_detail : sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f'The Error has occured in File ({file_name}) at Line number ({exc_tb.tb_lineno}) --> ERROR : ({str(error_message)}) '
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
    