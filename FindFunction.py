chaine = "Ceci est un exemple de chaîne de texte."
sous_chaine = "exemple"

position = chaine.find(sous_chaine)

if position != -1:
    print("La sous-chaîne", sous_chaine ," a été trouvée à la position", position)
else:
    print("La sous-chaîne", sous_chaine ,"n'a pas été trouvée dans la chaîne.")

