import struct
import logging
import json

logger = logging.getLogger('django')

def binaryConversion(value, data_type_name):
    if data_type_name == "boolean":
        value = 0 if value == '0' else value
        return struct.pack("?", value)
    elif data_type_name == "string":
        s = bytes(value, 'utf-8')    # Or other appropriate encoding
        return struct.pack("50s", s)
    elif data_type_name == "color":
        s = bytes(value, 'utf-8')    # Or other appropriate encoding
        return struct.pack("50s", s)
    elif data_type_name == "number":
        return struct.pack("d", float(value))
    return None

def fromBinary(binary_value, data_type_name):
    if data_type_name == "boolean":
        return struct.unpack("?", binary_value)[0]

    elif data_type_name == "string":
        string = struct.unpack("50s", binary_value)[0]
        rep = ''
        for c in string:
            if c != 0:
                rep += chr(c)
        return rep

    elif data_type_name == "color":
        string = struct.unpack("50s", binary_value)[0]
        rep = ''
        for c in string:
            if c != 0:
                rep += chr(c)
        try:
            rep = json.loads(rep)
        except json.JSONDecodeError:
            logger.error("FAILED to convert binary color payload : JSON provided by the user nay be in the wrong format : {}".format(rep))
        return rep

    elif data_type_name == "number":
        return struct.unpack("d", binary_value)[0]
    return None
