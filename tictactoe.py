#function to check if the last player did win the game(duh)
def winner(tableau, player):
	#verifier les ligne
	for i in range(3):
		if tableau[i][0] == tableau[i][1] == tableau[i][2] != " ":
			return True
	#verifier les colonnes
	for i in range(3):
		counter = 1
		line = 1
		while line < 3:
			if tableau[i][line] == tableau[i][0] != " ":
				counter += 1
			line += 1
		if counter == 3:
			return True

	#Verifier les diagonales
	if tableau[0][0] == tableau[1][1] == tableau[2][2] != " " or \
	 tableau[2][0] == tableau[1][1] == tableau[0][2] != " ":
		return True

	return False

#affichage du tableau
def print_tab(tableau):
	for i in range(3):
		line = ""
		for j in range(3):
			line += tableau[i][j]
		print(line)


#boucle du jeu
tableau = [{0:" ",1:" ",2:" "},
			{0:" ",1:" ",2:" "},
			{0:" ",1:" ",2:" "}]
player = "X"


for i in range(9):
	print_tab(tableau)
	print(f"c'est le role de {player}")
	while True:
		case = (int(input("c'est quoi la ligne(0,1,2) :")),int(input("c'est quoi la colonne(0,1,2) :")))
		if (case[0]  != 0 and case[0]  != 1 and case[0]  != 2 ) or (case[1] != 0 and case[1]  != 1 and case[1]  != 2):
			print("invalid range")
		else:
			if tableau[case[0]][case[1]] == " ":
				tableau[case[0]][case[1]] = player
				break
			else:
				print("Cet emplacement est déjà occupé. Réessayez.")

	if winner(tableau,player):
		print(f"{player} a gagné")
		break

	player = "O" if player == "X" else "X"

if not(winner(tableau,player)):
	print("Match nul")
