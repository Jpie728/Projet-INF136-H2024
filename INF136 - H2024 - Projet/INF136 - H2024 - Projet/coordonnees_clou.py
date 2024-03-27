
from transformation_geometrique import *
def calculer_coordonnees_clou(A,B,C,D,E):

    pt_0=('pt_0',(-B/2,C/2))
    pt_1=('pt_1',(-B/2,-C/2))
    pt_2=('pt_2',(-B/2-D,-A/2))
    pt_3=('pt_3',(-B/2-D,A/2))
    pk_2=('pk_2',(B/2,C/2))
    pk_1=('pk_1',(B/2,-C/2))
    pk_0=('pk_0',(B/2+E,0))

    resultat=[pt_0,pt_1,pt_2,pt_3,pk_2,pk_0,pk_1]


    return resultat

def appliquer_transormation_clou(points_clou,center_rotation,angle_rotation,direction_inclinaison,angle_inclinaison,axe_reflexion ):
    liste_reflexion=[]
    liste_rotation=[]
    liste_inclinaison=[]
    for point in points_clou:
        x,y=calculer_reflexion_point(point[1],axe_reflexion)
        liste_reflexion.append((point[0],(x,y)))
        x,y=calculer_rotate_point(point[1],angle_rotation,center_rotation)
        liste_rotation.append((point[0],(x,y)))
        x,y=calculer_inclinaison_point(point[1],angle_inclinaison,direction_inclinaison)
        liste_inclinaison.append((point[0],(x,y)))

    return liste_reflexion,liste_rotation,liste_inclinaison
