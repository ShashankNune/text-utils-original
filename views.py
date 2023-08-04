from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")
def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')
    punctuations='''!@#$%^&*()-={[]};:'",./?\|`~<>'''
    params={'purpose':'','analyzed_text':djtext}
    analyzed=''
    var=''
    if removepunc == 'on':
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        var+='Removed Punctuations'
        params={'purpose':var,'analyzed_text':analyzed}
    if fullcaps=='on':
        if removepunc=='off':
            djtext=djtext.upper()
            analyzed=djtext
            var+='Full Capitalized'
        else:
            analyzed=analyzed.upper()
            var+=', Full Capitalized'
        params={'purpose':var,'analyzed_text':analyzed}
    if newlineremover=='on':
        text=''
        if removepunc=='on' or fullcaps=='on':
            temp=analyzed
            var+=', Removed New Lines'
        else:
            temp=djtext
            var+='Removed New Lines'
        for char in temp:
            if char!='\n'and char!='\r':
                text+=char
        analyzed=text
        params={'purpose':var,'analyzed_text':analyzed}
    if extraspaceremover=='on':
        text=''
        if removepunc=='on' or fullcaps=='on'or newlineremover=='on':
            temp=analyzed
            var+=', Removed Extra Spaces'
        else:
            temp=djtext
            var+='Removed Extra Spaces'
        for index,char in enumerate(temp):
            if not (temp[index]==' 'and temp[index+1]==' '):
                text+=char
        analyzed=text
        params={'purpose':var,'analyzed_text':analyzed}
    if charcount=='on':
        if removepunc=='on'or fullcaps=='on'or newlineremover=='on'or extraspaceremover=='on':
            params['count']='The length of text= '
            params['count']+=str(len(analyzed))
        else: 
            params['count']="The length of text= "
            params['count']+=str(len(djtext))
    if removepunc=='on'or fullcaps=='on'or newlineremover=='on'or extraspaceremover=='on'or charcount=='on':
            return render(request,'analyze.html',params)
    else:
        params={'purpose':'','analyzed_text':'Error'}
        return render(request,'analyze.html',params)