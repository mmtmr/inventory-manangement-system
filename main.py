#LAI MEI SIM
#TP061562

def sectionDetails():
    section=[]
    numSection=int(input('Enter amount of car assembly sections in this division you want to add, type "0" to skip:'))
    if numSection!=0:
        for j in range(numSection):
            sec=[]
            s=[]
            nameSection=input('Enter name of assembly section: ')
            s.append(nameSection)
            codeSection=input('Enter code of assembing section: ')
            s.append(codeSection)
            sec.extend(s)
            section.append(sec)
            #print(section)
    return section

def divisionDetails(): 
    numDivision=int(input('Enter amount of car models/assembly divisions/warehouses you want to add, type the specific name and code of the division to modify the section,type "0" to skip: '))
    system=[]
    if numDivision!=0:
        for i in range(numDivision):
            division=[]
            div=[]
            nameDivision=input('Enter name of the car model for assembly division: ')
            div.append(nameDivision)
            codeWarehouse=input('Enter warehouse code for this assembly division: ')
            div.append(codeWarehouse)
            section=sectionDetails()
            division.extend(div)
            for sec in section:
                sys=[]
                sys.extend(division)
                sys.extend(sec)
                system.append(sys)
        #print(system)
    return system

def supplierDetails(name):
    fileHandler=open('supplier_details.txt','a')
    fileHandler.close()
    fileHandler=open('supplier_details.txt','r+')
    file=fileHandler.readlines()
    for line in file:
        line=line.rstrip()
        newLine=line.split("\t")
        if(name in line):
            return
    sup=[]
    sup.append(name)
    supPhone=input("Enter phone number:")
    supMail=input("Enter email:")
    supPIC=input("Enter person in charge:")
    sup.append(supPhone)
    sup.append(supMail)
    sup.append(supPIC)
    for s in sup:
        fileHandler.write(s)
        fileHandler.write('\t')
    fileHandler.write('\n')
    fileHandler.close()
    

def partsDetails():
    parts=[]
    idParts=''
    while(1):
        pts=[]
        p=[]
        idParts=input('Enter parts id, format is X000, type "0" to end: ')
        if idParts=='0':break
        p.append(idParts)
        nameParts=input('Enter parts name: ')
        p.append(nameParts)
        supplierParts=input('Enter supplier: ')
        p.append(supplierParts)
        supplierDetails(supplierParts)
        sectionParts=input('Enter assembly section code use in: ')
        p.append(sectionParts)
        #p.append('0')
        pts.extend(p)
        parts.append(pts)      
    return parts

def createSystemDetails():
    fileHandler=open('system_details.txt','a')         
    system=divisionDetails()
    for division in system:
        for div in division:
            for d in div:
                fileHandler.write(d)
            fileHandler.write('\t')
        fileHandler.write('\n')
    fileHandler.close()
    
    fileHandler=open('parts_details.txt','a')         
    parts=partsDetails()
    for part in parts:
        for pts in part:
            for p in pts:
                fileHandler.write(p)
            fileHandler.write('\t')
        fileHandler.write('\n')
    fileHandler.close()

def printPartsDetails():
    fileHandler=open('parts_details.txt','r')
    print("Below are the parts recorded in the system")
    print("Id\tName\tSupplier\tAssembly Section Code")
    for line in fileHandler:
        print(line)
    fileHandler.close()

def printSystemDetails():
    fileHandler=open('system_details.txt','r')
    print("Below are the assembly sections in each warehouse recorded in the system")
    print("Warehouse\tCode\tSection\Code")
    for line in fileHandler:
        print(line)
    fileHandler.close()

def addPartsInventory(parts,warehouse):
    partsInventory=[]
    ptsInv=[]
    pi=[]
    pi.append(parts)
    pi.append(warehouse)
    quantity=input("Enter the initial quantity: ")
    pi.append(quantity)  
    fileHandler=open('parts_inventory.txt','a')
    fileHandler.write('\n')
    for p in pi:
        fileHandler.write(p)
        fileHandler.write('\t')  
    fileHandler.close()
    ptsInv.extend(pi)
    partsInventory.append(ptsInv)
    

def addPartstoWarehouse():
    partsFH=open('parts_details.txt','r')
    parts=partsFH.readlines()
    systemFH=open('system_details.txt','r')
    system=systemFH.read().splitlines()
    inventoryFH=open('parts_inventory.txt','r')
    inventory=inventoryFH.read().splitlines()
        
    addParts=input("Enter the part code selected: ")
    addWarehouse=input("Enter the warehouse code selected: ")
    #addSection=parts[-1]
        
    tf=0

    for line in inventory:
        line=line.rstrip()
        newLine=line.split("\t")
        if(addParts in newLine and addWarehouse in newLine):
            partsFH.close()
            systemFH.close()
            inventoryFH.close()
            print("Existing part type in warehouse")
            return
        
    for line in parts:
        line=line.rstrip()
        newLine=line.split("\t")
        if(addParts in newLine):
            searchIndex=newLine[-1]
            tf=1
    if tf==0:
        print("Invalid part code")
 
    elif tf==1:
        for line in system:
            line=line.rstrip()
            newLine=line.split("\t")
            #print(newLine)
            if addWarehouse in newLine and searchIndex in newLine:
                addPartsInventory(addParts,addWarehouse)
                tf=2
                break
        if tf==1:
            print("Invalid warehouse code or warehouse does not have the specific section")
    partsFH.close()
    systemFH.close()
            
def restockFromSupplier():
    inventoryFH=open('parts_inventory.txt','r')
    inventory=inventoryFH.read().splitlines()
    inventoryFH.close()
    inventoryFH=open('parts_inventory.txt','w')

    addParts=input("Enter the part code selected: ")
    addWarehouse=input("Enter the warehouse code selected: ")
    addQuantity=int(input("Enter the quantity restocked: "))

    tf=0
    for line in inventory:
        line=line.rstrip()
        newLine=line.split("\t")
        newLine = [int(s) if s.isdigit() else s for s in newLine]
        
        if addWarehouse in newLine and addParts in newLine:
            newLine[-1]+=addQuantity
            newLine[-1]=str(newLine[-1])
            tf=1
            inventoryFH.write('\n')
            for new in newLine:
                inventoryFH.write(new)
                inventoryFH.write('\t')
            
        else:
            inventoryFH.write('\n')
            inventoryFH.write(line)
            
    inventoryFH.close()
    if tf==0:
        print("ERROR" )
        
def provideToSection():
    inventoryFH=open('parts_inventory.txt','r')
    inventory=inventoryFH.read().splitlines()
    inventoryFH.close()
    inventoryFH=open('parts_inventory.txt','w')
    
    addParts=input("Enter the part code selected: ")
    addWarehouse=input("Enter the warehouse code selected: ")
    addQuantity=int(input("Enter the quantity provided: "))

    tf=0
    for line in inventory:
        line=line.rstrip()
        newLine=line.split("\t")
        newLine = [int(s) if s.isdigit() else s for s in newLine]
        
        if addWarehouse in newLine and addParts in newLine:
            newLine[-1]=newLine[-1]-addQuantity
            if newLine[-1]<0:
                print("Running low")
                newLine[-1]+=addQuantity
                newLine[-1]=str(newLine[-1])
                tf=1
                inventoryFH.write('\n')
                for new in newLine:
                    inventoryFH.write(new)
                    inventoryFH.write('\t')
                #inventoryFH.write('\t')                
            else:
                newLine[-1]=str(newLine[-1])
                tf=1
                inventoryFH.write('\n')
                for new in newLine:
                    inventoryFH.write(new)
                    inventoryFH.write('\t')
                #inventoryFH.write('\t')
        else:
            inventoryFH.write('\n')
            inventoryFH.write(line)
    inventoryFH.close()

    if tf==0:
        print("ERROR")    

def modifyPartsInventory():
    print('\nSelect the following operation to continue:')
    print('1. Add Parts Type to selected Warehouse')
    print('2. Restock from Supplier')
    print('3. Provide to Assembly Section')
    choice=int(input('Enter selection: '))
    if choice==1:
        addPartstoWarehouse()           
    elif choice==2:
        restockFromSupplier()
    elif choice==3:
        provideToSection()
        
def printPartsID():
    f = open('parts_inventory.txt','r')
    lines=f.readlines()
    lines.sort()
    print("Parts id\tWarehouse code\Quantity")
    for line in lines:
        print(line)
    f.close()
    
    
def trackWarehouse(warehouse):
    fileHandler=open('parts_inventory.txt','r')
    file=fileHandler.readlines()
    code=warehouse
    print("Parts id\tWarehouse code\Quantity")    
    for line in file:
        line=line.rstrip()
        newLine=line.split("\t")
        if(code in line):
            quantity=int(newLine[-1])
            if (quantity<10):
                print(line)

    fileHandler.close()
        

def printWarehouse(warehouse):
    fileHandler=open('parts_inventory.txt','r')
    file=fileHandler.readlines()
    detailsHandler=open('parts_details.txt','r')
    details=detailsHandler.readlines()
    code=warehouse
    index=[]
    quantity=[]
    storage=[]
    count=0
    for line in file:
        line=line.rstrip()
        newLine=line.split("\t")
        ind=[]
        qty=[]
        if(code in line):
            ind.append(newLine[0])
            qty.append(newLine[-1])
            count=count+1
        index.extend(ind)
        quantity.extend(qty)
    
    for data in details:
        data=data.rstrip()
        newData=data.split("\t")
        stor=[]
        stor.append(newData)
        storage.extend(stor)

    for j in range(count):
        for k in range(len(storage)):
            if(index[j] in storage[k]):
                storage[k].append(quantity[j])
                print(storage[k])

    fileHandler.close()
    detailsHandler.close()



def trackPartsInventory():
    print('\nSelect the following operation to continue:')
    print('1. Print inventory according to parts id')
    print('2. Print inventory according to warehouse')
    choice=int(input('Enter selection: '))
    if choice==1:
        printPartsID()           
    elif choice==2:
        choiceCode=input('Enter warehouse code to continue:')
        print('\nSelect the following operation to continue:')
        print('1. Track parts that has stock quantity less than 10 units')
        print('2. Print inventory')
        choicePrint=int(input('Enter selection: '))
        if choicePrint==1:
            trackWarehouse(choiceCode)
        elif choicePrint==2:
            printWarehouse(choiceCode)

def searchPartID():
    fileHandler=open('parts_inventory.txt','r')
    file=fileHandler.readlines()
    key=input("Enter part id:")
    print("Parts id\tWarehouse code\Quantity")
    for line in file:
        line=line.rstrip()
        newLine=line.split("\t")
        if(key in line):
            print(line)
    fileHandler.close()

def searchSupplier():
    fileHandler=open('parts_details.txt','r')
    file=fileHandler.readlines()
    key=input("Enter part id:")
    for line in file:
        line=line.rstrip()
        newLine=line.split("\t")
        if(key in line):
            index=newLine[-2]
    fileHandler.close()

    fileHandler=open('supplier_details.txt','r')
    file=fileHandler.readlines()
    print("Name\tH/P\temail\tPerson in charge")
    for line in file:
        line=line.rstrip()
        newLine=line.split("\t")
        if(index in line):
            print(line)
    fileHandler.close()
    
def searchPartsBySupplier():
    fileHandler=open('parts_details.txt','r')
    file=fileHandler.readlines()
    key=input("Enter supplier:")
    print("Id\tName\tSupplier\tAssembly Section Code")
    for line in file:
        line=line.rstrip()
        newLine=line.split("\t")
        if(key in line):
            print(line)
    fileHandler.close()

def searchPartsByID():
    fileHandler=open('parts_details.txt','r')
    file=fileHandler.readlines()
    key=input("Enter parts id:")
    print("Id\tName\tSupplier\tAssembly Section Code")
    for line in file:
        line=line.rstrip()
        newLine=line.split("\t")
        if(key in line):
            print(line)
    fileHandler.close()


def search():
    print('\nSelect the following operation to continue:')
    print('1. Search part record by part id')
    print('2. Search supplier details by part id')
    print('3. Search parts details by supplier')
    print('4. Search part details by part id')
    choice=int(input('Enter selection: '))
    if choice==1:
        searchPartID()           
    elif choice==2:
        searchSupplier()
    elif choice==3:
        searchPartsBySupplier()
    elif choice==4:
        searchPartsByID()
    
def menu():
    print('\nSelect the following operation to continue:')
    print('1. Add Section, Division or Parts in System')
    print('2. Modify Parts Inventory')
    print('3. Track Parts Inventory')
    print('4. Search')
    choice=int(input('Enter selection: '))
    if choice==1:
        createSystemDetails()
    elif choice==2:
        modifyPartsInventory()
    elif choice==3:
        trackPartsInventory()
    elif choice==4:
        search()
    menu()
                                   
menu()
            
        
        
        
    
