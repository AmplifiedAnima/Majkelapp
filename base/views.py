

from . models import Word, Trainingvalue, User, profile
from . forms import  WordForm, TrainingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django import forms
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


class NewWordForm(forms.Form):
    word= forms.CharField(label="New word")

class NewTrainingForm(forms.Form):
    training = forms.CharField(label= "")

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method =="POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exit')

        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')

    context={'page': page}
    return render(request,'base/login_register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()

    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')



    return render(request,'base/login_register.html',{'form': form})

def home(request):
  
    return render(request, 'base/home.html', {'home':home })



trainingp=[]

def trainingprograms(request):
    trainingp = Trainingvalue.objects.all()

    context= {'trainingp': trainingp}
    return render(request, 'base/trainingprograms.html', context)
    
def profiles(request):
    
    profiles = profile.objects.all()
    context = {'profiles':profiles}
    return render(request,'base/profiles.html',context)



def profilepage(request,pk):
    
    user = Trainingvalue.objects.get(id=pk)
    trainingplan = Trainingvalue.objects.all()
    profilopage= profile.objects.get(id=pk)
    user_training= Trainingvalue.objects.filter(user=profilopage.user)
    context ={'user_training':user_training,'user':user,'profilopage':profilopage,
    'trainingplan':trainingplan,}

    return render(request, 'base/profilepage.html' , context)
   

def trainingplan(request, pk):
    training = Trainingvalue.objects.get(id=pk)
    SQUAT1RM = Trainingvalue.objects.values('SQUAT1RM').get(id=pk)
    DEADLIFT1RM = Trainingvalue.objects.values('DEADLIFT1RM').get(id=pk)
    BENCHPRESS1RM= Trainingvalue.objects.values('BENCHPRESS1RM').get(id=pk)

    mezocykl=Trainingvalue.objects.values('mesocycle').get(id=pk)
    mesocycle= mezocykl.get('mesocycle')
      
    sq=SQUAT1RM.get('SQUAT1RM')
    dl=DEADLIFT1RM.get('DEADLIFT1RM')
    bp=BENCHPRESS1RM.get('BENCHPRESS1RM')
    
    ubebi=Trainingvalue.objects.values('upperbodbi').get(id=pk)
    upperbodybilateral =ubebi.get('upperbodbi')

    ubpperbis=Trainingvalue.objects.values('upperbodybisets').get(id=pk)
    upperbis= ubpperbis.get('upperbodybisets')

    upperbirepetitions=Trainingvalue.objects.values('upperbodybireps').get(id=pk)
    upperbireps = upperbirepetitions.get('upperbodybireps')

    ubeuni = Trainingvalue.objects.values('upperboduni').get(id=pk)
    upperbodyunilateral = ubeuni.get('upperboduni')

    uperunis=  Trainingvalue.objects.values('upperbodyunisets').get(id=pk)
    uperunis = uperunis.get('upperbodyunisets')

    uperunir = Trainingvalue.objects.values('upperbodyunireps').get(id=pk)
    uperunireps = uperunir.get('upperbodyunireps')

    lbbi= Trainingvalue.objects.values('lowerbodybi').get(id=pk)
    lowerbodybilateral = lbbi.get('lowerbodybi')

    lowbodybisets= Trainingvalue.objects.values('lowerbodybisets').get(id=pk)
    lowerbodybisetos = lowbodybisets.get('lowerbodybisets')

    lowerbodybirepos= Trainingvalue.objects.values('lowerbodybireps').get(id=pk)
    lowbireps=lowerbodybirepos.get('lowerbodybireps')

    lbuni=Trainingvalue.objects.values('lowerbodyuni').get(id=pk)
    lowerbodyunilateral= lbuni.get('lowerbodyuni')

    lowbodunis= Trainingvalue.objects.values('lowerbodyunisets').get(id=pk)
    lowbodyunisets=lowbodunis.get('lowerbodyunisets')

    lwbodunir= Trainingvalue.objects.values('lowerbodyunireps').get(id=pk)
    lowerbodunireps = lwbodunir.get('lowerbodyunireps')
    
    corex =  Trainingvalue.objects.values('coretraining').get(id=pk)
    coretraining = corex.get('coretraining')

    corexsets= Trainingvalue.objects.values('coresets').get(id=pk)
    corexosets= corexsets.get('coresets')
    
    corerepix=Trainingvalue.objects.values('corereps').get(id=pk)
    corexoreps = corerepix.get('corereps')

    wbexer= Trainingvalue.objects.values('wholebodyexercise').get(id=pk)
    wholebodyexercise = wbexer.get('wholebodyexercise')

    wbs=Trainingvalue.objects.values('wholebodysets').get(id=pk)
    wholebodset= wbs.get('wholebodysets')

    wbr=Trainingvalue.objects.values('wholebodyreps').get(id=pk)
    wholebodrep= wbr.get('wholebodyreps')

    #CASUALTRAINING
    gppsets1=[2,3]
    gppsets2=[3,4]
    gpprepsrange1=[16,24]
    gpprepsrange2=[16,30]
    #GENERAL PHYSICAL PREPRATION SETS AND REP RANGES and Cas
    gppsets1=[2,3]
    gppsets2=[3,4]
    gpprepsrange1=[16,24]
    gpprepsrange2=[16,30]
    gppsq1w=[round(sq*0.70),round(sq*0.72,5),round(sq*0.75) ]
    gppsq2w=[round(sq*0.72,5),round(sq*0.75),round(sq*0.77,5)]
    gppdl1w=[round(sq*0.70),round(sq*0.72,5),round(sq*0.75)]
    gppdl2w=[round(sq*0.72,5),round(sq*0.75),round(sq*0.77,5)]
    gppbp1w=[round(sq*0.70),round(sq*0.72,5),round(sq*0.75)]
    gppbp2w=[round(sq*0.72,5),round(sq*0.75),round(sq*0.77,5)]
    #ACCUMULATION PHASE SETS AND REP RANGES +(INTENSITY= PIREPLIN'S TABLE)
    accrepsrange1=[18,30]
    accrepsrange2=[12,24]
    accrepsrange3=[10,20]
    accrepsrange4=[10,18]
    accsets1=[3,6]
    accsets2=[3,6]
    accsets3=[2,4]
    accsets4=[2,3]
    accsq1w= [round(sq*0.55),round(sq*0.57,5), round(sq*0.60), round(sq*0.62,5), round(sq*0.65)]
    accsq2w= [round(sq*0.67,5),round(sq*0.70),round(sq*0.72,5),round(sq*0.75),round(sq*0.77,5)]
    accsq3w= [round(sq*0.8),round(sq*0.82,5),round(sq*0.85),round(sq*0.87,5),round(sq*0.9)]
    accsq4w= [round(sq*0.5),round(sq*0.52,5),round(sq*0.55),round(sq*0.6)]
    accdl1w= [round(dl*0.55),round(dl*0.57,5), round(dl*0.60), round(dl*0.62,5), round(dl*0.65)]
    accdl2w= [round(dl*0.67,5),round(dl*0.70),round(dl*0.72,5),round(dl*0.75),round(dl*0.77,5)]
    accdl3w= [round(dl*0.8),round(dl*0.82,5),round(dl*0.85),round(dl*0.87,5),round(dl*0.9)]
    accdl4w= [round(dl*0.5),round(dl*0.52,5),round(dl*0.55),round(dl*0.6)]
    accbp1w= [round(bp*0.55),round(bp*0.57,5), round(bp*0.60), round(bp*0.62,5), round(bp*0.65)]
    accbp2w= [round(bp*0.67,5),round(bp*0.70),round(bp*0.72,5),round(bp*0.75),round(bp*0.77,5)]
    accbp3w= [round(bp*0.8),round(bp*0.82,5),round(bp*0.85),round(bp*0.87,5),round(bp*0.9)]
    accbp4w= [round(bp*0.5),round(bp*0.52,5),round(bp*0.55),round(bp*0.6)]
    #PEAK
    peakrepsrange1=[8,10]
    peakrepsrange2=[5,8]
   
    peaksets1=[5,8]
    peaksets2=[3,5]
    peaksets3=('PEAK', 'MAX OUT!')
    peaksets4=('Rest...', 'Start from gpp again')
    
    peaksq1w= [round(sq*0.87,5),round(sq*0.9),round(sq*0.92,5), round(sq*0.95) ]
    peaksq2w= [round(sq*0.90),round(sq*0.92,5),round(sq*0.95)]
    peakdl1w= [round(sq*0.87,5),round(sq*0.9),round(sq*0.92,5), round(sq*0.95)]
    peakdl2w= [round(sq*0.90),round(sq*0.92,5),round(sq*0.95)]
    peakbp1w= [round(sq*0.87,5),round(sq*0.9),round(sq*0.92,5), round(sq*0.95)]
    peakbp2w= [round(sq*0.90),round(sq*0.92,5),round(sq*0.95)]

    if training.mesocycle =="CASUALTRAINING" or "GPP":
        a= (f'{gppsets1[0]} - {gppsets1[1]}'),(f'{gpprepsrange1[0]} - {gpprepsrange1[1]}'),(f'{gppsq1w[0]}kg, {gppsq1w[1]}kg, {gppsq1w[2]}kg')
        a1=(f'{gppsets1[0]} - {gppsets1[1]}'),(f'{gpprepsrange1[0]} - {gpprepsrange1[1]}'),(f'{gppdl1w[0]}kg, {gppdl1w[1]}kg, {gppdl1w[2]}kg')
        a2=(f'{gppsets1[0]} - {gppsets1[1]}'),(f'{gpprepsrange1[0]} - {gpprepsrange1[1]}'),(f'{gppbp1w[0]}kg, {gppbp1w[1]}kg, {gppbp1w[2]}kg')
        b= (f'{gppsets2[0]} - {gppsets2[1]}'),(f'{gpprepsrange2[0]} - {gpprepsrange2[1]}'),(f'{gppsq2w[0]}kg, {gppsq2w[1]}kg, {gppsq2w[2]}kg')
        b1=(f'{gppsets2[0]} - {gppsets2[1]}'),(f'{gpprepsrange2[0]} - {gpprepsrange2[1]}'),(f'{gppdl2w[0]}kg, {gppdl2w[1]}kg, {gppdl2w[2]}kg')
        b2=(f'{gppsets2[0]} - {gppsets2[1]}'),(f'{gpprepsrange2[0]} - {gpprepsrange2[1]}'),(f'{gppbp2w[0]}kg, {gppbp2w[1]}kg, {gppbp2w[2]}kg')
        c= f''
        c1=f''
        c2=f''
        d= f''
        d1=f''
        d2=f''

       

    if training.mesocycle == "ACC":
        a= (f'{accsets1[0]} - {accsets1[1]}'),(f'{accrepsrange1[0]} - {accrepsrange1[1]}'),(f'{accsq1w[0]}kg, {accsq1w[1]}kg, {accsq1w[2]}kg, {accsq1w[3]}kg, {accsq1w[4]}kg')
        a1=(f'{accsets1[0]} - {accsets1[1]}'),(f'{accrepsrange1[0]} - {accrepsrange1[1]}'),(f'{accdl1w[0]}kg, {accdl1w[1]}kg, {accdl1w[2]}kg, {accdl1w[3]}kg, {accdl1w[4]}kg')
        a2=(f'{accsets1[0]} - {accsets1[1]}'),(f'{accrepsrange1[0]} - {accrepsrange1[1]}'),(f'{accbp1w[0]}kg, {accbp1w[1]}kg, {accbp1w[2]}kg, {accbp1w[3]}kg, {accbp1w[4]}kg ')
        b= (f'{accsets2[0]} - {accsets2[1]}'),(f'{accrepsrange2[0]} - {accrepsrange2[1]}'),(f'{accsq2w[0]}kg, {accsq2w[1]}kg, {accsq2w[2]}kg, {accsq2w[3]}kg, {accsq2w[4]}kg')
        b1=(f'{accsets2[0]} - {accsets2[1]}'),(f'{accrepsrange2[0]} - {accrepsrange2[1]}'),(f'{accdl2w[0]}kg, {accdl2w[1]}kg, {accdl2w[2]}kg, {accdl2w[3]}kg, {accdl2w[4]}kg')
        b2=(f'{accsets2[0]} - {accsets2[1]}'),(f'{accrepsrange2[0]} - {accrepsrange2[1]}'),(f'{accbp2w[0]}kg, {accbp2w[1]}kg, {accbp2w[2]}kg, {accbp2w[3]}kg, {accbp2w[4]}kg')
        c= (f'{accsets3[0]} - {accsets3[1]}'),(f'{accrepsrange3[0]} - {accrepsrange3[1]}'),(f'{accsq3w[0]}kg, {accsq3w[1]}kg, {accsq3w[2]}kg, {accsq3w[3]}kg, {accsq3w[4]}kg')
        c1=(f'{accsets3[0]} - {accsets3[1]}'),(f'{accrepsrange3[0]} - {accrepsrange3[1]}'),(f'{accdl3w[0]}kg, {accdl3w[1]}kg, {accdl3w[2]}kg, {accdl3w[3]}kg, {accdl3w[4]}kg')
        c2=(f'{accsets3[0]} - {accsets3[1]}'),(f'{accrepsrange3[0]} - {accrepsrange3[1]}'),(f'{accbp3w[0]}kg, {accbp3w[1]}kg, {accbp3w[2]}kg, {accbp3w[3]}kg, {accbp3w[4]}kg')
        d= (f'{accsets4[0]} - {accsets4[1]}'),(f'{accrepsrange4[0]} - {accrepsrange4[1]}'),(f'{accsq4w[0]}kg, {accsq4w[1]}kg, {accsq4w[2]}kg, {accsq4w[3]}kg')
        d1=(f'{accsets4[0]} - {accsets4[1]}'),(f'{accrepsrange4[0]} - {accrepsrange4[1]}'),(f'{accdl4w[0]}kg, {accdl4w[1]}kg, {accdl4w[2]}kg, {accdl4w[3]}kg')
        d2=(f'{accsets4[0]} - {accsets4[1]}'),(f'{accrepsrange4[0]} - {accrepsrange4[1]}'),(f'{accbp4w[0]}kg, {accbp4w[1]}kg, {accbp4w[2]}kg, {accbp4w[3]}kg')


    if training.mesocycle == "PEAK":
        a= (f'{peaksets1[0]} - {peaksets1[1]}'),(f'{peakrepsrange1[0]} - {peakrepsrange1[1]}'),(f'{peaksq1w[0]}kg, {peaksq1w[1]}kg, {peaksq1w[2]}kg,  {peaksq1w[3]}kg')
        a1=(f'{peaksets1[0]} - {peaksets1[1]}'),(f'{peakrepsrange1[0]} - {peakrepsrange1[1]}'),(f'{peakdl1w[0]}kg, {peakdl1w[1]}kg, {peakdl1w[2]}kg,  {peakdl1w[2]}kg')
        a2=(f'{peaksets1[0]} - {peaksets1[1]}'),(f'{peakrepsrange1[0]} - {peakrepsrange1[1]}'),(f'{peakbp1w[0]}kg, {peakbp1w[1]}kg, {peakbp1w[2]}kg,  {peakbp1w[2]}kg')
        b= (f'{peaksets2[0]} - {peaksets2[1]}'),(f'{peakrepsrange2[0]} - {peakrepsrange2[1]}'),(f'{peaksq2w[0]}kg, {peaksq2w[1]}kg, {peaksq2w[2]}kg')
        b1=(f'{peaksets2[0]} - {peaksets2[1]}'),(f'{peakrepsrange2[0]} - {peakrepsrange2[1]}'),(f'{peakdl2w[0]}kg, {peakdl2w[1]}kg, {peakdl2w[2]}kg')
        b2=(f'{peaksets2[0]} - {peaksets2[1]}'),(f'{peakrepsrange2[0]} - {peakrepsrange2[1]}'),(f'{peakbp2w[0]}kg, {peakbp2w[1]}kg, {peakbp2w[2]}kg')
        c=(str(peaksets3[0]),"",str(peaksets3[0]))
        c1=(str(peaksets3[0]),"",str(peaksets3[1]))
        c2=(str(peaksets3[0]),"",str(peaksets3[0]))
        d= ()
        d1=()
        d2=str(peaksets4[0]),"",str(peaksets4[1])

    context={ 'a':a,'a1':a1,'a2':a2 ,'b':b,'b1':b1,'b2':b2, 'c':c,'c1':c1,
    'c2':c2, 'd':d, 'd1':d1,'d2':d2 ,'sq':sq,'dl':dl,'bp':bp,'trainingp':trainingp, 
    'training': training,
    'mesocycle': mesocycle,
    'upperbodybilateral': upperbodybilateral,
    'upperbodyunilateral': upperbodyunilateral,
    'lowerbodybilateral': lowerbodybilateral,
    'lowerbodyunilateral': lowerbodyunilateral,
    'coretraining': coretraining,
    'wholebodyexercise': wholebodyexercise,
    'wholebodset':wholebodset,
    'wholebodrep':wholebodrep,
    'upperbis' : upperbis,
    'upperbireps':upperbireps,
    'uperunis': uperunis,
    'uperunireps' : uperunireps,
    'lowbodyunisets':lowbodyunisets,
    'lowerbodunireps':lowerbodunireps,
    'lowerbodybisetos':lowerbodybisetos,
    'lowbireps': lowbireps, 
    'corexoreps':corexoreps,
    'corexosets':corexosets,
 
}
# 'lowerbodybisets':lowerbodybisets,
#        
#     lowbodybireps = Trainingvalue.objects.values('lowerbodybireps')
#     lowerbodybirepetitions= lowbodybireps.get('lowerbodybireps')
# 'lowerbodybirepetitions': lowerbodybirepetitions,
    return render(request, 'base/trainingplan.html', context )
           

def pliktest(request, pk):
    training = Trainingvalue.objects.get(id=pk) 
    sets1=[3,6]
    sets2=[3,6]
    sets3=[2,4]
    repsrange1=[18,30]
    repsrange2=[12,24]
    repsrange3=[10,20]
    u=100

    firstweek= [u*0.55, u*0.60, u*0.65]
    secondweek=[u*0.70,u*0.75,u*0.8]
    thirdweek=[u*0.8,u*0.85,u*0.9]
    a = f'Week 1 will consist of {sets1[0]}, {sets1[1]} sets of total reps {repsrange1[0]},{repsrange1[1]} at {round(firstweek[0])} kg,  {firstweek[1]}kg,{firstweek[2]}kg'
    b=  f'Week 2 will consist of {sets2[0]}, {sets2[1]} sets of total reps {repsrange2[0]},{repsrange2[1]} at {round(secondweek[0])} kg,  {secondweek[1]}kg,{secondweek[2]}kg'
    c=  f'Week 3 will consist of {sets3[0]}, {sets3[1]} sets of total reps {repsrange3[0]},{repsrange3[1]} at {round(thirdweek[0])} kg,  {thirdweek[1]}kg,{thirdweek[2]}kg'



    context= {'a':a,'b':b,'c':c,'training':training }
    return render(request, 'base/pliktest.html', context)

@login_required(login_url='/login')           
def addtrainingunit(request):
    training = TrainingForm()
    if request.method == "POST":
        training = TrainingForm(request.POST)
        if training.is_valid():
            trainingp.append(training)
            training.save()
            return redirect('trainingprograms')
        context={'training': training}
        return render(request, 'base/addtrainingunit.html',context)
    else:
        return render(request,'base/addtrainingunit.html',
        {'training': training})


def trainingsheet(request,pk):
    training = Trainingvalue.objects.get(id=pk)
    form = TrainingForm(instance=training)

    if request.method == 'POST':
        form=TrainingForm (request.POST,instance=training)
        if form.is_valid():
            form.save()
            return redirect('trainingprograms')

    context = {'form': form}
    return render(request,'base/trainingsheet.html',context)

@login_required(login_url='/login')
def deletetraining(request,pk):
    training = Trainingvalue.objects.get(id=pk)
    if request.method == 'POST':
        training.delete()
        return redirect ('trainingprograms')
    return render (request, 'base/deletetraining.html',{'obj': training})



words=[]

def dictionary(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    words= Word.objects.filter(
    Q(english__contains=q) |
    Q(polish__icontains=q) |
    Q(genre__icontains=q) )

    word_count = words.count()

    context={'words':words ,'word_count':word_count}

    return render(request, 'base/dictionary.html', context)  

def word(request, pk):
        word= Word.objects.get(id=pk)
        context={'word':word}
        return render(request, 'base/word.html', context)


@login_required(login_url='/login')
def addword(request):
    word = WordForm()
    if request.method=="POST":
        word = WordForm(request.POST)
        if word.is_valid():
            words.append(word)
            word.save()
            return redirect('dictionary')
        context = {'word':word}
        return render(request, 'base/addword.html',context)
    else:
        return render(request,'base/addword.html',
        {"word":word})

@login_required(login_url='/login')
def deleteword(request,pk):
    word = Word.objects.get(id=pk)
    if request.method == 'POST':
        word.delete()
        return redirect ('dictionary')
    return render (request, 'base/deleteword.html',{'obj': word})



@login_required(login_url='/login')
def updateword(request,pk):
    word = Word.objects.get(id=pk)
    form = WordForm(instance=word)

    if request.method == 'POST':
        form = WordForm(request.POST,instance=word)
        if form.is_valid():
            form.save()
            return redirect('dictionary')

    context = {'form': form}
    return render(request,'base/wordform.html',context)
    


