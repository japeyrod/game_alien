class Settings():
    """设置类"""


    def __init__(self):
        #初始化
        self.scrennt_width = 800
        self.scrennt_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1

        #子弹
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allow = 3