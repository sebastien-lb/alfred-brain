
import logging
logger = logging.getLogger('django')

def compare(operator, data_type_name, value1, value2):

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
