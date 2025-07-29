import os as __os__
import uuid, re

def generate_IfcGuid(): #From ifcopenshell/guid.py
    g = uuid.uuid4().hex
    bs = [int(g[i : i + 2], 16) for i in range(0, len(g), 2)]
    def b64(v, l=4):
        return "".join([chars[(v // (64 ** i)) % 64] for i in range(l)][::-1])
    return "".join([b64(bs[0], 2)] + [b64((bs[i] << 16) + (bs[i + 1] << 8) + bs[i + 2]) for i in range(1, 16, 3)])

def check_IfcGuid(ifc_guid):
    if len(ifc_guid) != 22:
        return False
    allowed_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_$"
    for char in ifc_guid:
        if char not in allowed_chars:
            return False
    try:
        chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_$"
        def b64_to_int(chars_):
            return sum(chars_.index(c) * (64 ** i) for i, c in enumerate(chars_[::-1]))
        parts = [
            b64_to_int(ifc_guid[:2]),
            b64_to_int(ifc_guid[2:6]),
            b64_to_int(ifc_guid[6:10]),
            b64_to_int(ifc_guid[10:14]),
            b64_to_int(ifc_guid[14:18]),
            b64_to_int(ifc_guid[18:22])
        ]
        # If parts can be combined back to 16-byte array
        byte_array = [parts[0]]
        for i in range(1, len(parts)):
            byte_array += [(parts[i] >> (16 - j * 8)) & 0xFF for j in range(3)]
        if len(byte_array) != 16:
            return False
    except Exception:
        return False
    return True

def check_String(attr,value):
    if not (isinstance(value, str)):
        raise AttributeError(f"Type of '{attr}' must be a String")
    return(value)

def check_Boolean(attr,value):
    if not (isinstance(value, bool)):
        raise AttributeError(f"Type of '{attr}' must be a Boolean")
    return(value)

def check_bcfPath(bcfPath):
    if (not __os__.path.isdir(bcfPath)):
        raise AttributeError("Arg bcfPath must be a valid directory")
    if not bcfPath.endswith("\\"):
        bcfPath = f"{bcfPath}{__os__.sep}"
    return(bcfPath)

def check_NonEmptyOrBlankString(attr,value):
    warning_NonEmptyOrBlankString = f"All elements in '{attr}' must be a Non-Empty or Blank String"
    if (not (isinstance(value, str))) or (len(str(value).strip()) == 0):
        raise AttributeError(warning_NonEmptyOrBlankString)
    return(value)

def check_uuid4(attr, value):
    try:
        uuid.UUID(str(value), version=4)
    except ValueError:
        raise AttributeError(f"'{attr}' must be a hexadecimal UUID4 string")
    return(value)

def check_Required(attr,value):
    '''According to the xsd, certain attributes are required'''
    if value.strip() == '':
        raise AttributeError(f'{attr} is required')

def check_Viewpoint(attr,value):
    #Need to think about it
    #Maybe Check the existance of the .bcfv file
    #return the name of the .bcfv file
    if not (isinstance(value, str)):
        raise AttributeError(f"Type of '{attr}' must be a Viewpoint")
    return(value)

def check_Snapshot(attr,value):
    #Need to think about it
    #Check the existance of the image file
    #return the name of the image file
    if not (isinstance(value, str)):
        raise AttributeError(f"Type of '{attr}' must be a Viewpoint")
    return(value)

def check_Viewpoint_in_Comment(attr,value):
    #Need to think about it, return viewpoint Guid
    if not (isinstance(value, str)):
        raise AttributeError(f"Type of '{attr}' must be a Viewpoint")
    return(value)