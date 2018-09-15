class Settings():
    """设置类"""


    def __init__(self):
        #初始化
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_limit = 2

        #子弹
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allow = 3

        #外星人
        self.fleet_drop_speed = 50


        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 10
        self.bullet_speed_factor = 20
        self.alien_speed_factor = 20
        # 1向右 -1向左
        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        """提高速度"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
