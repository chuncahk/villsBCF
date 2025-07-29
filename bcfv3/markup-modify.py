import xml.etree.ElementTree as ET

def update_creation_date(xml_path, new_date, output_path=None):
    """
    Updates the <CreationDate> element in the XML file.
    Parameters:
    - xml_path (str): Path to the input XML file.
    - new_date (str): New date string in ISO 8601 format (e.g., "2000-01-01T12:00:00.000Z").
    - output_path (str, optional): Path to save the modified XML. If None, overwrites the original file.
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Find the CreationDate element
    creation_date_elem = root.find(".//CreationDate")
    if creation_date_elem is not None:
        creation_date_elem.text = new_date
        tree.write(output_path or xml_path, encoding="utf-8", xml_declaration=True)
        print(f"CreationDate updated to {new_date}")
    else:
        print("CreationDate element not found.")

# Example usage:
# update_creation_date("markup.xml", "2025-05-26T12:00:00.000Z")


def update_topic_guid(xml_path, new_guid, output_path=None):
    """
    Updates the Guid attribute of the <Topic> element in the XML file.
    Parameters:
    - xml_path (str): Path to the input XML file.
    - new_guid (str): New GUID string to set.
    - output_path (str, optional): Path to save the modified XML. If None, overwrites the original file.
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()
    # Find the Topic element and update its Guid attribute
    topic_elem = root.find(".//Topic")
    if topic_elem is not None:
        topic_elem.set("Guid", new_guid)
        tree.write(output_path or xml_path, encoding="utf-8", xml_declaration=True)
        print(f"Topic Guid updated to {new_guid}")
    else:
        print("Topic element not found.")