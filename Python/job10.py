# Ecrire dans un fichier 
texte = input("texte : ")
with open("output.txt",'w') as f :
    f.write(texte)
    f.close()

# lire un fichier
with open("output.txt", 'r') as f :
    contenu = f.read()
    print(contenu)
    f.close()