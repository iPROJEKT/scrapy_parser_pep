from datetime import datetime

BOT_NAME = 'pep_parse'
NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {'pep_parse.pipelines.PepParsePipeline': 300}
FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}
NOW_TIME = datetime.strftime(datetime.now(), '%Y-%m-%dT%H-%M-%S')

FILE_NAME = 'status_summary_'
RESULT_NAME_FOLDER = 'results'
FORMAT_FILE = '.csv'
ALLOWED_DOMAINS = 'peps.python.org'
START_URLS = 'https://peps.python.org/'
