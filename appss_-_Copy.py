import xml.etree.ElementTree as ET
import requests
import time

# parse the XML data from the string
root = ET.fromstring(open("4020dataset.xml").read())
TitleList = []
pmid_list = []

for ArticleTitle in root.iter('ArticleTitle'):
    title = print(ArticleTitle.text)
    TitleList.append(title)




for title in TitleList:
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={title}&retmode=xml"
    response = requests.get(url)
    root = ET.fromstring(response.text)
    for id in root.iter('Id'):
        print(id.text)
        pmid_list.append(id.text)

   

# extract the PMID from the XML file
pmid_list = [node.text for node in root.findall(".//Id")]

# write the PMID to a local XML-based file
root = ET.Element("PubMed")
for pmid in pmid_list:
    ET.SubElement(root, "PMID").text = pmid
tree = ET.ElementTree(root)
tree.write("groupID_result.xml")
