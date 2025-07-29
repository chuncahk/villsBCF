bcfPath = "C:\\Users\\Chun\\OneDrive\\BIMDevelop\\BCF\\villsBCF\\Test Field"

#Example of creating bcf.version
import version
test_bcf_version = version.BcfVersion(3)
version.create_bcf_version(bcfPath,test_bcf_version)

#Example of creating extensions.xml
import extensions
test_extensions_xml = extensions.ExtensionsXml(["ERROR","WARNING","INFORMATION","CLASH","OTHER"],
                             ["OPEN","IN_PROGRESS","SOLVED","CLOSED"],
                             ["LOW","MEDIUM","HIGH","CRITICAL"],
                             ["ARC","STR","MEP","CIV"],
                             ["Architect@example.com","Engineer@example.com","MEPDesigner@example.com"],
                             [],
                             ['Phase 1','Phase 2','Phase 3'])
extensions.create_extensions_xml(bcfPath, test_extensions_xml)

#Example of creating project.bcfp
import project
from uuid import uuid4
test_project_bcfp = project.ProjectBcfp("Testing",str(uuid4()))
project.create_project_bcfp(bcfPath, test_project_bcfp)