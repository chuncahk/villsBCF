import xml.etree.ElementTree as ET

filepath_xml = "C:\\Users\\Chun\\OneDrive\\BIMDevelop\\BCF\\Sample1\\56ecd7ca-2025-4bb4-b17d-76a6d5044716\\markup.bcf"
filepath_new_xml = filepath_xml + "2"
tree = ET.parse(filepath_xml)
root = tree.getroot()

#dir(root.findall("Comment")[0].find("Comment"))
c = root.findall("Comment")[0].find("Comment")
c.text = "Testing"
#print(root.findall("Comment")[0].keys())
#print(root.findall("Comment")[0].attrib)
#print(root.findall("Comment")[0].findall("*"))
#root.findall("Comment")[0]
#tree.write(filepath_new_xml)