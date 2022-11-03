# Des Instructions :
# À l'aide des modules de requêtes et de temps , créez une fonction qui renvoie le temps de chargement d'une page Web (combien de temps il faut pour une réponse complète à une requête).
# Testez votre code avec plusieurs sites tels que google, ynet, imdb, etc.

from urllib.request import urlopen
from time import time
site_internet="https://www.google.fr/" #0.069 secondes
# site_internet="https://www.geeksforgeeks.org/" 0.239 secondes

site=urlopen(site_internet)
#temps de debut
temps_epoque=time()
#lire tout le site
lire=site.read()
#on stocke le temps ecouler jusqua la fin de la lecture
nb_seconde=time()
site.close()
temps_site=round(nb_seconde-temps_epoque,3)
print("Le temps de chargement du site ",site_internet," est ",temps_site,"secondes")