from pypdf import PdfMerger,PdfReader,PdfWriter
from fpdf import FPDF

pages = []
names=[]
class all:
    def __init__(self,filename):
        self.filename = filename
        names.append(self.filename)
    def choose(self):
        user_num=input(f"\nIn the \"{self.filename}\" PDF which page you want to merge,  if u have more then one page then use comma(,) i.e. \"1,2,3,4\":\t")
        pages.append(user_num)


def write_it(writer,reader,each_page_num):
    read_page= reader.pages[each_page_num-1]
    writer.add_page(read_page)


if __name__== '__main__':
    print("Hey guys you are welcome here;")
    print("This program is full dedicated to merge the file copy the spefic file and also to encrept it")
    print("So, you have to choose what you want to do:\n")
    value= int(input("1) Merge the spefic files  \t 2)Take page out \t 3) To conver txt into pdf  \t\t"))
    i=io =0
    if value == 1:
        print("\nSo you want to merge the files")
        while True:
            try:    
                while i!=2:    
                    i+=1
                    io=io+1
                    file_name = input(f"\nEnter the location for file number {io}, that you want to merge with extention[name.pdf]:\t")
                    send_1st= all(file_name)
                    send_1st.choose()
                    if i==2:
                        continuee = input("\nDo you want to ADD more file to merge, choose among (y/n):\t")
                        if continuee.upper() == 'Y':
                            i=i-1
                        else:
                            pass

                filename01 = input("Write New file Path to save this New Pdf: with extention[ path\\new_pdf.pdf]\t")
                merger = PdfMerger()        
                for i,nome in enumerate(names):
                    poge0=pages[i]
                    poge1 = poge0.split(",")
                    for poge in poge1:
                        pos = 0
                        pdf = str(nome)
                        page = int(poge)
                        oi= page-1
                        merger.merge(position=pos,fileobj= pdf,pages=(oi,page))
                        pos = pos +1           
                open1 = open(filename01,"wb")
                merger.write(open1)
                print(f"Saved, on{filename01}    \nSucess")
                break
            except Exception as error:
                print("You Didnt match the request")
                print(error)
                break     
                        
    elif value ==2:
        while True:    
            try:    
                file_n = input("eg: newfolder\\new\\pdf_file\\example.pdf \nEnter the file path name of pdf [with .pdf] :  ")
                reader = PdfReader(file_n)
                writer = PdfWriter()

                while True:
                    try:
                        which_page_list = (input(f"Select Pages number from this file \"{file_n}\"\n\tUse comma to seprerate:\t")).split(',')
                        for each_page_num in which_page_list:
                            write_it(writer, reader,int(each_page_num))
                        break    
                    except Exception as error:
                        print("You have not match the request")
                        print(error)

                new_name = input("where you want to save this Pdf file, write path and name [without .pdf]:\t")+".pdf"
                with open(new_name,'wb') as file:
                    writer.write(file)                  
                print(f"Saved {new_name}\n success")
                break    
            except Exception as error:
                print("You Didnt match the request")
                print(error)
                try_again=input("if want to try again press 1 else hit enter:\t\t") 
                if try_again == 1:pass
                else: break   

    elif value == 3:
        while True :   
            try:
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size = 15)

                file0 = input("Enter the Txt file location ---->>with extention(filepath\\demo\\text.txt) :\t ")
                fo = open(file0, "r")
                for x in fo:
                    pdf.cell(200, 10, txt = x, ln = 1, align = 'C')

                new_name = input("Enter the pdf path name to save your file into with extention ------->>(filepath\\folder\pdfile.pdf):\t") 
                print("processing..........................................")
                pdf.output(new_name)
                print(f"\n\ncheck here{new_name}\nSuccess, Done")
                break
            except Exception as error:
                print("You Didnt match the request")
                print(error)
                try_again=input("if want to try again press 1 else hit enter:\t\t") 

                if try_again == 1:pass
                else: break
            
    input("Hit any key to exit")
    
