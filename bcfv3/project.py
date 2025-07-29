import xml.etree.ElementTree as ET
import utils

class ProjectBcfp():
    __slots__ = ("Name","ProjectId")
    def __init__(self,Name, ProjectId):
        self.Name = Name
        self.ProjectId = ProjectId
    def __setattr__(self, attr, value):
        value = self.check_attr(attr, value)
        object.__setattr__(self, attr, value)
    def check_attr(self,attr,val):
        if str(attr) == "Name":
            if not (isinstance(val, str)):
                raise AttributeError(f"'{attr}' must be a String, eventhrough it has no name")
        elif str(attr) == "ProjectId":
            if not (isinstance(val, str)):
                raise AttributeError(f"'{attr}' must be a String and it is recommended to be uuid4")
        return val

def create_project_bcfp(bcfPath, objProjectBcfp):
    """
    Create projects.bcfp file from object ExtensionsXml
    """
    if not isinstance(objProjectBcfp, ProjectBcfp):
        raise AttributeError("Arg objProjectBcfp must be a ProjectBcfp object")
    ProjectInfo = ET.Element("ProjectInfo")
    Project = ET.SubElement(ProjectInfo, "Project", attrib={"ProjectId":objProjectBcfp.ProjectId})
    Name = ET.SubElement(Project, "Name")
    Name.text = objProjectBcfp.Name
    ET.indent(ProjectInfo, space = "  ", level = 0)
    bcfPath = utils.check_bcfPath(bcfPath)
    finalXmlTree = ET.ElementTree(ProjectInfo)
    finalXmlTree.write(f"{bcfPath}project.bcfp", encoding='utf-8', xml_declaration=True, short_empty_elements = False)