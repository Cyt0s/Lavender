

class HDFS(object):
    def __init__(self,sc):
        self.URI = sc._gateway.jvm.java.net.URI
        self.Path = sc._gateway.jvm.org.apache.hadoop.fs.Path
        self.FileSystem = sc._gateway.jvm.org.apache.hadoop.fs.FileSystem
        self.fs = self.FileSystem.get(self.URI("hdfs://somehost:8020"), sc._jsc.hadoopConfiguration())



    def list_dir(self, dir_to_list):
        return self.fs.listStatus(self.Path(dir_to_list))


    def rm(self, dir_to_remove):
        return self.fs.delete(self.Path(dir_to_remove))


    def create_dir(self,dir_to_create):
        return self.fs.mkdirs(self.Path(dir_to_create))


    def is_dir_exists(self,dir_to_check):
        return self.fs.exists(self.Path(dir_to_check))


    def move(self, src_dir, dest_dir):
        return self.fs.rename(self.Path(src_dir), self.Path(dest_dir))


    def copy_dir_content(self, dir_to_copy_from, destination_dir):
        for pathStatus in self.list_dir(dir_to_copy_from):
            self.move(pathStatus.getPath(), destination_dir)