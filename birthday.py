def reader():
    file= open("birth.txt",encoding="utf8")
    for line in file:  
        words=line.split()     
        i=line
        print(i," \n")

        
def dict1() :
    file=open('birth.txt',encoding='utf8')
    dict_id=dict()
    message=dict()
    metadata=dict()
    dict_1=dict()
    birthday=list()
    count=1
    count2=0
    for line in file:
        macaf = line.find('-')
        if(line[1] == "."):
                result = line[macaf+1::] 
                colon = result.find(':')
                if(colon>0):
                    result2 = result[0:colon]
                    if not dict_id.get(result2):   
                        dict_id[result2]=count
                        count=count+1
                    message['datetime']=line[0:macaf-1]
                    message['id']=dict_id[result2]
                    message['text']=result[colon+1::].strip() 
                    birthday.append(message.copy())   
        count2=count2+1
        if(count2==1):
            creation_date=line[0:macaf-1]
        if(count2==2):
            team=line.index("הקבוצה")
            team1=line.index("ידי")
            chat_name=line[team+6:team1-1]
            creator=line[team1+4::]
    num_of_participants=len(dict_id)
    metadata["chat_name"]=chat_name
    metadata["num_of_participants"]=num_of_participants
    metadata["creator"]=creator
    metadata["creation_date"]=creation_date
    dict_1["messages"]=birthday
    dict_1["metadata"]=metadata
    for i,j in metadata.items():
        print(i,j)

        
