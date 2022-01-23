import os
import random
from ast import Pass
from cgitb import text

import PySimpleGUI as sg


class PassGen:
    def __init__(self):
        #layout
        sg.theme('Black')
        layout = [
            [sg.Text('Site/Software', size=(10, 1)), sg.Input(key='site', size=(20, 1))],
            [sg.Text('Email/Usuario', size=(10, 1)), sg.Input(key='user', size=(20, 1))],
            [sg.Text('Quantidade de Caracteres'),
            sg.Combo(values=list(range(1, 30)),
                    key='total_chars',
                    default_value=1,
                    size=(3, 1))
            ],
            [sg.Output(size=(30, 5))],
            [sg.Button(button_text='Gerar Senha', size=(10, 5))]

        ]


        # Declarar a janela
        self.window = sg.Window('Password Generator', layout)

    def Init(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Gerar Senha':
                password = self.password_generate(values)
                self.SavePassword(password, values)
    
    def password_generate(self, values):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVXWZabcdefghijklmopqrstuvxwz1234567890!@#$%*()_+?-=<>çÇ'
        chars = random.choices(char_list, k=int(values['total_chars']))
        password = ''.join(chars)
        return password

    def SavePassword(self, password, values):
        file = open('senhas.txt', 'a')
        file.write(f'Site: {values["site"]}, Usuário: {values["user"]}, Senha: {password}\n')
        print('Aquivo salvo com suceso!')

gen = PassGen()
gen.Init()
