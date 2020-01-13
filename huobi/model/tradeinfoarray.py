import huobi.model.position
import huobi.model.bararray
import numpy as np


class TradeInfoArray:

    def __init__(self, interval, size=100):
        self.count = 0
        self.inited = False
        self.size = size
        self.ttmu_buy_ratio = np.zeros(size)
        self.ttmu_sell_ratio = np.zeros(size)
        self.ttsi_buy_ratio = np.zeros(size)
        self.ttsi_sell_ratio = np.zeros(size)
        self.ttsi_locked_ratio = np.zeros(size)
        self.market_position = np.zeros(size)
        self.id = np.zeros(size)
        self.interval = interval
        self.boll_up_array = np.zeros(size)
        self.boll_down_array = np.zeros(size)
        self.boll_mid_array = np.zeros(size)
        self.boll_up_cnt_array = np.zeros(size)
        self.boll_up_brk_cnt_array = np.zeros(size)
        self.boll_down_cnt_array = np.zeros(size)
        self.boll_down_brk_cnt_array = np.zeros(size)
        self.boll_up = 0
        self.boll_down = 0
        self.boll_mid = 0
        self.boll_up_cnt = 0
        self.boll_up_brk_cnt = 0
        self.boll_down_cnt = 0
        self.boll_down_brk_cnt = 0

    def update_ttsi(self, ttsi_list: list):
        for cc in range(len(ttsi_list)):
            self.update_ttsi_array(ttsi_list[cc])

    def update_ttsi_array(self, ttsi_list):

        self.ttsi_buy_ratio[:-1] = self.ttsi_buy_ratio[1:]
        self.ttsi_sell_ratio[:-1] = self.ttsi_sell_ratio[1:]
        self.ttsi_locked_ratio[:-1] = self.ttsi_locked_ratio[1:]
        self.ttsi_buy_ratio[-1] = ttsi_list.buy_ratio
        self.ttsi_sell_ratio[-1] = ttsi_list.sell_ratio
        self.ttsi_locked_ratio[-1] = ttsi_list.locked_ratio

    def update_ttmu(self, ttmu_list: list):
        for cc in range(len(ttmu_list)):
            self.update_ttmu_array(ttmu_list[cc])

    def update_ttmu_array(self, ttmu_list):

        self.ttmu_buy_ratio[:-1] = self.ttmu_buy_ratio[1:]
        self.ttmu_sell_ratio[:-1] = self.ttmu_sell_ratio[1:]
        self.ttmu_buy_ratio[-1] = ttmu_list.buy_ratio
        self.ttmu_sell_ratio[-1] = ttmu_list.sell_ratio

    def update_postion(self, position_list: list):
        for cc in range(len(position_list)):
            self.update_postion_array(position_list[cc])

    def update_postion_array(self, ttmu_list):

        self.market_position[:-1] = self.market_position[1:]
        self.market_position[-1] = ttmu_list.volume

    def update_boll(self, barhigh, barlow, boll_up, boll_down, ccv):
        """
        Update new bar data into array manager.
        """
        self.count += 1
        if not self.inited and self.count >= self.size:
            self.inited = True
        self.boll_up = boll_up
        self.boll_down = boll_down
        self.boll_mid = (self.boll_up + self.boll_down) / 2

        if barlow > self.boll_mid:
            self.boll_up_cnt = self.boll_up_cnt + 1
            self.boll_down_cnt = 0
        else:
            self.boll_up_cnt = 0

        if barhigh < self.boll_mid:
            self.boll_down_cnt = self.boll_down_cnt + 1
            self.boll_up_cnt = 0
        else:
            self.boll_down_cnt = 0

        if barhigh > self.boll_up:
            self.boll_up_brk_cnt = self.boll_up_brk_cnt + 1
        else:
            self.boll_up_brk_cnt = 0

        if barlow < self.boll_down:
            self.boll_down_brk_cnt = self.boll_down_brk_cnt + 1
        else:
            self.boll_down_brk_cnt = 0

        self.boll_up_cnt_array[ccv] = self.boll_up_cnt
        self.boll_up_brk_cnt_array[ccv] = self.boll_up_brk_cnt
        self.boll_down_cnt_array[ccv] = self.boll_down_cnt
        self.boll_down_brk_cnt_array[ccv] = self.boll_down_brk_cnt

    def update_boll_array(self, bar, am):
        self.boll_up_array, self.boll_down_array = am.boll(20, 2, True)
        for ccv in range(19, self.size):
            self.update_boll(bar[ccv].high, bar[ccv].low, self.boll_up_array[ccv], self.boll_down_array[ccv], ccv)

    def bollr(self, array=False):

        if array:
            return self.boll_up_array, self.boll_up_cnt_array, self.boll_up_brk_cnt_array, self.boll_down_array, self.boll_down_cnt_array, self.boll_down_brk_cnt_array
        return self.boll_up, self.boll_up_cnt, self.boll_up_brk_cnt, self.boll_down, self.boll_down_cnt, self.boll_down_brk_cnt

    def to_str(self):
        tt: str = """ Boll Array
        self.boll_up: {}, self.boll_up_cnt: {}, self.boll_up_brk_cnt: {}, self.boll_down: {}, self.boll_down_cnt：{}, self.boll_down_brk_cnt：{}
        """.format(self.boll_up, self.boll_up_cnt, self.boll_up_brk_cnt, self.boll_down, self.boll_down_cnt,
                   self.boll_down_brk_cnt)
        return tt
