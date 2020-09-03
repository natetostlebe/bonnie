import wolframalpha
import wikipedia
import requests
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

client = wolframalpha.Client("AQW6GP-E3ETQHT5VV")

def search(text=''):
    res = client.query(text)
    if res['@success'] == 'false':
        print('Question cannot be resolved')

    else:
        result = ''

        pod0 = res['pod'][0]

        pod1 = res['pod'][1]

        if (('definition' in pod1['@title'].lower()) or ('result' in pod1['@title'].lower()) or (pod1.get('@primary','false') == 'true')):
            result = resolveListorDict(pod1['subpod'])
            print(result)
        else:
            question = resolveListorDict(pod0['subpod'])
            question = removeBrackets(question)
            search_wiki(question)
#class GUIapp(App):
#    def build(self):

#        return(b)

#GUIapp().run()
