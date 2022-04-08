import markdown2
# from django.http import HttpResponse
from django.shortcuts import render
from . import util
# from django import forms
from django.http import HttpResponseRedirect
# from django.urls import reverse
import random
import math


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


# ########################################
# ########## RUTA PARA ENTRIES ###########
# ########################################


def entry(request, title):
    # Obtener contenido en formato Markdown de carpeta entries/
    md_content = util.get_entry(title)

    # Chequear si el entry no existe
    if not md_content:
        return render(request, "encyclopedia/notfound.html", {
            "title": title
        })

    # Convertir contenido de Markdown a HTML
    html_content = markdown2.markdown(md_content)
    
    # Llamar template entry.html, pasar title y content
    return render(request, "wiki/entry.html", {
        "title": title,
        "content": html_content
    })


# ########################################
# ######### RUTA PARA BÚSQUEDAS ##########
# ########################################
def search(request):

    # Get string from search form and format it correctly
    search = request.POST.get('q')
    search = nicely(search.strip().title())

    # Try to find the entry
    found = util.get_entry(search)

    # If entry exists, redirect to entry's page
    if found:
        to_redirect = '/wiki/' + search # <-- SE SUPONE QUE DEBO USAR REVERSE, PERO NO ME LIGA
        return HttpResponseRedirect(to_redirect)

    # IF ENTRY DOES NOT EXIST, TRY TO SEARCH SUBSTRINGS !!!

    # Get list of existing entries
    entries = util.list_entries()

    # List of found entries that contain the substring "search"
    found = []
    for i in range(len(entries)):
        if search.upper() in entries[i].upper():
            found.append(entries[i])

    # If we find entries, redirect to results Page
    if found:
        to_redirect = '/results/' + search.lower()
        return HttpResponseRedirect(to_redirect)

    # If nothing found at all, redirecto to not_found Page
    to_redirect = '/not_found/' + search.lower()
    return HttpResponseRedirect(to_redirect)


def results(request, title):
    entries = util.list_entries()

    # List of found entries that contain the substring "search"
    found = []
    for i in range(len(entries)):
        if title in entries[i].lower():
            found.append(entries[i])

    return render(request, "encyclopedia/results.html", {
        "entries": found
    })


def not_found(request, title):
    return render(request, "encyclopedia/notfound.html", {
            "title": title
        })


# Función que simplemente pone en CAPS strings "html" y "css"
def nicely(title):
    if title.upper() == "HTML" or title.upper() == "CSS":
        title = title.upper()
    return title


# ##########################################
# ######### RUTA PARA RANDOM PAGE ##########
# ##########################################

def random_page(request):

    # Obtener random entry de la lista de entries
    entries = util.list_entries()
    entry = random_pick(entries)
    # Redirect to entry's Page
    to_redirect = '/wiki/' + entry
    return HttpResponseRedirect(to_redirect)


# Función que retorna un elemento random de una lista
def random_pick(entries):
    index = math.floor(random.random() * len(entries))
    return entries[index]


# ##################################################
# ########## PATH TO CREATE NEW PAGE ###############
# ##################################################

def new_page(request):
    # Si request es POST, intentar crear el nuevo entry
    if request.method == "POST":
        # Obtener title y content de formulario
        new_title = request.POST.get('new_title')
        new_content = request.POST.get('new_content')
        # Capitalize the first letter (without changing the rest), also strip() just in case
        new_title = my_upper(new_title.strip())
        # If title already exists, redirect to Error Page
        if util.get_entry(new_title):
            to_redirect = "/already_exists/" + new_title.lower()
            return HttpResponseRedirect(to_redirect)
        # If title is new, create new entry and redirect to it's Page
        else:
            util.save_entry(new_title, new_content)
            to_redirect = '/wiki/' + new_title
            return HttpResponseRedirect(to_redirect)
    # Si request no es POST, render new_page Page
    else:
        return render(request, "encyclopedia/new_page.html")


def already_exists(request, title):
    # return HttpResponse("PAGE ALREADY EXISTS")
    title = my_upper(nicely(title))
    return render(request, "encyclopedia/already_exists.html", {
        "title": title
    })


# Capitalize the first letter of every word in a string, don't change anything else
def my_upper(new_title):
    words = new_title.split()
    new_words = ""

    for word in words:
        first = word[:1].upper()
        rest = word[1:]
        new_words = new_words + first + rest + " "
    return new_words.strip()


# #####################################################
# ################ PATH TO EDIT PAGE ##################
# #####################################################

def edit_page(request):

    if request.method == "POST" and request.POST.get('sub_method') == "POSTING":
        title = request.POST.get('title')
        content = util.get_entry(title)
        return render(request, "wiki/edit_page.html", {
            "title": title,
            "content": content
        })
    elif request.method == "POST" and request.POST.get('sub_method') == "PATCHING":
        title = request.POST.get('title')
        content = request.POST.get('edit_content')

        # return HttpResponse(content)

        util.save_entry(title, content)
        md_content = util.get_entry(title)
        html_content = markdown2.markdown(md_content)
        return render(request, "wiki/entry.html", {
            "title": title,
            "content": html_content
        })


