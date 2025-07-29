import xml.etree.ElementTree as ET
import utils

class File():
    __slots__ = ('IfcProject','IfcSpatialStructureElement','isExternal','Filename','Date','Reference')
    def __init__(self,IfcProject,IfcSpatialStructureElement,isExternal,Filename,Date,Reference):
        self.IfcProject = IfcProject
        self.IfcSpatialStructureElement = IfcSpatialStructureElement
        self.isExternal = isExternal
        self.Filename = Filename
        self.Date = Date
        self.Reference = Reference
    def __setattr__(self, attr, value):
        value = self.check_attr(attr,value)
        object.__setattr__(self, attr, value)
    def check_attr(self,attr,value) -> str:
        if str(attr) == 'IfcProject':
            if len(str(value)) != 0:
                return(utils.check_uuid4(attr, value))
        elif str(attr) == 'IfcSpatialStructureElement':
            return(utils.check_uuid4(attr, value))
        elif str(attr) == 'isExternal':
            return(utils.check_Boolean(attr, value))
        elif str(attr) == 'Filename':
            return(utils.check_String(attr, value))

class Viewpoint():
    __slots__ = ('Guid')
    def __init__(self,Guid,Viewpoint,Snapshot):
        self.Guid = Guid
        self.Viewpoint = Viewpoint
        self.Snapshot = Snapshot
    def __setattr__(self, attr, value):
        value = self.check_attr(attr,value)
        object.__setattr__(self, attr, value)
    def check_attr(self,attr,value) -> str:
        if str(attr) == 'Guid':
            return(utils.check_uuid4(attr, value))
        elif str(attr) == 'Viewpoint':
            return(utils.check_Viewpoint(attr, value))
        elif str(attr) == 'Snapshot':
            return(utils.check_Snapshot(attr, value))

class Comment():
    __slots__ = ('Guid', 'Date', 'Author', 'Comment', 'Viewpoint')
    def __init__(self,Guid,Date,Author,Comment,Viewpoint):
        self.Guid = Guid
        self.Date = Date
        self.Author = Author
        self.Comment = Comment
        self.Viewpoint = Viewpoint
    def __setattr__(self, attr, value):
        value = self.check_attr(attr,value)
        object.__setattr__(self, attr, value)
    def check_attr(self,attr,value) -> str:
        if str(attr) == 'Guid':
            return(utils.check_uuid4(attr, value))
        elif str(attr) == 'Date':
            return(utils.check_Boolean(attr, value))
        elif str(attr) == 'Author':
            return(utils.check_String(attr, value))
        elif str(attr) == 'Comment':
            return(utils.check_String(attr, value))
        elif str(attr) == 'Viewpoint':
            return(utils.check_Viewpoint_in_Comment(attr, value))

class TopicHeader():
    """Class representing the header of a BCF topic."""
    __slots__ = ('Files')
    def __init__(self, Files):
        self.Files = Files
    def __setattr__(self, attr, value):
        value = self.check_attr(attr,value)
        object.__setattr__(self, attr, value)
    def check_attr(self,attr,value) -> str:
        if str(attr) == 'isExternal':
            pass

def create_files_to_markup(xml_path, new_files):
    """
    Adds multiple <File> elements to the <Files> section of a BCF Markup XML.

    Parameters:
    - xml_path: Path to the existing XML file.
    - new_files: List of dictionaries, each with keys 'Filename', 'Date', and 'Reference'.
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Find the <Files> element
    files_element = root.find(".//Files")
    if files_element is None:
        raise ValueError("No <Files> element found in the XML.")

    for file_info in new_files:
        file_element = ET.Element("File", IsExternal="true")

        filename = ET.SubElement(file_element, "Filename")
        filename.text = file_info["Filename"]

        date = ET.SubElement(file_element, "Date")
        date.text = file_info["Date"]

        reference = ET.SubElement(file_element, "Reference")
        reference.text = file_info["Reference"]

        files_element.append(file_element)

    # Save the modified XML
    tree.write("updated_markup.xml", encoding="utf-8", xml_declaration=True)
