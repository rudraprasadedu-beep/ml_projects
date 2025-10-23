import sys
from logger import logger  # updated import

def error_message_details(error, error_detail: sys):
    """
    Creates a detailed error message with file name and line number.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = (
        "Error occurred in Python script name [{0}] "
        "line number [{1}] "
        "error message [{2}]"
    ).format(file_name, exc_tb.tb_lineno, str(error))
    return error_message


class CustomException(Exception):
    """
    Custom exception class with detailed logging and printing.
    """
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_details(
            error_message, error_detail=error_detail
        )
        # Log the error message
        logger.error(self.error_message)
        # Print to console as well
        print(f"[ERROR] {self.error_message}")

    def __str__(self):
        return self.error_message


# Example usage
if __name__ == "__main__":
    try:
        a = 1 / 0  # intentional error
    except Exception as e:
        raise CustomException(e, sys)
