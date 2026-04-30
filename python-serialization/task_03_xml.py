#!/usr/bin/env python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    # Root element yaradırıq
    root = ET.Element("data")

    # Dictionary içində gəzirik
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # XML string saxlayır

    # XML tree yaradıb fayla yazırıq
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    # XML faylı oxuyuruq
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}

    # Elementləri dictionary-ə çeviririk
    for child in root:
        result[child.tag] = child.text

    return result
