# coding=utf-8
import pygame
import time
from pygame.locals import *
import random

screenW = 480 # window宽度
screenH = 700 # window高度

# 子弹基类
class BaseBullet(object):
  X = 0
  Y = 0
  def __init__(self, X = 0, Y = 0, type = ''):
    self.X = X
    self.Y = Y
    self.type = ''
  def judge(self):
    if self.type == 'enemy': # 敌机
      return True if self.Y > screenH else False
    elif self.type == 'bullet': # 飞机
      return True if self.Y < 0 else False

# 飞机
class HeroPlan(object):
  X = 0 # 飞机所在的X轴
  Y = 0 # 飞机所在的Y轴
  def __init__(self, W, H, url, screen):
    self.W = W
    self.H = H
    self.X = (screenW - W) / 2
    self.Y = screenH - H
    self.screen = screen
    self.urlObj = pygame.image.load(url)
    self.bullet_list = []
  # 显示飞机
  def display(self):
    self.screen.blit(self.urlObj, (self.X, self.Y))

    for bullet in self.bullet_list:
      bullet.display()
      bullet.move()
      if bullet.judge():
        self.bullet_list.remove(bullet)
  # 飞机移动
  def move(self):
    # 获取事件(检测键盘)
    for event in pygame.event.get():
      if event.type == QUIT:
        print('exit')
        exit()
      elif event.type == KEYDOWN:
        if event.key == K_a or event.key == K_LEFT:
          print('left')
          self.move_left()
        elif event.key == K_d or event.key == K_RIGHT:
          print('right')
          self.move_right()
        elif event.key == K_SPACE:
          print('space')
  def move_left(self):
    self.X -= 5
  def move_right(self):
    self.X += 5
  def fire(self):
    self.bullet_list.append(Bullet('./feiji/bullet.png', self.screen, self.X, self.Y, self.W, self.H))
 
# 飞机子弹
class Bullet(BaseBullet):
  W = 22
  H = 22
  speed = 5
  def __init__(self, url, screen, X, Y, planW, planH):
    self.X = X + (planW - self.W / 2 - 4) / 2
    self.Y = Y - self.H
    self.screen = screen
    self.image = pygame.image.load(url)
  def display(self):
    self.screen.blit(self.image, (self.X, self.Y))
  def move(self):
    self.Y -= self.speed
  # 小球是否越界
  def judge(self):
    baseBullet = BaseBullet(self.X, self.Y, 'bullet')
    return baseBullet.judge()

# 敌机
class EnemyPlan(object):
  X = 0 # 飞机所在的X轴
  Y = 0 # 飞机所在的Y轴
  speed = 4
  dir = 'right'
  def __init__(self, W, H, url, screen):
    self.W = W
    self.H = H
    self.X = 0
    self.Y = 0
    self.screen = screen
    self.urlObj = pygame.image.load(url)
    self.bullet_list = []

  # 显示飞机
  def display(self):
    self.screen.blit(self.urlObj, (self.X, self.Y))

    for bullet in self.bullet_list:
      bullet.display()
      bullet.move()
      if bullet.judge():
        self.bullet_list.remove(bullet)

  def move(self):
    if self.dir == 'right':
      self.X += self.speed
      if self.X > screenW - self.W:
        self.dir = 'left'
    elif self.dir == 'left':
      self.X -= self.speed
      if self.X < 0:
        self.dir = 'right'

  def fire(self):
    random_num = random.randint(1, 100)
    if random_num == 8 or random_num == 20:
      self.bullet_list.append(EnemyBullet('./feiji/bullet1.png', self.screen, self.X, self.H, self.W, self.H))

# 敌机子弹
class EnemyBullet(BaseBullet):
  W = 9
  H = 21
  speed = 4
  def __init__(self, url, screen, X, Y, planW, planH):
    self.X = X
    self.Y = Y
    self.screen = screen
    self.image = pygame.image.load(url)
  def display(self):
    self.screen.blit(self.image, (self.X, self.Y))
  def move(self):
    self.Y += self.speed
  # 小球是否越界
  def judge(self):
    baseBullet = BaseBullet(self.X, self.Y, 'enemy')
    return baseBullet.judge()

# 键盘检测
def key_control(aircraft):
  # 获取事件(检测键盘)
  for event in pygame.event.get():
    if event.type == QUIT:
      print('exit')
      exit()
    elif event.type == KEYDOWN:
      if event.key == K_a or event.key == K_LEFT:
        print('left')
        aircraft.move_left()
      elif event.key == K_d or event.key == K_RIGHT:
        print('right')
        aircraft.move_right()
      elif event.key == K_SPACE:
        print('space')
        aircraft.fire()

# 入口
def main():
  # 创建窗口
  depth = 32
  screen = pygame.display.set_mode((screenW, screenH), 0, depth)

  # 载入背景图片
  bg = pygame.image.load('./feiji/background.png')

  # 飞机
  hero = HeroPlan(100, 124, './feiji/hero1.png', screen)
  # 敌机
  enemy = EnemyPlan(51, 39, './feiji/enemy0.png', screen)

  while True:
    # 设定需要显示的图片
    screen.blit(bg, (0, 0))
    hero.display()
    enemy.display()

    # 更新需要显示的内容
    pygame.display.update()

    # 移动
    key_control(hero)
    enemy.move()
    enemy.fire()
    time.sleep(0.01)

if __name__ == '__main__':
  main()
