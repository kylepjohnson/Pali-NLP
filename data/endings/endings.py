#endings of words
import os
import sys
sys.path.insert(0, './endings')
import xml.etree.ElementTree as ET

#extractive required data from xml files
def extractTextFromElement(elementName, stringofxml,out=[]):
    tree = ET.fromstring(stringofxml)
    for child in tree.iter():
        if child.tag == elementName:
            if (child.text.strip() in out):
                pass
            else:
                out.append(child.text.strip())
    return out


def listAllEndings():
    """returns a list of possible word endings"""
    grammar_fp = os.path.expanduser('~/pali_models_cltk/stem/fullGrammar4.xml')
    f = open(grammar_fp, "r")
    xml01 = f.read()
    endings = extractTextFromElement("ending",xml01)
    f.close()
    endings.sort(key=len, reverse=True)
    return endings


def listAllEndings1():
    """repitition: to be checked later"""
    # f=open("fullGrammar5.xml","r")
    fp_grammar = os.path.expanduser('~/pali_models_cltk/stem/fullGrammar4.xml')
    print(fp_grammar)
    f = open(fp_grammar, 'r')
    xml02 = f.read()
    endings = extractTextFromElement("ending", xml02)
    f.close()
    return endings


def retainEndings(elementName, out=[]):
    """returns the endings of words a particular word class only
    the input is the word class
    """
    if elementName in ["all"]:
        return listAllEndings()
    element = "{'type': '"+str(elementName)+"'}"
    out = []
    grammar_fp = os.path.expanduser('~/pali_models_cltk/stem/fullGrammar4.xml')
    root=ET.parse(grammar_fp)
    tree = root.getroot()
    for child in tree:
        if str(child.attrib) in [element]:
            for child01 in child.iter():
                if child01.tag == "ending":
                    if (child01.text.strip() in out):
                        pass
                    else:
                        out.append(child01.text.strip())
    out.sort(key=len,reverse=True)
    return out



