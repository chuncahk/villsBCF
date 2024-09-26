import xml.etree.ElementTree as ET
import pathlib

bcf_version_file = "C:\\Users\\Chun\\OneDrive\\BIMDevelop\\BCF\\test.xml"

root = ET.Element("Version", attrib={"VersionId":"3.0"})
root.text = "\n"

ET.indent(root, space = "    ", level = 0) #Formatting xml
tree = ET.ElementTree(root)
tree.write(bcf_version_file, encoding='utf-8', xml_declaration=True)