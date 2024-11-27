import xml.etree.ElementTree as ET
import os as __os__

def __check_bcfPath(bcfPath):
    if (not __os__.path.isdir(bcfPath)):
        raise AttributeError("Arg bcfPath must be a valid directory")
    if not bcfPath.endswith("\\"):
        bcfPath = f"{bcfPath}{__os__.sep}"
    return(bcfPath)

def __check_NonEmptyOrBlankString(attr,value) -> str:
    warning_NonEmptyOrBlankString = f"All elements in '{attr}' must be a Non-Empty or Blank String"
    if not (isinstance(value, str)):
        raise AttributeError(warning_NonEmptyOrBlankString)
    if len(value.strip()) == 0:
        raise AttributeError(warning_NonEmptyOrBlankString) 
    return(value)

class File():
    __slots__ = ("IfcProject","IfcSpatialStructureElement","isExternal","Filename","Date","Reference")
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
        if str(attr) == "isExternal":
            if isinstance(value,bool):
                return(value)
        elif str(attr) == "Filename":
            if isinstance(value,bool):
                return(value)

class TopicHeader():
    __slots__ = ("Files")
    def __init__(self, Files):
        self.Files = Files
    def __setattr__(self, attr, value):
        value = self.check_attr(attr,value)
        object.__setattr__(self, attr, value)
    def check_attr(self,attr,value) -> str:
        if str(attr) == "isExternal":
            pass

class ExtensionsXml():
    __slots__ = ("TopicTypes","TopicStatuses","Priorities","TopicLabels","Users","SnippetTypes","Stages")
    def __init__(self,TopicTypes,TopicStatuses,Priorities,TopicLabels,Users,SnippetTypes,Stages):
        self.TopicTypes = TopicTypes
        self.TopicStatuses = TopicStatuses
        self.Priorities = Priorities
        self.TopicLabels = TopicLabels
        self.Users = Users
        self.SnippetTypes = SnippetTypes
        self.Stages = Stages
    def __setattr__(self, attr, value):
        value = self.check_attr(attr, value)
        object.__setattr__(self, attr, value)
    def check_attr(self,attr,value):
        if not (isinstance(value, list)):
            raise AttributeError(f"Type of '{attr}' must be a List")
        warning_NonEmptyOrBlankString = f"All elements in '{attr}' must be a Non-Empty or Blank String"
        for val in value:
            if not (isinstance(val, str)):
                raise AttributeError(warning_NonEmptyOrBlankString)
            if len(val.strip()) == 0:
                raise AttributeError(warning_NonEmptyOrBlankString)
        if len(value) != len(set(value)):
            raise AttributeError(f"Elements in '{attr}' cannot be repeated")
        return(value)

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
                raise AttributeError(f"'{attr}' must be a String and the format is recommended to be uuid4")
        return val

def create_bcf_version(bcfPath,objBcfVersion):
    """
    Create bcf.version file from object BcfVersion
    """
    if not isinstance(objBcfVersion, BcfVersion):
        raise AttributeError("Arg {objBcfVersion.title()} must be a BcfVersion object")
    Version = ET.Element("Version", attrib={"VersionId":objBcfVersion.Version})
    ET.indent(Version, space = "  ", level = 0)
    bcfPath = __check_bcfPath(bcfPath)
    finalXmlTree = ET.ElementTree(Version)
    finalXmlTree.write(f"{bcfPath}bcf.version", encoding='utf-8', xml_declaration=True, short_empty_elements = False)

def create_extensions_xml(bcfPath,objExtensionsXml):
    """
    Create extensions.xml file from object ExtensionsXml
    """
    if not isinstance(objExtensionsXml, ExtensionsXml):
        raise AttributeError("Arg objExtensionsXml must be a ExtensionsXml object")
    Extensions = ET.Element("Extensions")
    
    def __create_subelement(obj,main,slot,subslot):
        ele = ET.SubElement(main,slot)
        for text in getattr(obj,slot):
            subEle = ET.SubElement(ele,subslot)
            subEle.text = text
    subslots = ["TopicType","TopicStatus","Priority","TopicLabel","User","SnippetType","Stage"]
    for n,slot in enumerate(objExtensionsXml.__slots__):
        __create_subelement(objExtensionsXml, Extensions, slot, subslots[n])

    ET.indent(Extensions, space = "  ", level = 0)
    bcfPath = __check_bcfPath(bcfPath)
    finalXmlTree = ET.ElementTree(Extensions)
    finalXmlTree.write(f"{bcfPath}extensions.xml", encoding='utf-8', xml_declaration=True, short_empty_elements = False)
