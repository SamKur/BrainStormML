import sys  #Built-in functions, exceptions, and other objects.
# import logging
from src.logger import logging

def error_message_details(error, error_details:sys):
    exec_tb = error_details.exc_info()[2]
    filename = exec_tb.tb_frame.f_code.co_filename
    linenumber = exec_tb.tb_lineno
    return f"Error in py script [{filename}] @ line [{linenumber}] errmsg [{error}]"

class SusamayException(Exception):
    def __init__(self, error, error_details:sys):
        super().__init__(str(error))
        self.error_message = error_message_details(error, error_details)

    def __str__(self):
        return self.error_message
    
# # checking if exception.py is working or not
# if __name__=="__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Logging from exeception file started")
#         raise SusamayException(e,sys)
#     #We need to log this
#     #logging.info("Logging from exeception file started") 