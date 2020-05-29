'''
f=open("miarchivo.txt","w+")
f.write("wacha un texto XD")
f.close();
'''

'''
f=open("miarchivo.txt","a+") #el a es un permiso para que al final de la linea escrita puedas agregar mas texto
f.write(" otro mas")
f.close(); 
'''

f=open("miarchivo.txt","r") 
contenido = f.read()
print(contenido)