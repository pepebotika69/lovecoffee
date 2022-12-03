# Create your views here.
from datetime import datetime

from django.http import HttpResponse


def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello, waka-waka!</h1>
            <p>The current time is {now}.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
