import xml.etree.ElementTree as ET
import pathlib
import os

def create_bcf_version(projectPath = "",bcfVersion = ""):
    """
    Create bcf.version file
    """
    if (projectPath == "" or bcfVersion == ""):
        raise Exception("Arg projectPath, bcfVersion must be defined")
    path = pathlib.Path(projectPath)
    if not isinstance(bcfVersion, str):
        bcfVersion = f"{bcfVersion:.1f}"
    root = ET.Element("Version", attrib={"VersionId":bcfVersion})
    root.text = "\n"
    ET.indent(root, space = "    ", level = 0)
    tree = ET.ElementTree(root)
    tree.write(f"{path}{os.sep}bcf.version", encoding='utf-8', xml_declaration=True)

#def create_extensions_xml(projectPath = "",bcfVersion = ""):

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

class ExtensionsDotXml:
    __slots__ = ("Version")