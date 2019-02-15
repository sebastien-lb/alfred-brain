
import logging
from datetime import datetime
logger = logging.getLogger('django')

def compare(operator, data_type_name, value1, value2):
    if data_type_name == "time":
        value1 = value1//60
        value2 = value2//60
    if operator == "GTE":
        return value1 >= value2
    elif operator == "GT":
        return value1 > value2
    elif operator == "LTE":
        return value1 <= value2
    elif operator == "LT":
        return value1 < value2
    elif operator == "EQUAL":
        return value1 == value2
    else:
        logger.warning("FAIL Unknown comparison")

    return False
