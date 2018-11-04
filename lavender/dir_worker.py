class DirWorker(object):
    def __init__(self, fs, path, file_worker):
        self.fs = fs
        self.Path = path
        self.file_worker = file_worker

    def ls(self, dir_to_list):
        if self.fs.isDirectory(self.Path(dir_to_list)):
            return self.fs.listStatus(self.Path(dir_to_list))

    def does_dir_exist(self, dir_to_check):
        if self.fs.isDirectory(self.Path(dir_to_check)):
            return self.fs.exists(self.Path(dir_to_check))

    def move_dir_content(self, src_dir, dst_dir):
        if self.fs.isDirectory(self.Path(src_dir)):
            for fileStatus in self.ls(src_dir):
                self.file_worker.mv(fileStatus.getPath(), dst_dir)

    def mkdir(self, dir_to_create):
        if self.fs.isDirectory(self.Path(dir_to_create)):
            return self.fs.mkdirs(self.Path(dir_to_create))

    def rmdir(self, dir_to_delete):
        if self.fs.isDirectory(self.Path(dir_to_delete)):
            return self.file_worker.rm(self.Path(dir_to_delete))

    def get_dir_size(self, dir_to_sample):
        if self.fs.isDirectory(self.Path(dir_to_sample)):
            return self.fs.getContentSummary(self.Path(dir_to_sample)).getSpaceConsumed()

    def get_dir_file_count(self, dir_to_sample):
        if self.fs.isDirectory(self.Path(dir_to_sample)):
            return self.fs.getContentSummary(self.Path(dir_to_sample)).getFileCount()
