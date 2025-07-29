import xml.etree.ElementTree as ET

def json_to_element(tag, content):
    # Handle attributes and text
    attributes = content.get('@attributes', {}) if isinstance(content, dict) else {}
    element = ET.Element(tag, attrib=attributes)

    if isinstance(content, dict):
        for key, value in content.items():
            if key == '@attributes':
                continue
            elif key == '#text':
                element.text = value
            elif isinstance(value, list):
                for item in value:
                    child = json_to_element(key, item)
                    element.append(child)
            else:
                child = json_to_element(key, value)
                element.append(child)
    else:
        element.text = str(content)

    return element

# Example JSON structure
json_data = {
    "Markup": {
        "@attributes": {
            "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
            "xsi:schemaLocation": "markup.xsd"
        },
        "Header": {
            "Files": {
                "File": [
                    {
                        "@attributes": {
                            "IsExternal": "true"
                        },
                        "Filename": "BCF-ARK",
                        "Date": "2021-01-04T09:37:45.000Z",
                        "Reference": "https://bimsync.com/project/f5fbb3c695274d1890036bf64f77eb71/revisions/007afab57f264d2296aae0a452486ae1"
                    },
                    {
                        "@attributes": {
                            "IsExternal": "true"
                        },
                        "Filename": "BCF-MEP",
                        "Date": "2017-08-07T09:51:34.000Z",
                        "Reference": "https://bimsync.com/project/f5fbb3c695274d1890036bf64f77eb71/revisions/a21ed391f9e046a2bb2bc879c48f1d48"
                    }
                ]
            }
        },
        "Topic": {
            "@attributes": {
                "Guid": "a6f801b9-6bf6-4cb9-8b89-1ae24b76074a",
                "ServerAssignedId": "3",
                "TopicStatus": "OPEN",
                "TopicType": "ERROR"
            },
            "ReferenceLinks": "",
            "Title": "Related topic B",
            "Labels": "",
            "CreationDate": "2017-05-22T12:12:15.621Z",
            "CreationAuthor": "Architect@example.com",
            "ModifiedDate": "2017-05-22T12:12:15.621Z",
            "DocumentReferences": "",
            "RelatedTopics": {
                "RelatedTopic": {
                    "@attributes": {
                        "Guid": "c69c8879-bd4a-4182-a759-f3c8c5b47c94"
                    },
                    "#text": ""
                }
            },
            "Comments": {
                "Comment": {
                    "@attributes": {
                        "Guid": "da5306a4-b02c-43f9-aeba-602bc4db925a"
                    },
                    "Date": "2017-05-22T12:12:15.621Z",
                    "Author": "Architect@example.com",
                    "Comment": "#[c69c8879-bd4a-4182-a759-f3c8c5b47c94]"
                }
            },
            "Viewpoints": {
                "ViewPoint": [
                    {
                    "@attributes": {
                        "Guid": "a6f801b9-6bf6-4cb9-8b89-1ae24b76074a"
                    },
                    "Viewpoint": "viewpoint-f99eb1ed-6bd2-46da-95f1-663a86d5a38d.bcfv",
                    "Snapshot": "snapshot-f99eb1ed-6bd2-46da-95f1-663a86d5a38d.bcfv"
                    },
                    {
                    "@attributes": {
                        "Guid": "a6f801b9-6bf6-4cb9-8b89-1ae24b76074a"
                    },
                    "Viewpoint": "viewpoint-f99eb1ed-6bd2-46da-95f1-663a86d5a38d.bcfv",
                    "Snapshot": "snapshot-f99eb1ed-6bd2-46da-95f1-663a86d5a38d.bcfv"
                    }
                ]
            }
        }
    }
}

# Build XML tree
root_tag = list(json_data.keys())[0]
root_element = json_to_element(root_tag, json_data[root_tag])
tree = ET.ElementTree(root_element)
ET.indent(tree, space = "    ", level = 0)
# Write to file
bcf_filepath = "C:\\Users\\Chun\\Downloads\\output.bcf"
with open(bcf_filepath, "wb") as bcf_file:
    bcf_file.write(b'<?xml version="1.0" encoding="UTF-8" standalone = "yes"?>\n')

with open(bcf_filepath, "ab") as bcf_file:
    tree.write(bcf_file, encoding="UTF-8", xml_declaration=False, short_empty_elements = False)

