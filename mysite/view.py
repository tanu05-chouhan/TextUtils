# I have created this file Tanu!.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def analyze(request):
    #get the text
    textdj = request.POST.get('text', 'default')

    #check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    #check if checkbox is on
    if removepunc=='on':
        punctuations = '''!()-[]{}:;'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in textdj:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {"purpose": "removed-punctuations", "analyzed_text": analyzed}
        textdj = analyzed

    if fullcaps=='on':
        analyzed = ""
        for char in textdj:
            analyzed = analyzed + char.upper()
        params = {"purpose": "Changed to Uppercase", "analyzed_text": analyzed}
        textdj = analyzed

    if newlineremover=='on':
        analyzed = ""
        for char in textdj:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {"purpose": "Removed newline", "analyzed_text": analyzed}
        textdj=analyzed

    if extraspaceremover=='on':
        analyzed = ""
        for index, char in enumerate(textdj):
            if not(textdj[index]==" " and textdj[index+1]==" "):
                analyzed = analyzed + char
        params = {"purpose": "Removed Extra Spaces", "analyzed_text": analyzed}
        textdj = analyzed

    if(removepunc!='on' and fullcaps!='on' and newlineremover!='on' and extraspaceremover!='on'):
        return HttpResponse("Error! Please select any options and try again....")

    return render(request, 'analyze.html', params)
