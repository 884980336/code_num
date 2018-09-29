import zipfile
import sys
import os

z = zipfile.ZipFile(r"D:\zip_test.zip")
# z.extractall()
print(z.namelist())

# for i, j, k in os.walk(os.path.dirname(os.path.abspath(__file__))):
#     print(i,k)
    # print(j)
    # print(k)

# import uuid
# u = uuid.uuid1()
# print(str(u)[24:])
#  addc22ec-c0a2-11e8-b0ee-96e97919fd53


def print_directory_contents(sPath, lis):
    import os

    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath, lis)
        else:
            lis.append(sChildPath)

class zip:

    def __init__(self, path):
        self.path = os.path.dirname(path)
        z = zipfile.ZipFile(path)
        z.extractall(self.path)
        z.close()
        os.remove(path)

    def line_count(self):
        lis = []
        print_directory_contents(self.path, lis)
        i = 0
        for i in lis:
            cls = i.spilt(".")[-1]
            if hasattr(sys.modules.get("__main__"), cls):
                i += getattr(sys.modules.get("__main__"), cls)(i).line_count()

        return i


