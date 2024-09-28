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
circle.set_colorkey((0,0,0))

#TODO: Barların konumlarını belirle

#! Barların X konumu
bar1_x, bar2_x = 10., 790.
#! Barların Y konumu
bar1_y, bar2_y = 300., 300.
#! Topun X ve Y konumları
circle_x, circle_y = 400., 300.

#? Bar ve top ne kadar hareket edecek
#! Barların hareket değerleri

bar1_move, bar2_move = 0., 0.
#? Topun ve barların hızları ne olacak

speed_x, speed_y, speed_circle = 250.,250.,250.

#penceremin aktif olarak ekranda kalmasını sağlayalım.
while True: #For sayısal, while mantıksal bir döngüdür.

    for event in py.event.get():
        if event.type == QUIT: #Olayın tipi çıkış ise çık.
            exit()
    #!Barlar ve toplar burada gösterilecek
    
    py.display.update() #Ekranı güncelle ve aktif kalsın.