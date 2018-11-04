class FileWorker(object):
    def __init__(self, fs, path, conf, file_util):
        self.fs = fs
        self.Path = path
        self.conf = conf
        self.FileUtil = file_util

    def rm(self, dir_to_remove):
        return self.fs.delete(self.Path(dir_to_remove))

    def mv(self, src_dir, dest_dir):
        return self.fs.rename(self.Path(src_dir), self.Path(dest_dir))

    def cp(self, src_dir, dst_dir):
        return self.FileUtil.copy(self.fs, self.Path(src_dir), self.fs, self.Path(dst_dir), False, self.conf)

    def rename(self, src_name_dir, dst_name_dir):
        return self.fs.rename(src_name_dir, dst_name_dir)
