from vpython import *
#GlowScript 3.0 VPython

    #Momentum=orbitalVelocity*1000*mass
    #pos=vector([distance from sun]*10**9)

#background color
scene.background=color.black
scene.opacity=0.7


#planet variables
sun = sphere( pos=vector(0,0,0), radius=170*10**8, color=color.yellow, mass=2.0*10**30, momentum=vector(0,0,0), make_trail=True, texture = "http://i.imgur.com/yoEzbtg.jpg" )
mercury = sphere( pos=vector(57.6*10**9,0,0), radius=4879*10**6, mass=0.33*10**24, momentum=vector(0,15642*10**24,0), visible=False )
venus = sphere(pos=vector(108.2*10**9,0,0), radius=12104*10**6, mass=4.87*10**24, momentum=vector(0,170450*10**24,0), visible=False )
earth = sphere( pos=vector(150*10**9,0,0), radius=12756*10**6, mass=6*10**24, momentum=vector(0,180000*10**24,0), visible=False )
mars = sphere( pos=vector(243*10**9,0,0), radius=6792*10**6, mass=6.39*10**23, momentum=vector(0,24000*6.39*10**23,0), visible=False )
jupiter = sphere(pos=vector(778*10**9,0,0), radius=142984*10**6, mass=1898*10**24, momentum=vector(0,24.86*10**30,0), visible=False )
saturn = sphere(pos=vector(1433.5*10**9,0,0), radius=120536*10**6, mass=568*10**24, momentum=vector(0,5.51*10**30,0), visible=False )
uranus = sphere(pos=vector(2872.5*10**9,0,0), radius=51118*10**6, mass=86.8*10**24, momentum=vector(0,5.9*10**29,0), visible=False )
neptune = sphere(pos=vector(4495.1*10**9,0,0), radius=49528*10**6, mass=102*10**24, momentum=vector(0,5.51*10**29,0), visible=False )

#Setting planet textures
mercury.texture = "https://i.imgur.com/tJV7qzf.png"
venus.texture = "https://i.imgur.com/7VTEX2w.jpeg"
earth.texture = textures.earth
mars.texture = "https://i.imgur.com/Mwsa16j.jpeg"
jupiter.texture = "https://i.imgur.com/RMMtt0K.jpeg"
saturn.texture = "https://i.imgur.com/5Pur4IE.jpeg"
uranus.texture = "https://i.imgur.com/2kZNvFw.jpeg"
neptune.texture = "https://i.imgur.com/lyLpoMk.jpeg"

#Attaching trails
me = attach_trail(mercury, color=color.white)
v = attach_trail(venus, color=color.orange)
e = attach_trail(earth, color=color.green)
ma = attach_trail(mars, color=color.red)
j = attach_trail(jupiter, color=color.purple)
s = attach_trail(saturn, color=color.yellow)
u = attach_trail(uranus, color=color.cyan)
n = attach_trail(neptune, color=color.blue)

#planet visibility
#mercury
def meVisibility(b):
    if b.checked:
        mercury.visible=True
    else:
        mercury.visible=False
        me.clear()
checkbox(bind=meVisibility, text='Mercury')
#venus
def vVisibility(b):
    if b.checked:
        venus.visible=True
    else:
        venus.visible=False
        v.clear()
checkbox(bind=vVisibility, text='Venus')
#earth
def eVisibility(b):
    if b.checked:
        earth.visible=True
    else:
        earth.visible=False
        e.clear()
checkbox(bind=eVisibility, text='Earth')
#mars
def maVisibility(b):
    if b.checked:
        mars.visible=True
    else:
        mars.visible=False
        ma.clear()
checkbox(bind=maVisibility, text='Mars')
#jupiter
def jVisibility(b):
    if b.checked:
        jupiter.visible=True
    else:
        jupiter.visible=False
        j.clear()
checkbox(bind=jVisibility, text='Jupiter')
#saturn
def sVisibility(b):
    if b.checked:
        saturn.visible=True
    else:
        saturn.visible=False
        s.clear()
checkbox(bind=sVisibility, text='Saturn')
#uranus
def uVisibility(b):
    if b.checked:
        uranus.visible=True
    else:
        uranus.visible=False
        u.clear()
checkbox(bind=uVisibility, text='Uranus')
#neptune
def nVisibility(b):
    if b.checked:
        neptune.visible=True
    else:
        neptune.visible=False
        n.clear()
checkbox(bind=nVisibility, text='Neptune')


#Defining Gforce
def gforce( object1,object2 ):
    G = 6.67*10**(-11)
    distanceVector =object1.pos-object2.pos
    distance = mag(distanceVector)
    directionVector = distanceVector / distance
    force = G*object1.mass*object2.mass / (distance**2)
    forceVector = force*directionVector
    return forceVector


#Run/Pause button
running = True
def Run(b):
    global running, remember_dt, dt
    running = not running
    if running:
        b.text = "Pause"
        dt = remember_dt
        color.red
    else:
        b.text = "Run"
        remember_dt = dt
        dt = 0
        color.green
    return
button(text="Pause", pos = scene.title_anchor, bind=Run )


#Reset button
def Reset(c):
    global t, mercury
    running = False
    t=0
#mercury
    me.clear()
    mercury.pos=vector(57.6*10**9,0,0)
    mercury.momentum=vector(0,15642*10**24,0)
#venus
    v.clear()
    venus.pos=vector(108.2*10**9,0,0)
    venus.momentum=vector(0,170450*10**24,0)
#earth
    e.clear()
    earth.pos=vector(150*10**9,0,0)
    earth.momentum=vector(0,18*10**28,0)
#mars
    ma.clear()
    mars.pos=vector(243*10**9,0,0)
    mars.momentum=vector(0,24000*6.39*10**23,0)
#jupiter
    j.clear()
    jupiter.pos=vector(778*10**9,0,0)
    jupiter.momentum=vector(0,24.86*10**30,0)
#saturn
    s.clear()
    saturn.pos=vector(1433.5*10**9,0,0)
    saturn.momentum=vector(0,5.51*10**30,0)
#uranus
    u.clear()
    uranus.pos=vector(2872.5*10**9,0,0)
    uranus.momentum=vector(0,5.9*10**29,0)
#neptune
    n.clear()
    neptune.pos=vector(4495.1*10**9,0,0)
    neptune.momentum=vector(0,5.51*10**29,0)
    
button(text="Reset", pos = scene.title_anchor, bind=Reset)


dt = 30
t = 0
while (True):
    rate(200000)
    
#rotating the sun
    rotationSpeed=0.000001
    sun.rotate(axis=vector(0,1,0), angle=rotationSpeed*dt)


#Mercury to the sun
    mercury.force = gforce( sun,mercury )
    mercury.pos = mercury.pos + mercury.momentum/mercury.mass*dt
    mercury.momentum = mercury.momentum + mercury.force*dt
    t = t + dt   
#Venus to the sun
    venus.force = gforce( sun,venus )
    venus.pos = venus.pos + venus.momentum/venus.mass*dt
    venus.momentum = venus.momentum + venus.force*dt
    t = t + dt
#Earth to the sun
    earth.force = gforce( sun,earth )
    earth.pos = earth.pos + earth.momentum/earth.mass*dt
    earth.momentum = earth.momentum + earth.force*dt
    t = t + dt 
#Mars to the sun
    mars.force = gforce( sun,mars )
    mars.pos = mars.pos + mars.momentum/mars.mass*dt
    mars.momentum = mars.momentum + mars.force*dt
    t = t + dt
#Jupiter to the sun
    jupiter.force = gforce( sun,jupiter )
    jupiter.pos = jupiter.pos + jupiter.momentum/jupiter.mass*dt
    jupiter.momentum = jupiter.momentum + jupiter.force*dt
    t = t + dt
#Saturn to the sun
    saturn.force = gforce( sun,saturn )
    saturn.pos = saturn.pos + saturn.momentum/saturn.mass*dt
    saturn.momentum = saturn.momentum + saturn.force*dt
    t = t + dt
#Uranus to the sun
    uranus.force = gforce( sun,uranus )
    uranus.pos = uranus.pos + uranus.momentum/uranus.mass*dt
    uranus.momentum = uranus.momentum + uranus.force*dt
    t = t + dt
#Neptune to the sun
    neptune.force = gforce( sun,neptune )
    neptune.pos = neptune.pos + neptune.momentum/neptune.mass*dt
    neptune.momentum = neptune.momentum + neptune.force*dt
    t = t + dt
