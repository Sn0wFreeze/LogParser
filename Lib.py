from datetime import datetime


def Open_File(dir: str):
    
    try:
        
        with open(dir, 'r') as file:
            
            file1 = file.read()
            file.close()
    
    except:
        
        return -1

    return file1



def Write_File(file_name: str, content: str):


    file_name += str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))+".txt"


    try:
        
        with open(file_name, 'w') as file:
            
            file.write(content)
            file.close()
    
    except:
         
        return -1
