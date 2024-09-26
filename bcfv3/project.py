import xml.etree.ElementTree as ET
import pathlib
import os

def create_bcfversion(projectPath = "",bcfVersion = ""):
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