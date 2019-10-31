import textwrap

from django.http import HttpResponse
from django.views.generic.base import View


class HomePageView(View):

    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Issue Tracker</title>
            </head>
            <body>
                <style>
                .button {
                  background-color: #1E90FF;
                  border: none;
                  color: black;
                  padding: 15px 25px;
                  text-align: center;
                  font-size: 16px;
                  cursor: pointer;
                }

                .button:hover {
                  background-color: blue;
                }
                </style>
                <h1>Issue Tracker</h1>
                <form action="http://google.com">
                 <button class="button">Nova Issue</button>
                </form> 

            </body>
            </html>
        ''')
        return HttpResponse(response_text)
