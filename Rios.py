rios={'Nilo':'Egito',"Amazonas":"Brasil","Rio Danúbio":"Alemanha"}
for n in rios:
        print(n)
        if "Nilo" in n:
            print("O rio Nilo é lindo")
        if "Amazonas"in n:
            print("O rio Amazonas é bonito")
        if "Rio Danúbio" in n:
            print("Rio Danúbio é legal")

print("=-=-=-=-=-=-=Rios-=-=-=-=--=-=--=-=-=")
for r in rios.keys():
    print(r)
print("=-=-=-=-=-=-=Países=-==-=-=-==-==-==-=-==-")
for p in rios.values():
    print(p)