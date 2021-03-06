import torch


class hparams:
    def __init__(self):
        self.train_scp = "../input/voicebank/dataset/train_segan.scp"
        self.train_scp_eng = "../input/voicebank/dataset/train_segan_english.scp"
        self.train_scp_chi = "../input/voicebank/dataset/train_segan_chinese.scp"
        self.save_path = "save/voicebank/"

        self.train_mode = 0

        self.ref_batch_size = 128  # 400 VirtualBatchNorm1d的参考数据批量大小
        self.batch_size = 128   # 128



        self.n_epoch = 100
        self.size_z = (1024, 8)  # z的形状

        self.fs = 16000  # 读取音频数据的采样率
        self.win_len = 16384  # 切割音频段的长度

