import re
from beancount.ingest import importer
from beancount_dbs import utils

class Importer(importer.ImporterProtocol):
    def identify(self, file):
        if file.mimetype() != 'application/pdf':
            return False
        text = file.convert(utils.pdf_to_text)
        print(f"text: {text}")
        if text:
            return re.search('Bank code +024', text) is not None