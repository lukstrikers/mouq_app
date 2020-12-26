import json
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QCompleter
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QFont

def clean_str(json_output_list):
	print('\n')
	output = ''
	for i in json_output_list:
		for key in i.keys():
			output += '{}'.format(key) + '_'*(22 - len(key)) + '_____{} '.format(i[key]) + '\n'
		output += 2*'\n'
	return output

	

def get_info(input_nom, person = True):
	with open('test_database.json') as f:
		data = json.load(f)
		count = -1
		final_count = 0
		found = False
		to_print = []
		if person:
			for name in data['people']:
				count += 1
				nom = name['nom'].lower()
				prenom = name['prenom'].lower()
				if nom == input_nom.lower():
					to_print.append(name)
					found = True
					final_count = count
				elif prenom == input_nom.lower():
					to_print.append(name)
					found = True
					final_count = count
			if found:
				return to_print, final_count
			else:
				return 'Aucune personne trouvée', final_count
		else:
			for name in data['depliant']:
				presta = name['Prestation'].lower()
				if presta == input_nom.lower():
					to_print.append(name)
					found = True
			if found:
				return to_print, final_count
			else:
				return 'Aucune prestation trouvée', final_count
		f.close()

def add_person():
	with open('test_database.json') as f:
		data = json.load(f)
		f.close()
		add = {"nom": input('Nom : '),
				"prenom": input('Prenom : '),
				"date de naissance": input('date de naissance : '),
				"Num Tel": input('Num Tel : '),
				"Adresse": input('Adresse : '),
				"Mail": input('Mail : '),
				"Identifiant Bien Etre": input('Identifiant Bien Etre : '),
				"type presta": input('type presta : '),
				"divers infos": input('divers infos : ')}
		data['people'].append(add)

	print('La personne a bien ete ajoutee...')
	with open('test_database.json', 'w') as outfile:
		json.dump(data, outfile, indent = 2)
		outfile.close()

def delete_person(input_nom):
	with open('test_database.json') as f:
		data = json.load(f)
		list_people = []
		for name in data['people']:
			prenom = name['prenom'].lower()
			if prenom == input_nom.lower():
				pass
			else:
				list_people.append(name)
		if len(data['people']) != len(list_people):
			data['people'] = list_people
			print('La personne a bien ete supprimee...')
		else:
			print("Cette personne n'existe pas")
		with open('test_database.json', 'w') as outfile:
			json.dump(data, outfile, indent = 2)

	


def modifier_var():
	with open('test_database.json') as f:
		data = json.load(f)
		f.close()
		input_name = input('Nom : ')
		if get_info(input_name, True)[0] != 'Aucune personne trouvée':
			clean_str(get_info(input_name, True)[0])
			input_modif = input('\n' + 'Que voulez vous changez ? : ')
			for var in range(len(data['people'])):
				if var == get_info(input_name, True)[1]:
					for i in data['people'][var]:
						if i == input_modif:
							data['people'][var][i] = input(' Modification : ')
							break
		else:
			return print(' Aucune personne trouvée, Retour Menu' + '\n')
			f.close()
	with open('test_database.json', 'w') as outfile:
		json.dump(data, outfile, indent = 2)
		outfile.close()

def voir_depliant():
	with open('test_database.json') as f:
		data = json.load(f)
		to_string = []
		print(" 1 -> Rechercher une prestation")
		print(" 2 -> Voir tous le depliant")
		input_user = input("-> ")
		if input_user == '2':
			for i in data['depliant']:
				to_string.append(i)
			return clean_str(to_string)
		else:
			launch_class(False)
		

def add_presta():
	with open('test_database.json') as f:
		data = json.load(f)
		f.close()
		add = {"Prestation": input('Nom de la prestation : '),
				"prix": input('Prix de la prestation : ')}
		data['depliant'].append(add)

	print('La prestation a bien ete ajoutee...')
	with open('test_database.json', 'w') as outfile:
		json.dump(data, outfile, indent = 2)
		outfile.close()



def Get_Choice(number): 
	return {
	'1' : lambda: launch_class(True),
	'2' : lambda: add_person(),
	'3' : lambda : delete_person(input('Nom : ')),
	'4' : lambda : modifier_var(),
	'5' : lambda : voir_depliant(),
	'6' : lambda : add_presta(),
	'7' : lambda : 'fin'
	}.get(number, lambda: "erreur")()

def main():
	print(" 1 -> Rechercher")
	print(" 2 -> Ajouter Quelqu'un")
	print(" 3 -> Supprimer Quelqu'un")
	print(" 4 -> Modifier coordonnees")
	print(" 5 -> Voir Depliant")
	print(" 6 -> Ajouter ou modifier une prestation")
	print(" 7 -> Quitter")
	Choix = Get_Choice(input('\n' + 'Que voulez vous faire : '))
	while Choix != 'fin':
		print('\n')
		print(" 1 -> Rechercher")
		print(" 2 -> Ajouter Quelqu'un")
		print(" 3 -> Supprimer Quelqu'un")
		print(" 4 -> Modifier coordonnees")
		print(" 5 -> Voir Depliant")
		print(" 6 -> Ajouter ou modifier une prestation")
		print(" 7 -> Quitter")
		Choix = Get_Choice(input('\n' + 'Que voulez vous faire : '))
