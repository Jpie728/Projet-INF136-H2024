from PIL import Image
import numpy as np

def appliquer_rgb_to_gry(chemin_image_couleur, chemin_sauvegarde_gris):

    image_couleur = Image.open(chemin_image_couleur)

    image_array = np.array(image_couleur)
    print(image_array[0,0])

    hauteur, largeur, _ = image_array.shape
    print(hauteur, largeur)

    image_gris = np.zeros((hauteur, largeur), dtype=np.uint8)
    print(image_gris)

    for j in range(hauteur):
        for i in range(largeur):

            couleur_1, couleur_2, couleur_3 = image_array[j, i]

            moyenne = (int(couleur_1) + int(couleur_2) + int(couleur_3)) // 3

            image_gris[j, i] = moyenne

    image_gris = Image.fromarray(image_gris)
    image_gris.save(chemin_sauvegarde_gris)


def appliquer_transformation_1 (image_gris):
    hauteur, largeur = image_gris.shape

    resultat = np.zeros((hauteur, largeur))

    indices_voisins = [(-1, -1), (-1, 0), (-1, 1), (0, 1),(1,1), (1,0),(1, -1), (0, -1)]

    for i in range(1,hauteur-1):
        for j in range(1,largeur-1):

            gc = image_gris[i, j]

            code_binaire =''

            for depl_i, depl_j in indices_voisins:

                ni, nj = i + depl_i, j + depl_j

                gv = image_gris[ni, nj]

                if gv >= gc:
                    code_binaire += '1'
                else:
                    code_binaire += '0'

            valeur_dec= int(code_binaire, 2)

            resultat[i, j] = valeur_dec

    return resultat



def appliquer_transformation_2(image_gris, rayon):

    hauteur, largeur = image_gris.shape


    resultat = np.zeros((hauteur, largeur))

    for i in range(rayon, hauteur - rayon):
        for j in range(rayon, largeur - rayon):

            nouvelle_valeur = (
                    np.log10(
                        1 + abs(image_gris[i, j + rayon] - 2 * image_gris[i, j] + image_gris[i, j - rayon])) +
                    np.log10(
                        1 + abs(image_gris[i + rayon, j] - 2 * image_gris[i, j] + image_gris[i - rayon, j])) +
                    np.log10(1 + abs(image_gris[i - rayon, j + rayon] - 2 * image_gris[i, j] +
                        image_gris[i+ rayon, j - rayon]))
            )

            resultat[i, j] = int(nouvelle_valeur)


    return resultat


