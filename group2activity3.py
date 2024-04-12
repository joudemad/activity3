
import csv


def clearand_prepare(d):
    try:
                   
        print("Choose a column from below to clear and prepare data")
    
        while True:
            column=input("1.Branch\n2.Product\n3.Price\n4.Units sold\nEnter your choice:")
            c=[]
            a=[]

            if column=="1" or column=="Branch" or column=="branch":
                for y in d:
                    a.append(y[0])
            elif column=="2" or column=="Product" or column=="product":
                for i in d:
                    a.append(i[1])
            elif column=="3" or column=="Price" or column=="price":
                for i in d:
                    a.append(i[2])
            elif column=="4" or column=="Units sold" or column=="units sold":
                for i in d:
                    a.append(i[3])
            else:
                raise TypeError
            
            print(a)



            for i in a:
                if re.findall("[0-9]",i):
                    b = int(i)
                elif i == " " or i==None:
                    b = ""
                else:
                    raise ValueError            
                c.append(b)

            break

                
    except TypeError:
        print("\nWrong input!!!\n")
        clearand_prepare(d)
            



    except ValueError:
        print("\nNon-numerical column!!!\n")
        clearand_prepare(d)




        

    while True:
        try:

                    
            replace=0
                    
            print("Stage 2: Clear and Prepare Data")
            value=input("Would you like to replace the empty cells from this column with\n\n1.Maximum Value from column\n2.Minimum Value from column\n3.Average Value from column\n\nEnter your choice:")
            if value=="1" or value=="Maximum value" or value=="maximum value":
                replace=maximum(c)  
            elif value=="2" or value=="minimum value" or value=="Minimum value":
                replace=minimum(c)  

            elif value=="3" or value=="Average value" or value=="average value":
                replace=average(c)  
            else:
                print("\nInvalid! Try Again!\n\n")
                continue
     

            length=len(c)



            for i in range(length):
                if c[i]==None or c[i]=="" or c[i]==" ":
                    c[i]=replace
                else:
                    continue 

            print("All empty values are replaced with option:",value)    

            print(c)  
                         
            break






        except:
            print("\nWrong input!!!\n")
            continue


            

        




def loaddata():


    print("Stage 1: Load Data")
    x=input("Enter file name: ")
    while True:
        try:
            d=[]
            with open(x,"r") as filehandle:
                file=csv.reader(filehandle)
                print("File Exists.\nLoading file....\nFile successfully loaded!\n")
                next(file)
                for i in file:
                    d.append(i)
                    print(i)
                clearand_prepare(d)

                break


        except FileNotFoundError:
            print("Wrong Input.")
            x=input(" Please enter an already existing file name: ")
            




def main():
    print("---------------------------------\nWelcome to Data Analysis CLI\n---------------------------------")
    print("Program stages:\n\n1. Load Data\n2. Clean and prepare Data\n3. Analyse Data\n4. Visualise Data\n")
    
    loaddata()
    print("Thank you and Goodbye!")
main()