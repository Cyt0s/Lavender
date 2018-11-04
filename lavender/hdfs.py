

class HDFS(object):
    def __init__(self, sc, namenode_uri):
        self.URI = sc._gateway.jvm.java.net.URI
        self.Path = sc._gateway.jvm.org.apache.hadoop.fs.Path
        self.FileSystem = sc._gateway.jvm.org.apache.hadoop.fs.FileSystem
        self.FileUtil = sc._gateway.jvm.org.apache.fs.FileUtil
        self.conf = sc._jsc.hadoopConfiguration()
        self.fs = self.FileSystem.get(self.URI(namenode_uri), self.conf)

    def ls(self, dir_to_list):
        return self.fs.listStatus(self.Path(dir_to_list))

    def rm(self, dir_to_remove):
        return self.fs.delete(self.Path(dir_to_remove))

    def mkdir(self, dir_to_create):
        return self.fs.mkdirs(self.Path(dir_to_create))

    def does_dir_exist(self, dir_to_check):
        return self.fs.exists(self.Path(dir_to_check))

    def mv(self, src_dir, dest_dir):
        return self.fs.rename(self.Path(src_dir), self.Path(dest_dir))

    def get_dir_size(self, dir_to_sample):
        return self.fs.getFileStatus(self.Path(dir_to_sample)).getBlockSize()

    def cp(self, src_dir, dst_dir):
        return self.FileUtil.copy(self.fs, self.Path(src_dir), self.fs, self.Path(dst_dir), False, self.conf)
