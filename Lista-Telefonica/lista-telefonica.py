start = -1
lista_telefonica = ["João","61999282134", "Maria", "6199992331"]

while start < 0:
   
        def search():
            try:
                i = 0
                print("SEUS CONTATOS: \n")
                for i in range(len(lista_telefonica)):
                    if (i % 2 == 0):
                        print(lista_telefonica[i])   
                contact = (input("\nQual contato deseja acessar?\n"))
                if (contact.isalpha()):    
                    if (contact) in (lista_telefonica):
                        print("\nO número é " + lista_telefonica[lista_telefonica.index(contact) +  1] + "\n")
                else:
                    print("\nApenas Letras\n\n")            
            except ValueError:
                print("Digite apenas o nome do usuário")

        def add():
            try:
                print("SEUS CONTATOS: \n")
                for i in range(len(lista_telefonica)):
                    if (i % 2 == 0):
                        print(lista_telefonica[i]) 
                new_contact = str(input("\nInsira o nome do novo contato\n"))
                new_number = str(input("\nInsira o numero do novo contato\n"))
                if(new_contact.isalpha()):
                    lista_telefonica.append(new_contact)
                    lista_telefonica.append(new_number)
                else:
                    print("\nApenas Letras\n\n")  
            except ValueError:
                print("Digite apenas o nome do usuário")
        
        def remove():
            try:
                print("SEUS CONTATOS: \n")
                for i in range(len(lista_telefonica)):
                    if (i % 2 == 0):
                        print(lista_telefonica[i]) 
                rem_contact = str(input("\nQual contato deseja remover?\n"))
                if(rem_contact.isalpha()):
                    rem_contact2 = str(lista_telefonica[lista_telefonica.index(rem_contact) +  1])
                    lista_telefonica.remove(rem_contact)
                    lista_telefonica.remove(rem_contact2)
                else:
                    print("\nApenas Letras\n\n")      
            except ValueError:
                print("Digite apenas o nome do usuário")
        
        def main():
            try:
                x = int(input("\nO que deseja fazer?\n"
                + "1 - Adicionar contato"
                + "2 - Procurar número de contato"
                + "3 - Remover contato"))
                functions[x]()
            except ValueError:
                print("Digite apenas as opções disponíveis")
        functions = {1: add, 2: search, 3: remove}
        main()