import pygame as py
from pygame.locals import *
import random
from sys import exit

#PyGame Başlatma Aracı
py.init() #init -> initialize = Başlatmak demektir.

#Pygame için ekranımızı tasarlayalım.
screen = py.display.set_mode((800,600),0,32) #Ekran Ayarı
py.display.set_caption("Ping Pong Game!") #Ekran Başlığı

#Oyundaki iki barı tasarlayalım.
back = py.Surface((800,600)) #Pencerenin yüzeyini belirle
background = back.convert() #800x600 ekranı oyun alanı haline getir.
background.fill((0,0,0)) #RGB ->Red,Green,Blue -> arkaplan rengi

#BARLAR -> İki barın ortak özelliği
bar = py.Surface((10,50))  #10 genişlik, 50 yükseklik
#Bar1'in Özellikleri
bar1 = bar.convert()
bar1.fill((0,0,255)) #Bar1 mavi
#Bar2'nin Özellikleri
bar2 = bar.convert()
bar2.fill((0,255,0)) #Bar2 yeşil

#Topun Özellikleri
circle_sur = py.Surface((15,15)) #Topun genişlik ve yükseklik ayarı
circ=py.draw.circle(circle_sur, (255,0,0),(15/2,15/2),15/2)#Çemberi çiz
circle = circle_sur.convert() #Topu ekranda oluştur



#penceremin aktif olarak ekranda kalmasını sağlayalım.
while True: #For sayısal, while mantıksal bir döngüdür.
    py.display.update() #Ekranı güncelle ve aktif kalsın.