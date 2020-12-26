import tkinter
import test as t

def main_form(main_wind):
  def save_info():

    t.add_person(firstname.get(), lastname.get(), birth.get(), tel.get(), adresse.get(), mail.get(), id_bien.get(), presta.get(), divers.get())

    firstname_entry.delete(0, tkinter.END)
    lastname_entry.delete(0, tkinter.END)
    birth_entry.delete(0, tkinter.END)
    tel_entry.delete(0, tkinter.END)
    adresse_entry.delete(0, tkinter.END)
    mail_entry.delete(0, tkinter.END)
    id_bien_entry.delete(0, tkinter.END)
    presta_entry.delete(0, tkinter.END)
    divers_entry.delete(0, tkinter.END)

    screen.destroy()


    
  screen = tkinter.Toplevel(main_wind)
  screen.geometry("500x900")
  screen.title("Ajouter un(e) client(e)")
  heading = tkinter.Label(screen, text = "Ajouter un(e) client(e)", bg = "#645e6b", fg = "white", width = "500", height = "3")
  heading.pack()
   
  firstname_text = tkinter.Label(screen, text = "Nom * ",)
  lastname_text = tkinter.Label(screen, text = "Prénom * ",)
  birth_text = tkinter.Label(screen, text = "date de naissance * ",)
  tel_text = tkinter.Label(screen, text = "Num Tel * ",)
  adresse_text = tkinter.Label(screen, text = "Adresse * ",)
  mail_text = tkinter.Label(screen, text = "Mail * ",)
  id_bien_etre_text = tkinter.Label(screen, text = "Identifiant Bien Etre * ",)
  type_presta_text = tkinter.Label(screen, text = "type presta * ",)
  divers_text = tkinter.Label(screen, text = "divers * ",)
  firstname_text.place(x = 15, y = 50)
  lastname_text.place(x = 15, y = 120)
  birth_text.place(x = 15, y = 200)
  tel_text.place(x = 15, y = 280)
  adresse_text.place(x = 15, y = 360)
  mail_text.place(x = 15, y = 440)
  id_bien_etre_text.place(x = 15, y = 520)
  type_presta_text.place(x = 15, y = 600)
  divers_text.place(x = 15, y = 680)


  firstname = tkinter.StringVar()
  lastname = tkinter.StringVar()
  birth = tkinter.StringVar()
  tel = tkinter.StringVar()
  adresse = tkinter.StringVar()
  mail = tkinter.StringVar()
  id_bien = tkinter.StringVar()
  presta = tkinter.StringVar()
  divers = tkinter.StringVar()

  firstname_entry = tkinter.Entry(screen, textvariable = firstname, width = "30")
  lastname_entry = tkinter.Entry(screen, textvariable = lastname, width = "30")
  birth_entry = tkinter.Entry(screen, textvariable = birth, width = "30")
  tel_entry = tkinter.Entry(screen, textvariable = tel, width = "30")
  adresse_entry = tkinter.Entry(screen, textvariable = adresse, width = "30")
  mail_entry = tkinter.Entry(screen, textvariable = mail, width = "30")
  id_bien_entry = tkinter.Entry(screen, textvariable = id_bien, width = "30")
  presta_entry = tkinter.Entry(screen, textvariable = presta, width = "30")
  divers_entry = tkinter.Entry(screen, textvariable = divers, width = "30")

  firstname_entry.place(x = 15, y = 70)
  lastname_entry.place(x = 15, y = 150)
  birth_entry.place(x = 15, y = 240)
  tel_entry.place(x = 15, y = 310)
  adresse_entry.place(x = 15, y = 390)
  mail_entry.place(x = 15, y = 470)
  id_bien_entry.place(x = 15, y = 550)
  presta_entry.place(x = 15, y = 630)
  divers_entry.place(x = 15, y = 710)

  register = tkinter.Button(screen,text = "Register", width = "30", height = "2", command = save_info, bg = "grey")
  register.place(x = 15, y = 850)