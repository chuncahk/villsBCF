import xml.etree.ElementTree as ET
import utils

class BcfVersion():
    __slots__ = ("Version")
    def __init__(self, Version):
        self.Version = Version
    def __setattr__(self, attr, value):
        value = self.check_attr(attr,value)
        object.__setattr__(self, attr, value)
    def check_attr(self,attr,value) -> str:
        if (isinstance(value, int) or isinstance(value, float)):
            return (f"{value:.1f}")
        else:
            raise AttributeError(f"Type of '{attr}' must be Integer or Float")

def create_bcf_version(bcfPath,objBcfVersion):
    """
    Create bcf.version file from object BcfVersion
    """
    if not isinstance(objBcfVersion, BcfVersion):
        raise AttributeError("Arg objBcfVersion must be a BcfVersion object")
    Version = ET.Element("Version", attrib={"VersionId":objBcfVersion.Version})
    ET.indent(Version, space = "  ", level = 0)
    bcfPath = utils.check_bcfPath(bcfPath)
    finalXmlTree = ET.ElementTree(Version)
    finalXmlTree.write(f"{bcfPath}bcf.version", encoding='utf-8', xml_declaration=True, short_empty_elements = False)