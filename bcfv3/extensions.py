import xml.etree.ElementTree as ET
import utils

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

def create_extensions_xml(bcfPath,objExtensionsXml):
    """
    Create extensions.xml file from object ExtensionsXml
    """
    if not isinstance(objExtensionsXml, ExtensionsXml):
        raise AttributeError("Arg objExtensionsXml must be a ExtensionsXml object")
    Extensions = ET.Element("Extensions")
    
    subslots = ["TopicType","TopicStatus","Priority","TopicLabel","User","SnippetType","Stage"]
    for n,slot in enumerate(objExtensionsXml.__slots__):
        ele = ET.SubElement(Extensions,slot)
        for text in getattr(objExtensionsXml,slot):
            subEle = ET.SubElement(ele,subslots[n])
            subEle.text = text

    ET.indent(Extensions, space = "  ", level = 0)
    bcfPath = utils.check_bcfPath(bcfPath)
    finalXmlTree = ET.ElementTree(Extensions)
    finalXmlTree.write(f"{bcfPath}extensions.xml", encoding='utf-8', xml_declaration=True, short_empty_elements = False)