# import turtle
# wn = turtle.Screen()   #these called construction functions
# sena = turtle.Turtle()  #sena is not a str,int etc. it is a turtle object
# sena.forward(200)
# sena.left(90)      
# sena.forward(100)
# sena.left(90)       #you can say sena.right(-90) or sena.right(270) too
# sena.forward(200)
# sena.left(90)
# sena.forward(100)

# wn.exitonclick()   #makes the drawing stay on screen until you manually close it.


#import turtle

# wn = turtle.Screen()
# wn.bgcolor("seagreen")
# leo = turtle.Turtle()
# leo.color("peachpuff")
# leo.pensize(2)
# leo.shape("turtle")


# leo.forward(200)
# leo.left(120)
# leo.forward(200)
# leo.left(120)
# leo.forward(200)
# leo.left(120)

# ücgen yaptım leo yu dış acısıyla, cokgenlerin dış acıları 360/n


# judas = turtle.Turtle()
# judas.color("lightskyblue")
# judas.pensize(2)

# judas.forward(100)
# judas.left(36)
# judas.forward(100)
# judas.left(36)
# judas.forward(100)
# judas.left(36)
# judas.forward(100)
# judas.left(36)
# judas.forward(100)
# judas.left(36)
# judas.forward(100)
# judas.left(36)
# judas.forward(100)
# judas.left(36)
# judas.forward(100)
# judas.left(36)
# judas.forward(100)
# judas.left(36)
# judas.forward(100)
# judas.left(36)


# wn.exitonclick()


# loop (for döngüsü)

# for name in ["asiye" , "sema", "melek", "yeter", "ciğdem" , "zeynep"]:
#     print("Merhaba!!!!" , name ,"seni çok özledim")
#     print("loop finished") # döngünün içinde tab le ikinci
#  satırı forun altına yazarsan loopun için de olur her liste elementi için bunu yazıcak


# print("loop finished") # loop döngüsünden çıktığın için bir kere yazacak

#100gen cizzzzz range kullanıcaz range(3) liste elemanı ismi
#önemli değilse tane eleman 0,1,2 verir 3 döngü ,range(3,5) range 3 den baslar
#  5 e kadar (5 dahil değil) sayı verir 3,4 
# range(0,13,2) 0 dan 13e 13 dahil olmamak üzere 2şer olarak sayar.


# print(list(range(4)))
# print(list(range(7,35)))
# print(list(range(2,37,2)))

import turtle

wn = turtle.Screen()
wn.bgcolor("white")
giant = turtle.Turtle()
giant.pensize(2)
giant.shape("turtle")


# for i in range(100):  #i döngünün adı sakın turtle opjenin adını verme!!!!!
#     giant.forward(160)
#     giant.left(3.6)

for aColor in ["lightcoral", "turquoise" , "darkcyan" , "darkorchid" , "gold"]:
    giant.color(aColor)
    giant.forward(60)
    giant.left(72)

wn.exitonclick()


