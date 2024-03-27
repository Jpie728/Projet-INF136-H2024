import math


def calculer_reflexion_point(point,axe):
    if axe=='x':
        x=point[0]
        y=0-point[1]
    if axe == 'y':
        x= 0 - point[0]
        y=point[1]
    return x,y

def calculer_rotate_point(point,angle,centre):
    angle_radians = math.radians(angle)

    Qx = point[0] - centre[0]
    Qy= point[1] - centre[1]


    rot_x = Qx * math.cos(angle_radians) - Qy * math.sin(angle_radians)
    rot_y = Qx * math.sin(angle_radians) + Qy * math.cos(angle_radians)

    x1 = rot_x + centre[0]
    y1 = rot_y + centre[1]
    x1 = round(x1, 2)
    y1 = round(y1, 2)
    return x1, y1
def calculer_inclinaison_point(point,angle,direction):
    angle_radians=math.radians(angle)

    if direction=='x':
        x1=point[0]+math.tan( angle_radians)*point[1]
        y1=point[1]
    if direction=='y':
        x1=point[0]
        y1=math.tan( angle_radians)*point[0]+point[1]
    x1=round(x1,2)
    y1=round(y1,2)
    return x1,y1


