

u  = Trainingvalue.objects.values_list('maximalvalue').get(id=1)
print(type(u))
    
def lprogressgpp(x):
       
    sets1=(3,6)
    sets2=(3,6)
    sets3=(2,4)
    repsrange1=(18,30)
    repsrange2=(12,24)
    repsrange3=(10,20)

            
    z=(print('Week 1 will consist of', str(sets1[0]),'-',str(sets1[1]), 'sets',' of total reps', 
    str(repsrange1[0]),'-',str(repsrange1[1]), 'at:',str(round(x * 0.55)),'kg',',',str(x * 0.60),'kg',',',str(x * 0.65),'kg') ,
    print('Week 2 will consist of', str(sets2[0]),'-',str(sets2[1]),'sets',' of total reps ',
    str(repsrange2[0]),'-',str(repsrange2[1]), 'at:',str(x * 0.70),'kg',',',str(x * 0.75),'kg',',',str(x * 0.80),'kg'),
    print('week 3 will consist of', str(sets3[0]),'-',str(sets3[1]),'sets',' of total reps',  
    str(repsrange3[0]),'-',str(repsrange3[1]), 'at:',str(x * 0.80),'kg',',',str(x * 0.85),'kg',',',str(x * 0.90),'kg'))

    return z

lprogressgpp(200)

# #%%%        Reps/sets   optimal     Total range
# # 55-65     3-6            24           18-30
# # 70-80     3-6            18           12-24
# # 80-90     2-4            15           10-20
# # 90 +      1-2            4            10    def lprogresgpp(x):
# #         sets1=(3,6)
# #         sets2=(3,6)
# #         sets3=(2,4)
# #         repsrange1=(18,30)
# #         repsrange2=(12,24)
# #         repsrange3=(10,20)
        
# #         z =(
# #         print('Week 1 will consist of', str(sets1[0]),'-',str(sets1[1]), 'sets',' of total reps', 
# #         str(repsrange1[0]),'-',str(repsrange1[1]), 'at:',str(round(x * 0.55)),'kg',',',str(x * 0.60),'kg',',',str(x * 0.65),'kg') ,
# #         print('Week 2 will consist of', str(sets2[0]),'-',str(sets2[1]),'sets',' of total reps ',
# #         str(repsrange2[0]),'-',str(repsrange2[1]), 'at:',str(x * 0.70),'kg',',',str(x * 0.75),'kg',',',str(x * 0.80),'kg'),
# #         print('week 3 will consist of', str(sets3[0]),'-',str(sets3[1]),'sets',' of total reps', 
# #         str(repsrange3[0]),'-',str(repsrange3[1]), 'at:',str(x * 0.80),'kg',',',str(x * 0.85),'kg',',',str(x * 0.90),'kg'))

        
        
#     z = print(lprogresgpp(x))


# def waveprogacc(x):
#     sets1=(3,6)
#     sets2=(3,6)
#     sets3=(2,4)
#     sets4=(1,2)
#     repsrange1=(18,30)
#     repsrange2=(12,24)
#     repsrange3=(10,20)
#     repsrange4 =10
#     print('Week 1 will consist of', str(sets3[0]),'-',str(sets3[1]),' of total reps', str(repsrange1[0]),'-',str(repsrange1[1]), 'at:',str(x * 0.7),',',str(x * 0.75),',',str(x * 0.80))
#     print('Week 2 will consist of', str(sets2[0]),'-',str(sets2[1]),' of total reps ', str(repsrange2[0]),'-',str(repsrange2[1]), 'at:',str(x * 0.70),',',str(x * 0.75),',',str(x * 0.80))
#     print('week 3 will consist of', str(sets3[0]),'-',str(sets3[1]),' of total reps', str(repsrange3[0]),'-',str(repsrange3[1]), 'at:',str(x * 0.80),',',str(x * 0.85),',',str(x * 0.90))





# lprogresgpp(100)
# #print(f'remember to check your max in between')



# # week 1 = 
# # week 2 =
# # week 3 = 


# # print(defineintensity(100))
 
#  # week1=[[x * 0.55],[x * 0.60],[x * 0.65]]
#  #   week2=[[x * 0.7],[x * 0.75],[x * 0.80]]
#   #  week3=[[x * 0.80],[x * 0.85],[x * 0.90]]
    
# # words={


# # 'transesophageal': 'przezprzełykowy',
# # 'stent' :'stent,proteza rozszerzająca naczynie',
# # 'drain':'sączkowanie',
# # 'dilated renal tubule' : 'rozszerzony kanalik nerkowy',
# # 'blister': 'listek tabletek',
# # 'krwotok':'haemorrhage',
# # 'healthcare proxy': 'pełnomocnik w sprawie decyzji medycznych',
# # 'diverticular disease':'choroba uchyłkowa',
# # 'focal segmental glomerulosclerosis':'ogniskowe segmentalne szkliwienie kłębuszków',
# # 'labyrinth': 'błędnik',
# # 'ear,nose and throat doctor,otolaryngologist' : 'otolaryngolog',
# # 'fallopian tube' : 'jajowód',
# # 'mrsa bacteria' : 'bakteria gronkowca złocistego',
# # 'carotid aneurysm': 'tętniak tętnicy szyjnej',
# # 'herpes': 'opryszczka',
# # 'shingles': "półpasiec",
# # 'Hemosiderin':'Hemosyderyna',
# # 'cauda equina syndrom ': 'syndrom końskiego ogona',
# # 'triscuspid regurgitation':'niedomykalność zastawki trójdzielnej',
# # # }
# # #    <form method="GET" action ="{% url 'home' %}">

# # #         <input type ="text" name="q" placeholder="Search Rooms..."/>


