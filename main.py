import MyLinkedList
import Element
import smtplib
from email.mime.text import MIMEText


def save(studentsList, filepath):
    with open(filepath, "w") as file_object:
        tmp = studentsList.get(0)
        while tmp is not None:
            str = ""
            str = tmp.data["email"] + "," + tmp.data["name"] + "," + tmp.data["lastName"] + "," + tmp.data[
                "project"] + "," + \
                  tmp.data["list1"] + "," + tmp.data["list2"] + "," + tmp.data["list3"] + "," + \
                  tmp.data["homework1"] + "," + tmp.data["homework2"] + "," + tmp.data["homework3"] + "," \
                  + tmp.data["homework4"] + "," + tmp.data["homework5"] + "," + tmp.data["homework6"] + "," + \
                  tmp.data["homework7"] + "," + tmp.data["homework8"] + "," + tmp.data["homework9"] + "," + tmp.data[
                      "homework10"] + "," + \
                  tmp.data["grade"] + "," + tmp.data["gradeStatus"]
            file_object.write(str + "\n")
            tmp = tmp.nextE


def isGradable(studentData):
    if studentData["project"] == "-1" or studentData["list1"] == "-1" or studentData["list2"] == "-1" or studentData[
        "list3"] == "-1":
        return False
    return True


def calculateGrade(studentData):
    procentOceny = int(studentData["project"])
    procentZadan = min(0, int(studentData["homework1"]))
    procentZadan = procentZadan + min(0, int(studentData["homework2"]))
    procentZadan = procentZadan + min(0, int(studentData["homework3"]))
    procentZadan = procentZadan + min(0, int(studentData["homework4"]))
    procentZadan = procentZadan + min(0, int(studentData["homework5"]))
    procentZadan = procentZadan + min(0, int(studentData["homework6"]))
    procentZadan = procentZadan + min(0, int(studentData["homework7"]))
    procentZadan = procentZadan + min(0, int(studentData["homework8"]))
    procentZadan = procentZadan + min(0, int(studentData["homework9"]))
    procentZadan = procentZadan + min(0, int(studentData["homework10"]))
    if procentZadan >= 800:
        procentOceny = procentOceny + 60
    elif procentZadan >= 70:
        procentOceny = procentOceny + max(int(studentData["list1"]), int(studentData["list2"]),
                                          int(studentData["list3"])) + 40
    elif procentZadan >= 60:
        procentOceny = procentOceny + int(studentData["list1"]) + int(studentData["list2"]) + int(
            studentData["list3"]) - min(int(studentData["list1"]), int(studentData["list2"]),
                                        int(studentData["list3"])) + 20
    else:
        procentOceny = procentOceny + int(studentData["list1"]) + int(studentData["list2"]) + int(studentData["list3"])

    ocena = 2
    if procentOceny > 90:
        ocena = 5
    elif procentOceny > 80:
        ocena = 4.5
    elif procentOceny > 70:
        ocena = 4
    elif procentOceny > 60:
        ocena = 3.5
    elif procentOceny > 50:
        ocena = 3
    return ocena


def grade(studentsList):
    for i in range(studentsList.size):
        if isGradable(studentsList.get(i).data):
            if studentsList.get(i).data["gradeStatus"] == "None":
                studentsList.get(i).data["grade"] = str(calculateGrade(studentsList.get(i).data))
                studentsList.get(i).data["gradeStatus"] = "GRADED"

        else:
            if studentsList.get(i).data["gradeStatus"] == "None":
                studentsList.get(i).data["gradeStatus"] = "HOME_9"

    print("Oceny zostaly wystawione")
    input("<<NACISNIJ ENTER ABY KONTYNUOWAC>>")


def addStudent(studentsList):
    print("\n\nPodaj dane studenta w formacie: 'email,imie,nazwisko,projekt,lista1,lista2,lista3,pracaDomowa1,"
          "pracaDomowa2,...,pracaDomowa10,ocena,statusOceny'")
    print("W przypadku niewystawionej oceny uzyj '-1'")
    print("Jesli uczen nie dostal oceny semestralnej uzyj 'None'")
    str = input()
    obecny = False
    strings = str.split(",")
    email = strings[0]
    for i in range(studentsList.size):
        if studentsList.get(i).data["email"] == email:
            obecny = True
    if obecny:
        print("W systemie jest juz student o podanym emailu!")
        input("<<NACISNIJ ENTER ABY KONTYNUOWAC>>")
    else:
        student = {
            "email": strings[0],
            "name": strings[1],
            "lastName": strings[2],
            "project": strings[3],
            "list1": strings[4],
            "list2": strings[5],
            "list3": strings[6],
            "homework1": strings[7],
            "homework2": strings[8],
            "homework3": strings[9],
            "homework4": strings[10],
            "homework5": strings[11],
            "homework6": strings[12],
            "homework7": strings[13],
            "homework8": strings[14],
            "homework9": strings[15],
            "homework10": strings[16],
            "grade": strings[17],
            "gradeStatus": strings[18]
        }
        studentsList.append(Element.Element(student), sortFunc)

        print("Student dodany")
        input("<<NACISNIJ ENTER ABY KONTYNUOWAC>>")


def deleteStudent(studentsList):
    str = input("\n\nPodaj email studenta ktorego chcesz usunac:\n")
    for i in range(studentsList.size):
        if studentsList.get(i).data["email"] == str:
            obecny = True
            studentsList.delete(i)
            print("Student usuniety")
            input("<<NACISNIJ ENTER ABY KONTYNUOWAC>>")
            return 0

    print("Nie ma studenta o podanym emailu")
    input("<<NACISNIJ ENTER ABY KONTYNUOWAC>>")


def sendMail(studentsList):
    states = input("Podaj statusy dla jakich wysylane beda maile:")

    sender = ""
    password = ""
    for i in range(studentsList.size):
        student = studentsList.get(i).data
        if student["gradeStatus"] in states.split(","):
            print("Student:")
            print(student)
            newStatus = input("Jaki nowy status nadac temu studentowi: ")
            student["gradeStatus"] = newStatus
            recipients = [student["email"]]
            msg = MIMEText("Gratulacje, twoja ocena to " + student["grade"])
            msg['Subject'] = "Oceny"
            msg['From'] = ""
            msg['To'] = student["email"]
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())
            smtp_server.quit()
    print("Maile zostaly wyslane")
    input("<<NACISNIJ ENTER ABY KONTYNUOWAC>>")

def sortFunc(a, b):  # funkcja sortujaca
    if a["gradeStatus"] == "None" and b["gradeStatus"] != "None":
        return True
    if b["gradeStatus"] == "None" and a["gradeStatus"] != "None":
        return False
    return a["name"].lower() <= b["name"].lower()


lista = MyLinkedList.MyLinkedList()
filepath = "ocenystudenci"

with open(filepath) as file_object:  # pobieranie danych z pliku
    for line in file_object:
        str = line.rstrip()
        # print(str)
        strings = str.split(",")
        student = {
            "email": strings[0],
            "name": strings[1],
            "lastName": strings[2],
            "project": strings[3],
            "list1": strings[4],
            "list2": strings[5],
            "list3": strings[6],
            "homework1": strings[7],
            "homework2": strings[8],
            "homework3": strings[9],
            "homework4": strings[10],
            "homework5": strings[11],
            "homework6": strings[12],
            "homework7": strings[13],
            "homework8": strings[14],
            "homework9": strings[15],
            "homework10": strings[16],
            "grade": strings[17],
            "gradeStatus": strings[18]
        }
        lista.append(Element.Element(student), sortFunc)

while True:
    print("Co chcesz zrobic?"
          "\n1. Automatycznie wystawic oceny"
          "\n2. Dodac nowego studenta"
          "\n3. Usunac studenta"
          "\n4. Wyslac studentom maile z ocenami")
    answer = input("Podaj odpowiedz: ")
    if answer == "1":
        grade(lista)
        save(lista, filepath)
    elif answer == "2":
        addStudent(lista)
        save(lista, filepath)
    elif answer == "3":
        deleteStudent(lista)
        save(lista, filepath)
    elif answer == "4":
        # sendMail(students)
        save(lista, filepath)

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
