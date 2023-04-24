import MyLinkedList
import Element

lista = MyLinkedList.MyLinkedList()
e1 = Element.Element("1")
e2 = Element.Element("2")
e3 = Element.Element("3")
e4 = Element.Element("4")
e5 = Element.Element("5")

lista.append(e1)
lista.append(e2)
lista.append(e3)
lista.append(e4)
lista.append(e5)

print(lista.__str__())

print(lista.get(1).data)

lista.delete(1)
print(lista.__str__())
