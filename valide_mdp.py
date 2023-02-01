import hashlib
 
mot_de_passe = input("Choisir un mot de passe\n")

#8 caractères

def validateur(password):
    if len(password) < 8:
        print("Le mot de passe doit être supérieur à 8 caractères")

#au moins 1 lettre maj
#au moins 1 lettre min
#au moins un chiffre
#au moins un caractère spé (!,@,#,$,%,^,&,*)
    
    minuscule = False
    majuscule = False
    chiffre = False
    special = False

    for i in range(len(password)):
        if password[i]>="a" and password [i]<="z":
            minuscule = True

        if password[i]>="A" and password [i]<="Z":
            majuscule = True

        if password[i]>="0" and password [i]<="9":
            chiffre = True

        if password[i] == "!" or password[i] == "@" or password[i] == "#" or password[i] == "$" or password[i] == "%" or password[i] == "^" or password[i] == "&" or password[i] == "*":
            special = True
    
    if minuscule == False:
        print("Le mot de passe doit comporter au moins une lettre minuscule")

    if majuscule == False:
        print("Le mot de passe doit comporter au moins une lettre majuscule")

    if chiffre == False:
        print("Le mot de passe doit comporter au moins un chiffre")

    if special == False:
        print("Le mot de passe doit comporter au moins un caractère spécial")

    if (minuscule, majuscule, chiffre, special, password) == False:
        print("Le mot de passe respecte toutes les normes")

#1) demande à l'utilisateur de choisir un mdp
#2) verifier si le mdp <==> exigences de secu
#3)si mdp valide, afficher un message de confirmation + quitter le programme
#4)si mdp n'est pas valide, afficher msg erreur + demander à l'utilisateur de choisir un nv mdp
        
#5) repeter étapes 2 et 4 jusqu'à que l'utilisateur choisisse un mdp valide
 
validateur(mot_de_passe)

#à l'aide de la librairie "Hashlib" + en utilisant l'algorithme de hachage SHA-256,
#écrire un progr. qui crypte le mdp que l'utilisateur à entré précedemment

str = hashlib.sha256(b'v')

str_hex = str.hexdigest()

print(str_hex)