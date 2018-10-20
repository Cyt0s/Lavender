class HDFSPro(object):


    def __init__(self,hdfs):
        self.hdfs=hdfs

    def move_dir_content(self,src_dir,dst_dir):
        for fileStatus in self.hdfs.list_dir(src_dir):
            self.hdfs.move(fileStatus.getPath(),dst_dir)


