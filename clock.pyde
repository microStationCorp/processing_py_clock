svelocity = -90
mvelocity = -90
hvelocity = -90
radious = 200
sradious = radious - 20
mradious = radious - 30
hradious = radious - 60

numbers = []

def setup():
    size(600, 600)
    frameRate(60)
    for i in range(-90, 270, 30):
        numbers.append([radious * cos(radians(i)), radious * sin(radians(i)),
                        (radious - 10) * cos(radians(i)), (radious - 10) * sin(radians(i))])

def draw():
    translate(width / 2, height / 2)
    background(51)
    secPointer()
    minPointer()
    hPointer()
    clockFig()


def clockFig():
    global radious, numbers
    ellipseMode(CENTER)
    noFill()
    stroke(255)
    strokeWeight(4)
    # ellipse(0, 0, radious * 2, radious * 2)
    fill(255)
    ellipse(0, 0, 3, 3)
    for n in numbers:
        line(n[0], n[1], n[2], n[3])

def hPointer():
    global hvelocity, hradious
    x = hradious * cos(radians(hvelocity))
    y = hradious * sin(radians(hvelocity))
    stroke(255, 87, 34)
    strokeWeight(6)
    line(0, 0, x, y)
    hvelocity += 0.00014
    if hvelocity > 180:
        hvelocity = -179

def minPointer():
    global mvelocity, mradious
    x = mradious * cos(radians(mvelocity))
    y = mradious * sin(radians(mvelocity))
    stroke(33, 223, 248)
    strokeWeight(4)
    line(0, 0, x, y)
    mvelocity += 0.0017
    if mvelocity > 180:
        mvelocity = -179

def secPointer():
    global svelocity, sradious
    x = sradious * cos(radians(svelocity))
    y = sradious * sin(radians(svelocity))
    stroke(255, 100, 225)
    strokeWeight(3)
    line(0, 0, x, y)
    svelocity += 0.1
    if svelocity > 180:
        svelocity = -179
