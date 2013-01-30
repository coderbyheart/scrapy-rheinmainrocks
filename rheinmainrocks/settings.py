# Scrapy settings for rheinmainrocks project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'rheinmainrocks'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['rheinmainrocks.spiders']
NEWSPIDER_MODULE = 'rheinmainrocks.spiders'
DEFAULT_ITEM_CLASS = 'rheinmainrocks.items.RheinmainrocksItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
ITEM_PIPELINES = ['rheinmainrocks.pipelines.RheinmainrocksPipeline']
