import random
import tkinter as tk
from matplotlib import pyplot as plt
import pandas as pd
from tabulate import tabulate


class Aisthitiras:
    """Δημιουργια αντικειμενου αισθητηρας"""

    def __init__(self, tameio):
        self.tameio = tameio

    def anixneyei(self, ePassList):
        """Με την χρηση της random επιστρεφει ενα ePass απο την λιστα ePassList"""
        return random.choice(ePassList)


class Tameio:
    """Δημιουργια αντικειμενου ταμειο """

    def __init__(self):
        self.arDieleysewn = 0
        self.esodaDieleysewn = 0
        self.dieleyseis_ana_gyro = 0
        self.total_epivatika = 0
        self.total_dikikla = 0
        self.total_fortiga = 0

    def __str__(self):
        return ("\n--ΣΤΑΤΙΣΤΙΚΑ ΤΑΜΕΙΟΥ--\n"
                f"Aριθμός διελεύσεων: {self.arDieleysewn}\n"
                f"Έσοδα: {self.esodaDieleysewn:.2f} €\n")

    def addAxiaDieleysis(self, axia):
        """Αυξάνει τον αριθμο των συνολικων διελευσεων, τον διελευσεων ανα γύρο
           και προσθετη την αντιστοιχη χρεωση στα συνολικα εσοδα"""
        self.arDieleysewn += 1
        self.dieleyseis_ana_gyro += 1
        self.esodaDieleysewn += axia

    def reset(self):
        """Μηδενιζει ολες τις μεταβλητες για να μπορει
           να ξεκινησει το προγραμμα απο την αρχη"""
        self.arDieleysewn = 0
        self.esodaDieleysewn = 0
        self.dieleyseis_ana_gyro = 0
        self.total_epivatika = 0
        self.total_dikikla = 0
        self.total_fortiga = 0

    def count_oxhmata(self, kathgoria):
        """Ελεγχει τις κατηγοριες των οχηματων που
           περασαν και αυξανει τον αντιστοιχο μετρητη"""
        if kathgoria == "Επιβατικό":
            self.total_epivatika += 1
        elif kathgoria == "Δίκυκλο":
            self.total_dikikla += 1
        else:
            self.total_fortiga += 1


class ePass:
    """Δημιουργια αντικειμενου ePass και ανάλογα την
        κατηγορία δημιουργείτε το αντίστοιχο Όχημα"""

    def __init__(self, kodikos, arithmos, kategoria):
        self.kodikos = kodikos

        if kategoria == "Επιβατικό":
            self.car = Epivatiko(arithmos, kategoria, 1.50)
        elif kategoria == "Δίκυκλο":
            self.car = Dikyklo(arithmos, kategoria, 0.60)
        else:
            self.car = Fortigo(arithmos, kategoria, 3.20)

        self.ypoloipoLogariasmoy = random.randint(5, 10)

    def elegxei(self):
        """Ελέγχει το υπολοιπο λογαριασμου στο ePass
           αν αρκει για να περασει το οχημα"""
        if self.ypoloipoLogariasmoy >= self.car.xreosh:
            return True

    def xrewnei(self):
        """Μειώνει το υπολοιπο λογαριασμου
           αφαιρωντας τη χρεωση του οχήματος"""
        self.ypoloipoLogariasmoy -= self.car.xreosh
        self.car.arithmos_dielefsewn += 1


class Oxima:
    """Κατασκευαζουμε την κλαση Οχημα """

    def __init__(self, arithmos, kategoria, xreosh):
        self.arithmos = arithmos
        self.kategoria = kategoria
        self.xreosh = xreosh
        self.arithmos_dielefsewn = 0


class Epivatiko(Oxima):
    """Κατασκευαζουμε την υποκλάση Επιβατικο οπου ειναι παιδι της κλάσης Οχημα"""

    def __init__(self, arithmos, kategoria, xreosh):
        super().__init__(arithmos, kategoria, xreosh)


class Dikyklo(Oxima):
    """Κατασκευαζουμε την υποκλάση Δικυκλο οπου ειναι παιδι της κλάσης Οχημα"""

    def __init__(self, arithmos, kategoria, xreosh):
        super().__init__(arithmos, kategoria, xreosh)


class Fortigo(Oxima):
    """Κατασκευαζουμε την υποκλάση Φορτηγο οπου ειναι παιδι της κλάσης Οχημα"""

    def __init__(self, arithmos, kategoria, xreosh):
        super().__init__(arithmos, kategoria, xreosh)


# button_print
def print_as_table():
    """Μορφοποιημενη εκτυπωση σε πινακα. Μετρατρεπει την λιστα σε panda data frame
       και μετα με την βιβλιοθηκη tabulate κανουμε εκτυπωση"""
    headers = ["ePass", "Υπόλοιπο", "Αρ. Κυκλοφορίας", "Κατηγορία", "Αρ. Διελεύσεων"]
    for i in ePassList:
        new_ePassList.append([i.kodikos,
                              round(i.ypoloipoLogariasmoy, 2),
                              i.car.arithmos,
                              i.car.kategoria,
                              i.car.arithmos_dielefsewn])
    panda_table = pd.DataFrame(new_ePassList, columns=headers)
    text_output.configure(state="normal")
    text_output.insert("end", tabulate(panda_table, headers=headers, tablefmt='fancy_grid', showindex=True) + "\n")
    text_output.see("end")
    text_output.configure(state="disabled")
    new_ePassList.clear()


# button_chart
def car_chart():
    """Χρησιμοποιει την βιβλιοθηκη matplotlib και φτιαχνει ενα ραβδογραμμα
       με τον αριθμο των διελευσεων του καθε οχηματος"""
    a = []
    headers = ["Αρ. Κυκλοφορίας", "Αρ. Διελεύσεις"]
    for i in ePassList:
        a.append([i.car.arithmos, i.car.arithmos_dielefsewn])
    panda_table = pd.DataFrame(a, columns=headers)
    oxhmata = panda_table["Αρ. Κυκλοφορίας"]
    dielefseis = panda_table["Αρ. Διελεύσεις"]
    bar = plt.barh(oxhmata, dielefseis)
    # στο τελος της μπαρας εμφανιζεται και η "τιμη" που εχει
    plt.bar_label(bar, labels=dielefseis, label_type="edge")
    # ο οριζοντιος αξονας θα εχει τιμες απο το 0 εως τον μεγιστο αριθμο διελευσεων
    plt.xticks([int(i) for i in range(0, max(dielefseis) + 1)])
    plt.show()


def tameio_chart():
    katigories = ["Επιβατικά", "Δίκυκλα", "Φορτηγά"]
    count = [tameio.total_epivatika, tameio.total_dikikla, tameio.total_fortiga]
    # εσοδα αναλογα την κατηγορια του οχηματος
    money = [round(tameio.total_epivatika * 1.5, 2),
             round(tameio.total_dikikla * 0.6, 2),
             round(tameio.total_fortiga * 3.2, 2)]
    # Δημιουργούμε τη λίστα etiketes χρησιμοποιώντας μια list comprehension,
    # όπου για κάθε στοιχείο m στη λίστα money δημιουργούμε τη συμβολοσειρά f"Έσοδα: {m} €"
    etiketes = [f"Έσοδα: {m} €" for m in money]
    bar = plt.barh(katigories, count)
    plt.bar_label(bar, labels=etiketes, label_type="center")
    plt.xticks([int(i) for i in range(0, max(count) + 1)])
    plt.xlabel("Αριθμός διελεύσεων")
    plt.show()


# button_clear
def clear():
    """Διαγράφει ο,τι περιέχει το Text widget"""
    text_output.configure(state="normal")
    text_output.delete(1.0, tk.END)
    text_output.configure(state="disabled")


def reset_epass():

    """Αρχικοποιεί τις μεταβλητές που μετρούν σε 0"""
    for epass in ePassList:
        epass.car.arithmos_dielefsewn = 0
        epass.ypoloipoLogariasmoy = random.randint(5, 10)
    tameio.reset()


# button_start
def run():
    """καλει την μεθοδο loop οπου γινεται μια επαναληξη μεχρι να περασουν 20 οχηματα."""

    def loop():
        """Γινεται ελεγχος αν το οχημα εχει αρκετο υπολοιπο για την διελευση, αν εχει τπτε
           γινεται η χρεωση, αυξανεται ο μετρητης για την κατηγορια του οχηματος και εκτυπωνεται καταλληλο μηνυμα
           αν δεν εχει αρκετο υπολοιπο καλειται η μεθοδος  popup_window. Τελος υπαρχει ενα delay μεχρι να ξανα
           καλεστει η loop"""
        if tameio.dieleyseis_ana_gyro < 20:
            temp = aisthitiras.anixneyei(ePassList)
            if temp.elegxei():
                temp.xrewnei()
                tameio.addAxiaDieleysis(temp.car.xreosh)
                tameio.count_oxhmata(temp.car.kategoria)
                text_output.configure(state="normal")
                text_output.insert("end", f"-> Διέλευσε το {temp.car.arithmos}, αριθμός διελεύσεων: {temp.car.arithmos_dielefsewn}, υπόλοιπο λογαριασμού: {temp.ypoloipoLogariasmoy:.2f} €\n")
                text_output.see("end")
                text_output.configure(state="disabled")
                history_list.append(["ΝΑΙ", temp.kodikos,
                                     f"{temp.ypoloipoLogariasmoy:.2f}",
                                     temp.car.arithmos,
                                     temp.car.kategoria,
                                     temp.car.arithmos_dielefsewn])
            else:
                popup_window(temp)
        else:
            return
        # μικρη παυση μεχρι με τυχαιο ακεραιο που αντιστοιχει σε ms
        root.after(random.randint(500, 1500), loop)

    def popup_window(temp):
        """Δημιουργει καινουργιο παραθυρο για αν ρωτησει τον χρηστη αν θελει να
           προσθεσει χρηματα στο ePass"""

        # button_no
        def no():
            history_list.append(["ΟΧΙ", temp.kodikos,
                                 f"{temp.ypoloipoLogariasmoy:.2f}",
                                 temp.car.arithmos,
                                 temp.car.kategoria,
                                 temp.car.arithmos_dielefsewn])
            popup.destroy()
            text_output.configure(state="normal")
            text_output.insert("end", f"[!] To όχημα με αριθμό πινακίδας {temp.car.arithmos} δεν μπορεί να διελεύσει "
                                      f"γιατί το υπόλοιπο του λογαριασμού είναι {temp.ypoloipoLogariasmoy:.2f} €\n")
            text_output.see("end")
            text_output.configure(state="disabled")
            root.after(random.randint(500, 1500), loop)

        # button_yes
        def yes():
            """Προσθέτει 10 ευρω στο λογαριασμο, γινεται η χρεωση, ενημερωνει το ταμειο, τον μετρητη για την
               κατηγορια του οχηματος, την λιστα για το ιστορικο και εκτυπωνει καταλληλο μηνυμα στο text widget"""
            temp.ypoloipoLogariasmoy += 10
            temp.xrewnei()
            tameio.addAxiaDieleysis(temp.car.xreosh)
            tameio.count_oxhmata(temp.car.kategoria)
            history_list.append(["ΝΑΙ", temp.kodikos,
                                 f"{temp.ypoloipoLogariasmoy:.2f}",
                                 temp.car.arithmos,
                                 temp.car.kategoria,
                                 temp.car.arithmos_dielefsewn])
            popup.destroy()
            text_output.configure(state="normal")
            text_output.insert("end", "[✓] Φορτώθηκαν 10 € στο ePass " + str(temp.kodikos) + " του οχήματος "
                               + str(temp.car.arithmos) + "\n")
            text_output.insert("end", f"-> Διέλευσε το {temp.car.arithmos}, αριθμός διελεύσεων: {temp.car.arithmos_dielefsewn}, υπόλοιπο λογαριασμού: {temp.ypoloipoLogariasmoy:.2f} €\n")
            text_output.see("end")
            text_output.configure(state="disabled")
            root.after(random.randint(500, 1500), loop)

        popup = tk.Toplevel()
        popup.title("Φόρτωση υπολοίπου")
        popup.geometry("400x160+730+350")
        top = tk.Frame(popup, bg="#194361", width=300, height=100)
        top.pack(side="top", fill="both", expand=True)
        bottom = tk.Frame(popup, bg="#194361", width=100, height=60)
        bottom.pack(side="bottom", fill="both", expand=False)
        label = tk.Label(top, text="Δεν επαρκεί το υπόλοιπο\nγια να γίνει η διέλευση.\nΝα φορτωθούν 10 € στο ePass;",
                         font=("Courier", 14, "bold"),
                         bg="#194361", fg="#FFE8D1")
        label.pack()

        button_yes = tk.Button(bottom, text="NAI", font=("Courier", 14, "bold"), command=yes,
                               fg="#FFE8D1", bg="#032B43", width=15)
        button_yes.grid(pady=10, padx=10, row=0, column=0)
        button_no = tk.Button(bottom, text="OXI", font=("Courier", 14, "bold"), command=no,
                              fg="#FFE8D1", bg="#032B43", width=15)
        button_no.grid(pady=10, padx=10, row=0, column=1)
        popup.mainloop()

    tameio.dieleyseis_ana_gyro = 0
    loop()


# button_tameio
def stats_tameiou():
    """Εκτύπωση στατιστικων ταμειου"""
    text_output.configure(state="normal")
    text_output.insert("end", tameio.__str__() + "\n")
    text_output.see("end")
    text_output.configure(state="disabled")


# button_history
def show_history():
    """Εκτυπωση ιστορικου με τα οχηματα με την σειρα που περασε το καθε ενα"""
    headers = ["Διέλευση", "ePass", "Υπόλοιπο", "Αρ. Κυκλοφορίας", "Κατηγορία", "Αρ. Διελεύσεων"]
    panda_table1 = pd.DataFrame(history_list, columns=headers)
    text_output.configure(state="normal")
    text_output.insert("end", tabulate(panda_table1, headers=headers, tablefmt='fancy_grid', showindex=True + 1) + "\n")
    text_output.see("end")
    text_output.configure(state="disabled")


# button_reset
def epanafora():
    """ Καλει την reset_epass, αδειαζει την λιστα που κραταει το ιστορικο
        και εκτυπωνει καταλληλο μηνυμα"""
    reset_epass()
    history_list.clear()
    text_output.configure(state="normal")
    text_output.insert("end", "Έγινε επαναφορά της εφαρμογής και μπορείτε να αρχίσετε ξανά από την αρχή.\n")
    text_output.see("end")
    text_output.configure(state="disabled")


if __name__ == '__main__':
    # 20 ePass - οχήματα
    ePassList = [
        ePass(1715, "ΝΙΒ1000", "Επιβατικό"),
        ePass(2230, "ΑΡΚ2113", "Δίκυκλο"),
        ePass(3934, "ΙΝΟ3225", "Φορτηγό"),
        ePass(4141, "PPE4789", "Επιβατικό"),
        ePass(5371, "XAY5466", "Επιβατικό"),
        ePass(4230, "ΙΚΕ8624", "Δίκυκλο"),
        ePass(6642, "XIE6472", "Επιβατικό"),
        ePass(7499, "TΡΚ7228", "Φορτηγό"),
        ePass(8107, "KΞΙ8331", "Δίκυκλο"),
        ePass(9503, "ZΧK9112", "Επιβατικό"),
        ePass(9977, "ΙΟK9955", "Φορτηγό"),
        ePass(3715, "ΙΑΒ4163", "Επιβατικό"),
        ePass(2340, "ΙΚΡ2024", "Δίκυκλο"),
        ePass(9674, "ΥΖΕ4640", "Φορτηγό"),
        ePass(4531, "PΟΑ9768", "Επιβατικό"),
        ePass(3471, "ΤΑΑ6596", "Δίκυκλο"),
        ePass(3974, "ΘΥΑ7391", "Επιβατικό"),
        ePass(7410, "ΖΠΑ1960", "Δίκυκλο"),
        ePass(9791, "ΑΣΔ7364", "Φορτηγό"),
        ePass(4931, "ΜΝΟ2675", "Φορτηγό"),
    ]
    tameio = Tameio()
    aisthitiras = Aisthitiras(tameio)
    new_ePassList = []
    history_list = []

    root = tk.Tk()
    root.title("ΤΕΛΙΚΟ PROJECT - «ΔΙΑΧΕΙΡΙΣΗ ΗΛΕΚΤΡΟΝΙΚΩΝ ΔΙΟΔΙΩΝ»")
    # ρυθμιζουμε το μεγεθος του παραθυρου και το που θα τοποθετηθει
    root.geometry("1100x700+350+100")

    # δεξι frame που θα μπουν τα κουμπια
    left = tk.Frame(root, bg="#194361", width=300, height=800)
    left.pack(side="left", fill="both", expand=False)

    # αριστερο frame που θα μπει το text widget
    right = tk.Frame(root, bg="#194361", width=800, height=800)
    right.pack(side="left", fill="both", expand=True)

    onomata = tk.Label(left, text="Στειργιανός Γιώργος\nΤσιλιγκίρης Κωσταντίνος\nΧαριλάου Σάββας\nΧρόνης Σπύρος",
                       font=("Courier", 13, "bold"), bg="#194361", fg="#FFE8D1", anchor="w", justify="left")
    onomata.place(x=10, y=390)

    info = tk.Label(left, text="Έτος 2023-2024\nΠΛΗΠΡΟ - ΗΛΕ50\n«Διόδια»", font=("Courier", 13, "bold"),
                    bg="#194361", fg="#FFE8D1", anchor="w", justify="left")
    info.place(x=10, y=480)

    # κουμπι για την εναρξη της επαναληψης
    button_start = tk.Button(left, text="ΕΝΑΡΞΗ", font=("Courier", 14, "bold"),
                             command=run, fg="#FFE8D1", bg="#032B43", width=20)
    button_start.grid(pady=5, padx=10, row=0, column=0)

    # κουμπι για την εκτυπωση στατιστικων των οχηματων
    button_print = tk.Button(left, text="ΟΧΗΜΑΤΑ", font=("Courier", 14, "bold"),
                             command=print_as_table, fg="#FFE8D1", bg="#032B43", width=20)
    button_print.grid(pady=5, padx=10, row=1, column=0)

    # κουμπι για την εκτυπωση στατιστικων του ταμειου
    button_tameio = tk.Button(left, text="ΤΑΜΕΙΟ", font=("Courier", 14, "bold"),
                              command=stats_tameiou, fg="#FFE8D1", bg="#032B43", width=20)
    button_tameio.grid(pady=5, padx=10, row=2, column=0)

    # κουμπι για την εκτυπωση του ιστορικου
    button_history = tk.Button(left, text="ΙΣΤΟΡΙΚΟ ΔΙΕΛΕΥΣΕΩΝ", font=("Courier", 14, "bold"),
                               command=show_history, fg="#FFE8D1", bg="#032B43", width=20)
    button_history.grid(pady=5, padx=10, row=3, column=0)

    # κουμπι για την εκαθαριση του Text Widget
    button_clear = tk.Button(left, text="ΕΚΚΑΘΑΡΙΣΗ ΟΘΟΝΗΣ", font=("Courier", 14, "bold"),
                             command=clear, fg="#FFE8D1", bg="#032B43", width=20)
    button_clear.grid(pady=5, padx=10, row=4, column=0)

    # κουμπι για ραβδογραμμα των οχηματων
    button_car_chart = tk.Button(left, text="ΓΡΑΦΗΜΑ ΟΧΗΜΑΤΩΝ", font=("Courier", 14, "bold"),
                                 command=car_chart, fg="#FFE8D1", bg="#032B43", width=20)
    button_car_chart.grid(pady=5, padx=10, row=5, column=0)

    # κουμπι για ραβδογραμμα του ταμειου
    button_tameio_chart = tk.Button(left, text="ΓΡΑΦΗΜΑ ΤΑΜΕΙΟΥ", font=("Courier", 14, "bold"),
                                    command=tameio_chart, fg="#FFE8D1", bg="#032B43", width=20)
    button_tameio_chart.grid(pady=5, padx=10, row=6, column=0)

    # κουμπι για την επαναφορα των μεταβλητων που μετρανε πληθος σε 0
    button_epanafora = tk.Button(left, text="ΕΠΑΝΑΦΟΡΑ", font=("Courier", 14, "bold"),
                                 command=epanafora, fg="#FFE8D1", bg="#032B43", width=20)
    button_epanafora.grid(pady=5, padx=10, row=7, column=0)

    # δημιουργια Text Widget για να γινονται οι εκτυπωσεις
    text_output = tk.Text(right, bg="#fefae0", wrap="word", font=("Courier", 10), fg="#000000")
    text_output.pack(side="left", pady=5, padx=5, fill="both", expand=True)

    # μπαρα κυλισης για το Text Widget
    scrollbar = tk.Scrollbar(right, command=text_output.yview)
    scrollbar.pack(side="right", fill="y")
    text_output.configure(yscrollcommand=scrollbar.set)

    root.mainloop()