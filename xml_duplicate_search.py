import xml.etree.ElementTree as ET
import os


def parser(reviews, parent, child, file_log):
    j = 0
    for node in reviews:
        j += 1
        for i in range(len(node)):
            limits = node[i].findall(".//" + child)
            if len(limits) > 1:
                with open(file_log, "a") as input_file:
                    input_file.write(ET.tostring(node[i]) + "\n")
                    input_file.write("%s present 2 times in %s node number %d" % (child, parent, j) + "\n")


def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f


def search_xml(parent, child, file_log):
    for f in listdir_nohidden('.'):
        print " "
        print "Searching in filename %s" % f
        tree = ET.parse(open(f))
        reviews = tree.findall(".//" + parent)
        parser(reviews, parent_tag, child, file_log)
        with open(file_log, "a") as input_file:
            input_file.write("###############" + "\n")
            input_file.write("NO DUPLICATES FOUND" + "\n")
            input_file.write("End of filename %s " % f + "\n")
            input_file.write("###############" + "\n")
        print "Processed: ", f
        print "See filename: %s for details" % file_log


menu = 1
while menu:
    print '###MENU###'
    print "1. Search XML"
    print "2. Exit"
    meniu = raw_input("Enter selection: ")

    if meniu == '1':
        parent_tag = raw_input("Enter parent in which to search for duplicates: ")
        child_tag = raw_input("Enter search phrase: ")
        file_name = raw_input("Enter filename for the log: ")
        parent_tag = parent_tag.strip()
        child_tag = child_tag.strip()
        file_name = file_name.strip()
        if not file_name.startswith('.'):
            file_name = "." + file_name
        search_xml(parent_tag, child_tag, file_name)
    if meniu == '2':
        menu = 0
