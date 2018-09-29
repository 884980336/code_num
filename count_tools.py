import docx as word
import zipfile
import sys
import os
class Py:

    def __init__(self, path):
        self.path = path

    def line_count(self):

        try:
            count = 0
            with open(self.path, encoding="gbk") as f:
                for i in f:
                    if i and not i.startswith("#"):
                        count+=1

        except UnicodeDecodeError:
            count = 0
            with open(self.path, encoding="utf8") as f:
                for i in f:
                    if i and not i.startswith("#"):
                        count += 1
        return count


Html = Txt = Py


class Docx:

    def __init__(self, path):
        self.path = path

    def line_count(self):
        count = 0
        file = word.Document(self.path)
        for i in file.paragraphs:
            if i.text and not i.text.startswith("#"):
                count+=1
        return count


def print_directory_contents(sPath, lis):
    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath, lis)
        else:
            lis.append(sChildPath)


class Zip:

    def __init__(self, path):
        self.path = os.path.dirname(path)
        z = zipfile.ZipFile(path)
        z.extractall(self.path)
        z.close()
        os.remove(path)

    def line_count(self):
        lis = []
        print_directory_contents(self.path, lis)
        count = 0
        for i in lis:
            cls = i.split(".")[-1]
            sys.modules.get(__name__)
            if hasattr(sys.modules.get(__name__), cls):
                count += getattr(sys.modules.get(__name__), cls)(i).line_count()

        return count
