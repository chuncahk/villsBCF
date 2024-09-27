import xml.etree.ElementTree as ET
import pathlib
import os

class BcfDotVersion():
    __slots__ = ("Version")
    def __init__(self, Version):
        self.Version = Version
    def __setattr__(self, attr, value):
        value = self.check_attr_Version(value)
        object.__setattr__(self, attr, value)
    def check_attr_Version(self,val):
        if (isinstance(val, int) or isinstance(val, float)):
            return (f"{val:.1f}")
        else:
            raise AttributeError("Type of 'Version' must be Integer or Float")

class ExtensionsDotXml():
    __slots__ = ("Version")

def create_bcf_dot_version(bcfPath,objBcfDotVersion):
    """
    Create bcf.version file from object BcfDotVersion
    """
    if (not os.path.isdir(bcfPath)):
        raise AttributeError("Arg bcfPath must be a valid directory")
    if not isinstance(objBcfDotVersion, BcfDotVersion):
        raise AttributeError("Arg objBcfDotVersion must be a BcfDotVersion object")
    path = pathlib.Path(bcfPath)
    root = ET.Element("Version", attrib={"VersionId":objBcfDotVersion.Version})
    root.text = "\n"
    ET.indent(root, space = "    ", level = 0)
    tree = ET.ElementTree(root)
    tree.write(f"{bcfPath}{os.sep}bcf.version", encoding='utf-8', xml_declaration=True)

