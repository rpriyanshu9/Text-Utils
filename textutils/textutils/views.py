
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    djremovepunc = request.POST.get('removepunc', 'off')
    djcapson = request.POST.get('capson', 'off')
    djnewlineremove = request.POST.get('newlineremove', 'off')
    djspaceremove = request.POST.get('spaceremove', 'off')
    djcountchar = request.POST.get('countchar', 'off')

    if djremovepunc == "on":
        punc = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punc:
                analyzed += char
        params = {'purpose': 'remove punctuatuations', 'analyzed_text': analyzed}
        djtext=analyzed

    if djcapson=="on":
        analyzed=""
        for char in djtext:
            analyzed+=char.upper()
        params = {'purpose': 'Uppercase the text', 'analyzed_text': analyzed}
        djtext = analyzed

    if djnewlineremove=="on":
        analyzed=""
        for char in djtext:
            if char!='\n':
                analyzed+=char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if djspaceremove=="on":
        analyzed=""
        for index,char in enumerate(djtext):
            if djtext[index]==" ":
                pass
            else:
                analyzed+=char
        params = {'purpose': 'Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if djcountchar=="on":
        analyzed="The character count is "
        count=0
        for char in djtext:
            count+=1
        analyzed+=f'{count}'
        params = {'purpose': 'Uppercase the text', 'analyzed_text': analyzed}
        djtext = analyzed

    if djremovepunc!="on" and djspaceremove!="on" and djcapson!="on" and djcountchar!="on" and djnewlineremove!="on":
        return HttpResponse("Error, please choose at least one of the options.")
    else:
        return render(request, 'analyze.html', params)
