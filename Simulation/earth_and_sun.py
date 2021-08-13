
G = 6.67e-11
def get_force(object1,object2):
    
    
    force_vec = -(G*object1.mass*object2.mass/((mag(object1.pos-object2.pos)))**2)*((object1.pos-object2.pos)/(mag(object1.pos-object2.pos)))
    
    return force_vec
    
#ang_mom = (1.496e9**2 * 2*3.14159 * 5.972e24)  / 31557600
#y = ang_mom/(147.1e9*5.972e24)

we = 2.0415560107360918e-07 #math.sqrt(G*1.989e30/147.1e9**3) 
wm = 2.6481815042775373e-06 #math.sqrt(G*5.972e24/384400e3**3)

sun = sphere( pos=vector(0,0,0), radius=696.3e6*100, color=color.yellow,
               mass = 1.989e30, momentum=vector(0, 0, 0), make_trail=True )
     
earth = sphere(pos=vector(147.1e9,0,0), radius=6.371e6*1000, texture=textures.earth,
               mass = 5.972e24, momentum=vector( 0, 147.1e9*we*5.972e24, 0), make_trail=True )

moon = sphere( pos=earth.pos+vector(-384400e3,0,0), radius=1.7371e6*100, color=color.white,
               mass = 7.348e22, momentum=vector(0, 0, 0), make_trail=True )

moon.momentum = moon.mass*(earth.momentum/earth.mass+vector(0,384400e3*wm,0))

dt = 100000
t = 0
while (True):
    rate(10000)
    print(earth.momentum)

    sun.force = get_force(sun,earth)
    earth.force = get_force(earth,sun)
    moon.force = get_force(moon,earth)
    
    sun.momentum = sun.momentum + sun.force*dt
    earth.momentum = earth.momentum + earth.force*dt
    moon.momentum = moon.momentum + moon.force*dt
    
    sun.pos = sun.pos + sun.momentum*dt /sun.mass
    earth.pos = earth.pos + earth.momentum*dt /earth.mass
    moon.pos = moon.pos + moon.momentum*dt /moon.mass

    t = t + dt