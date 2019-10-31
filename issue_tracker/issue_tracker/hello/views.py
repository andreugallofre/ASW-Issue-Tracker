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
                <form action="nova_issue">
                 <button class="button">Nova Issue</button>
                </form>
                <b>Issues:</b>

            </body>
            </html>
        ''')
        return HttpResponse(response_text)

class NovaIssue(View):

    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <html>
                  <head>
                      <title>Nova Issue</title>
                  </head>
                  <body>
                    <h1>Nova Issue</h1>

                     <form action="issue">
                      <div>
                        <label>Títol</label>
                        <input type="text">
                      </div>
                      <style>
                      label {
                        display: inline-block;
                        width: 140px;
                        text-align: left;
                      }​
                      button {
                        background-color: #1E90FF;
                        border: none;
                        color: black;
                        padding: 15px 25px;
                        text-align: center;
                        font-size: 16px;
                        cursor: pointer;
                      }
                      </style>
                      <label>Descripció</label>
                      <textarea name="comment" rows="10" cols="50">Expliqueu l'issue...</textarea><br>
                      <label>Tipus</label>
                        <select name="tipus">
                          <option value="bug">Bug</option>
                          <option value="millora">Millora</option>
                          <option value="proposta">Proposta</option>
                          <option value="tasca">Tasca</option>
                        </select><br>
                      <label>Prioritat</label>
                      <select name="prioritat">
                        <option value="trivial">Trivial</option>
                        <option value="menor">Menor</option>
                        <option value="major">Major</option>
                        <option value="critica">Crítica</option>
                        <option value="bloquejant">Bloquejant</option>
                      </select><br>
                    <button class="button">Crear issue</button>
                    </form>


                  </body>
            </html>
        ''')
        return HttpResponse(response_text)

class Issue(View):

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
                <form action="nova_issue">
                 <button class="button">Nova Issue</button>
                </form>
                <b>Issues:</b>

            </body>
            </html>
        ''')
        return HttpResponse(response_text)
