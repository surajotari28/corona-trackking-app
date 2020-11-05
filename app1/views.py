from django.shortcuts import render
import json
import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "80a239ad54msh4d38f2c63968fe3p152c1cjsn51518d94f340"
    }

response = requests.request("GET", url, headers=headers).json()

# Create your views here.
def Home(request):
    mylist = []
    corona = int(response['results'])
    for i in range(0, corona):
        mylist.append(response['response'][i]['country'])
    if request.method == 'POST':
        form = request.POST['selectedcountry']
        for i in range(0, corona):
            if form == response['response'][i]['country']:
                new = response['response'][i]['cases']['new']
                active = response['response'][i]['cases']['active']
                critical = response['response'][i]['cases']['critical']
                recovered = response['response'][i]['cases']['recovered']
                total = response['response'][i]['cases']['total']
                deaths = int(total) - int(active) - int(recovered)
        context = {'selectedcountry' : form, 'mylist' : mylist,'new' : new, 'active': active, 'critical': critical, 'recovered': recovered, 'total': total, 'deaths': deaths}
        return render(request, 'index.html', context)

    corona = int(response['results'])
    mylist = []
    for i in range(0, corona):
        mylist.append(response['response'][i]['country'])
        context = {'mylist':mylist}
        return render(request, 'index.html', context)
