# -*- coding: utf-8 -*-
from lxml import etree
root = etree.Element("root")
print(root.tag)
etree.SubElement(root,"child1")
etree.SubElement(root,"child2")
print(etree.tostring(root))
