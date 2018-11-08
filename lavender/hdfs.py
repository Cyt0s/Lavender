from dir_worker import DirWorker
from file_worker import FileWorker
from fs_properties import FsProperties

class HDFS(object):
    def __init__(self, sc):
        self.URI = sc._gateway.jvm.java.net.URI
        self.Path = sc._gateway.jvm.org.apache.hadoop.fs.Path
        self.FileSystem = sc._gateway.jvm.org.apache.hadoop.fs.FileSystem
        self.FileUtil = sc._gateway.jvm.org.apache.fs.FileUtil
        self.conf = sc._jsc.hadoopConfiguration()
        self.fs = self.FileSystem.get(self.URI(self.conf.get('fs.defaultFS')), self.conf)
        self.file_worker = FileWorker(self.fs, self.Path, self.conf, self.FileUtil)
        self.dir_worker = DirWorker(self.fs, self.Path, self.file_worker)
        self.fs_properties = FsProperties(self.fs)
