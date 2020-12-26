import tkinter
import test as m
import sys
import formulaire as form
import class_searchbar as sb
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

def search_client():
	resltt = clean_str(m.get_info(sb.launch_search_bar(True), True)[0])
	print(resltt)
	resultat_window = tkinter.Toplevel(app)
	resultat_window.title("Résultat de la recherche")
	lb = tkinter.Label(resultat_window, text = resltt, width = 70, height = 30)
	lb.pack()

def search_presta():
	resltt = clean_str(m.get_info(sb.launch_search_bar(False), False)[0])
	print(resltt)
	resultat_window = tkinter.Toplevel(app, bg = '#474030')
	resultat_window.config(width = 1000, height = 800)
	resultat_window.title("Résultat de la recherche")


	prestaname_text_1 = tkinter.Label(resultat_window, text = clean_str(resltt)[0][0], bg = '#474030', font = ("Courier", 20), fg = 'white')
	prestaname_text_2 = tkinter.Label(resultat_window, text = clean_str(resltt)[0][1], bg = '#474030', font = ("Courier", 20), fg = 'white')

	prixpresta_text_1 = tkinter.Label(resultat_window, text = clean_str(resltt)[1][0], bg = '#474030', font = ("Courier", 20), fg = 'white')
	prixpresta_text_2 = tkinter.Label(resultat_window, text = clean_str(resltt)[1][1], bg = '#474030', font = ("Courier", 20), fg = 'white')

	#lb = tkinter.Label(resultat_window, text = resltt, width = 70, height = 30)
	prestaname_text_1.place(relheight=0.2, relwidth = 0.2)
	prestaname_text_2.place(relheight=0.2, relwidth = 0.8)

	#prixpresta_text_1.pack(side=tkinter.LEFT, padx=20, pady=20)
	#prixpresta_text_2.pack(side=tkinter.RIGHT, padx=20, pady=20)



#fenêtre et paramétrages
app = tkinter.Tk()
app.geometry("800x600")
app.title("MOUQUET'S ETHIQUE")

def add_client(app = app):
	form.main_form(app)

#widgets
mainmenu = tkinter.Menu(app)

client_menu = tkinter.Menu(mainmenu, tearoff=0)
client_menu.add_command(label = 'Rechercher un(e) client(e)', command = search_client)
client_menu.add_command(label = 'Ajouter un(e) client(e)', command = add_client)
client_menu.add_command(label = 'Effacer un(e) client(e)')
client_menu.add_command(label = "Modifier les coordonnees d'un(e) client(e)")


mon_menu = tkinter.Menu(mainmenu, tearoff=0)
mon_menu.add_command(label = "Rechercher une prestation", command = search_presta)
mon_menu.add_command(label = "Voir toutes les prestation")
mon_menu.add_command(label = "Ajouter une prestation")

menu_parametre = tkinter.Menu(mainmenu, tearoff=0)
menu_parametre.add_command(label = "Quitter", command = app.quit)

mainmenu.add_cascade(label='Client(e)', menu = client_menu)
mainmenu.add_cascade(label='Mon menu', menu = mon_menu)
mainmenu.add_cascade(label='Paramètres', menu = menu_parametre)

#main loop
app.config(menu = mainmenu, bg = '#645e6b')
app.mainloop()