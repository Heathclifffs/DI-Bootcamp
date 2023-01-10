Projet : IMDI
IMDB For Developers Institute


Des Instructions
PARTIE III
PARTIE III.A : Comptes
Hier nous avons créé une accountsapplication, aujourd'hui nous allons travailler sur cette application spécifique

Créez 4 nouvelles routes :
S'inscrire
connexion
Se déconnecter
profil, qui prend l'identifiant de l'utilisateur en paramètre

Créez 2 nouveaux formulaires à partir du modèle User ( django_auth) :
Formulaire d'inscription :
Nom d'utilisateur
Prénom
Nom de famille
Mot de passe1
Mot de passe2

Formulaire de connexion :
Nom d'utilisateur
Mot de passe

Créez trois nouveaux modèles (ils doivent tous étendre le fichier base.html ) :
login.html : affiche le formulaire LoginForm
signup.html : affiche le formulaire SignupForm
profil.html
inclut le modèle navbar.html ( voir la partie I d'hier )
affiche le nom d'utilisateur, le prénom et le nom de famille de l'utilisateur

Créez une vue appelée inscription qui doit effectuer les actions suivantes :
Récupère les données du formulaire
Crée un nouvel utilisateur
Récupère l'utilisateur avec la authenticate()méthode. Pour plus d'informations sur la méthode d'authentification - Consultez la documentation de Django :
Si l'utilisateur existe déjà :
Connectez l'utilisateur. Utilisez la méthode de connexion .
Redirigez l'utilisateur vers la route /homepage qui appartient à l' application films (voir partie I)

Créez une vue de connexion qui agit comme la vue d'inscription.

Créez une vue de déconnexion qui déconnecte l'utilisateur et le redirige vers la route /homepage qui appartient à l'application films (voir Partie I) - utilisez la méthode de déconnexion - Consultez la documentation de Django )

Créer une vue de profil qui récupère et affiche l'utilisateur en fonction de son identifiant


PARTIE B : Films
Suite de la partie I d'hier

Dans la barre de navigation, les liens addFilm et addDirector doivent être affichés uniquement dans le cas où l'utilisateur courant est un superutilisateur.

Seul l'administrateur peut modifier les données d'un film et d'un réalisateur
http://127.0.0.1:8000/film_app/homepage/- Lorsque l'utilisateur n'est pas un administrateur
