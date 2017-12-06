from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Movies, Wish, Users
from autoCompleteTrie import *
import json
import pandas as pd
import re
import numpy as np
from sklearn.neighbors import NearestNeighbors
# from .signals import delete_wishlist
global username
useri = -1 
def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    print("inside homepage")
    context = {'movie_list': Movies.objects.all()}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def login(request):
    username = request.GET.get('username')
    pw = request.GET.get('password')
    data = {
        'success' : False
    }
    global userid
    users= [x[0].split(' (')[0] for x in Users.objects.values_list('username')]
    if username not in users:    
        return JsonResponse(data)
    userid = Users.objects.filter(username = username).values_list('userid')[0][0]
    truepw = Users.objects.filter(username = username).values_list('password')[0][0]
    print (userid,"userid")
    print (truepw)
    if truepw != pw:
        return JsonResponse(data)
    data = {
        'success' : True
    }
    return JsonResponse(data) 

def singup(request):
    # insert into user database
    username = request.GET.get('username')
    pw1 = request.GET.get('password1')
    pw2 = request.GET.get('password2')
    gender = request.GET.get('gender')
    loc = request.GET.get('location')
    print (pw1)
    print (pw2)
    print (username)
    if pw1 != pw2:
        data = {
            'notvalid' : True
        }        
    else:
        try:
            Users(username=username, password=pw1, location=loc, gender=gender).save()    
            data = {
                'notvalid': False
            }  
        except:
            data = {
                'notvalid' : True
            }
    # return searchdatabase
    return JsonResponse(data)

def mainboard(request):
    print("inside mainboard")
    #print(wishmovie)
    context = {'movie_list': Movies.objects.all()}
    data = {
        'exists': False
    }
    JsonResponse(data)
    return render(request, 'polls/details.html', context)

def insertwishlist(request):
    print("something for debug")
    print(request)
    # insert to wisttable , RETURN true/false
    wishmovie = request.GET.get('movie', None)
    # userid = request.GET.get('userid', None)
    #console.log(wishmovie)
    print(wishmovie)
    print(userid)
    exist = Wish.objects.filter(userid=userid, movieid=wishmovie)
    if exist:
        data = {
            'exists': True
        }
    else:
        Wish(userid=userid, movieid=wishmovie).save()
        data = {
            'exists': False
        }
    return JsonResponse(data)

def autocomplete(request):
    # input is prefix;
    # build trie tree, return result
    # out
    print("inside autocompute")
    if request.is_ajax():
        q = request.GET.get('term', '')
        print (q)
        Entries= [x[0].split(' (')[0] for x in Movies.objects.values_list('title')]
        trie = Trie()
        trie.initializeTrie(Entries)
        data = trie.autoComplete(q)
        print (data)
	#places = Place.objects.filter(city__icontains=q)
        #results = []
        #for pl in places:
        #    place_json = {}
        #    place_json = pl.city + "," + pl.state
        #    results.append(place_json)
        data = json.dumps(data)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
    #return render(request, 'polls/search.html', context)
def search(request):
    # INPUT : string, part of movie name
    # OUTPUT: table, all the matchrecords
    searchmovie = request.GET.get('qquery', None)
    print(searchmovie)
    if(searchmovie == None):
        searchmovie = "shesfsd"
    data = Movies.objects.filter(title__icontains=searchmovie)
    context = {'movie_list': data}
    return recommendation(request)   
    # return render(request, 'polls/search.html', context)

def searchupdate(request):
    # INPUT : string, part of movie name
    # OUTPUT: table, all the matchrecords
    searchmovie = request.GET.get('qquery', None)
    print(searchmovie)
    if(searchmovie == None):
        searchmovie = "she"
    data = Movies.objects.filter(title__icontains=searchmovie)
    print(data)
    context = {'movie_list': data}
    #return render(request, 'polls/search.html', context)
    html = render_to_string('polls/search.html', context)
    return HttpResponse(html)

def wishlist(request):
    # return wishtable
    # userid = request.GET.get('userid', None)
    global userid
    print(userid)
    wishlist = Wish.objects.filter(userid=userid).values_list('movieid')
    context = {'movie_list': Movies.objects.filter(movieid__in=wishlist)}
    # return recommendation(request)
    return render(request, 'polls/wishlist.html', context)

def deletepost(request):
    # perform delete opration
    wishmovie = request.GET.get('movie', None)
    # userid = request.GET.get('userid', None)
    exist = Wish.objects.filter(userid=userid, movieid=wishmovie)
    if exist:
        # exist.delete()
        for instance in exist:
            instance.delete()
        print("insert delete before delete wish")
        # delete_wishlist(sender=Wish, instance=exist, user=request.user)
        data = {
            'exists': True
        }
    else:
        data = {
            'exists': False
        }
    wishlist = Wish.objects.filter(userid=userid).values_list('movieid')
    context = {'movie_list': Movies.objects.filter(movieid__in=wishlist)}
    return render(request, 'polls/wishlist.html', context)
    #return JsonResponse(data)

def profile(request):
    print("insideprofile")
    data = {
          'name' : 'Admin User',
          'gender' : 'female',
          'location' : 'Champaign'
    }
    context = {'user_info' : data}
    return render(request, 'polls/profile.html', context)

def profileupdate(request):
    # userid = request.GET.get('userid', None)
    newname = request.GET.get('newname', None)
    newgender = request.GET.get('newgender', None)
    newlocation = request.GET.get('newlocation', None)

    # perform user database update here
    # update = Users.objects.get(userid=userid)
    update = Users.objects.get(userid=userid)
    if update:
        update.username = newname
        update.gender = newgender
        update.location = newlocation
        update.save()
    else:
        Users(userid=userid, username=newname, gender=newgender, location=newlocation).save()

    print(newname)
    data = {
          'name' : newname,
          'gender' : newgender,
          'location' : newlocation
    }
    context = {'user_info' : data}
    print(context)
    html = render(request, 'polls/profile.html', context)
    return HttpResponse(html)
    #return render(request, 'polls/profile.html', context)

def recommendation(request):
    global userid
    arr = np.load("/home/shared/workfolder/MovieTogetherDjango/mysite/movie2arr.npy")
    with open("/home/shared/workfolder/MovieTogetherDjango/mysite/mid2idx.json", 'r') as f:
        mid2idx = json.load(f)
    idx2mid = {mid2idx[k]:k for k in mid2idx}
    wishlist = Wish.objects.filter(userid=userid).values_list('movieid')
    idl = [mid2idx[str(mid[0])] for mid in wishlist]
    if len(idl) == 0:
        mid = [44194, 44199, 44665, 44828, 45081, 45186, 45499, 45517, 45722, 45730]
        context = {'recommand_list': Movies.objects.filter(movieid__in=mid)}
        return render(request, 'polls/search.html', context) 
    vec = np.mean(arr[idl, ], axis=0)
    nbrs = NearestNeighbors(n_neighbors=10+len(wishlist), algorithm='auto').fit(arr)
    distances, indices = nbrs.kneighbors(np.array([vec, np.zeros(arr.shape[1])]))
    result = [i for i in indices[0] if i not in idl][:10]
    retmid = [idx2mid[i] for i in result]

    users = Wish.objects.values_list('userid').distinct()
    users = [user[0] for user in users]
    wishlist = Wish.objects.filter(userid=userid).values_list('movieid')
    wishlist = [mid[0] for mid in wishlist]
    score = 0
    for u in users:
        temp = Wish.objects.filter(userid=u).values_list('movieid')
        temp = [mid[0] for mid in temp]
        s = len(set(wishlist) & set(temp))
        if u != userid and s > score:
            score = s
            uid = u
    if score == 0:
        context = {'recommand_list': Movies.objects.filter(movieid__in=retmid)}
    else:
        context = {'recommand_list': Movies.objects.filter(movieid__in=retmid), 'recommand_friend': Users.objects.filter(userid=uid)}
    print(context)
    return render(request, 'polls/search.html', context)

# def friendRecommendation(request):
#     global userid
#     users = Users.objects.values_list('userid').distinct()
#     users = [user[0] for user in users]
#     wishlist = Wish.objects.filter(userid=userid).values_list('movieid')
#     wishlist = [mid[0] for mid in wishlist]
#     score = 0
#     for u in users:
#         temp = Wish.objects.filter(userid=u).values_list('movieid')
#         temp = [mid[0] for mid in temp]
#         s = len(set(wishlist) & set(temp))
#         if u != userid and s > score:
#             score = s
#             uid = u
#     if score == 0:
#         context = {}
#     else:
#         context = {'recommand_friend': Users.objects.filter(userid=uid)}
#     return render(request, 'polls/search.html', context) 
