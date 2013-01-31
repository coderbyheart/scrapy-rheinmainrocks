import re
import os

class RheinmainrocksPipeline(object):
    def process_item(self, item, spider):
        nickname = re.sub("[^A-Za-z0-9]", "", unicode(item["name"]).lower())
        filename=nickname + ".xml"
        with open(filename, "w") as x:
            writeln = lambda s: x.write(s + os.linesep)
            writeln('<?xml version="1.0" encoding="UTF-8"?>')
            writeln('<usergroup xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="../xsd/usergroup.xsd">')
            writeln('    <name>%s</name>' % unicode(item['name']))
            writeln('    <nickname>%s</nickname>' % unicode(nickname))
            writeln('    <description>%s</description>' % unicode(item['location']))
            writeln('    <url>%s</url>' % unicode(item['url']))
            writeln('    <tags>')
            for tag in unicode(item['subject']).split(','):
                writeln('        <tag>%s</tag>' % tag.strip())
            writeln('    </tags>')
            writeln('</usergroup>')
        return item
