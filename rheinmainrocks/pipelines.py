import re

class RheinmainrocksPipeline(object):
    def process_item(self, item, spider):
        filename=re.sub("[^A-Za-z0-9]", "", unicode(item["name"]).lower()) + ".xml"
        with open(filename, "w") as x:
            x.write('<?xml version="1.0" encoding="UTF-8"?>')
            x.write('<usergroup>')
            for k in ['name','url','location','subject']:
                x.write('<%s>%s</%s>' % (k, unicode(item[k]), k))
            x.write('</usergroup>')
        return item
