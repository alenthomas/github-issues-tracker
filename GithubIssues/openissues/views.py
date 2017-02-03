from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import datetime, requests, json

INVALID_ERROR = {'error':True, 'message':"Invalid url, Please try again"}

API = "https://api.github.com/repos/"

@method_decorator(csrf_exempt, name='dispatch')
class HomePage(View):

    def get(self, request):
        return render(request, 'openissues/home.html')

    def post(self, request):
        link = request.POST.get('url', None)
        url_list = link.split('/')
        try:
            for words in url_list:
                if 'github.com' in words:
                    index = url_list.index(words)
            owner, repo = url_list[index+1], url_list[index+2]
        except UnboundLocalError:
            return self.error(request, INVALID_ERROR)

        api = API + owner + '/' + repo + '/issues?status=open&page='
        open_issues, count = 0, 0

        issues_list = []

        while(True):
            count += 1
            final_url = api + str(count)
            print(final_url)
            api_response = requests.get(final_url)
            data = json.loads(api_response.text)
            if(len(data) == 0):
                break
            open_issues += len(data)
            issues_list.extend(data)

        return render(request, 'openissues/home.html')

    def error(self, request, message):
        return render(request, 'openissues/home.html', message)
