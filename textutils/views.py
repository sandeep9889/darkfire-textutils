# i hve created this file-sandeep
from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    print(request)
    return render(request,'index.html')
    #return HttpResponse("<h1>home</h1>") 

 

def analyze(request):
    #get the text
    djtext1=request.POST.get('text','default')
    # cheak the cheackbox value
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcounter=request.POST.get('charcounter','off')
    #printing the text
    print(djtext1)
    print(removepunc)
    # check the checkbox is on
    if(removepunc=='on'):
        # analyzed= djtext1  here to print what you return in server
        punctuations= '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed=""
        for char in djtext1:
            if char not in punctuations:
                analyzed= analyzed + char
        djtext1=analyzed      
        params = {'purpose': 'removed punctuation', 'analyzed_text':analyzed}
        #analyze the text
        #return render(request,'analyze.html',params)
    if(fullcaps=='on'):
        #this is analyze capital letter
        analyzed=""
        for char in djtext1: #im adding this comment
            analyzed=analyzed + char.upper() #upper is func that is to be capitalized
        
        params = {'purpose': 'changed to upper case', 'analyzed_text':analyzed}
        djtext1=analyzed
        #return render(request,'analyze.html',params)
    if(newlineremover=='on'):
        analyzed=''
        for char in djtext1:
            if char !='\n' and char!='\r':
                analyzed=analyzed+char
        params = {'purpose': 'new line remover', 'analyzed_text':analyzed}
        djtext1=analyzed
        #return render(request,'analyze.html',params)    
    if(extraspaceremover=='on'):
        analyzed=''
        for index,char in enumerate(djtext1):
            if not ( djtext1[index] ==" " and djtext1[index+1]==" "):
                analyzed=analyzed+char
        params = {'purpose': 'extra space remover', 'analyzed_text':analyzed}
        djtext1=analyzed
        #return render(request,'analyze.html',params)
    if(charcounter=='on'):
        analyzed=len(djtext1)
        params = {'purpose': 'character counter', 'analyzed_text':analyzed}
        djtext1=analyzed
        #return render(request,'analyze.html',params)
        
    if(charcounter!='on'and extraspaceremover!='on'and newlineremover!='on'and  fullcaps!='on' and  removepunc!='on'  ):
        return HttpResponse("ERROR")  
    return render(request,'analyze.html',params)                     




def aboutus(request):
    print(request)
    return render(request,'aboutus.html')   



def contactus(request):
    print(request)
    return render(request,'contactus.html')     


#def analyze(request):
    #djtext2=print(request.GET.get('text','default'))
    #print(djtext2)
    #return HttpResponse("remove punc")   
