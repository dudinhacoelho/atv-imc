import PySimpleGUI as sg

sg.theme('DarkPurple1')  

layout = [ 
            [sg.Text('Índice de Massa Corpórea - IMC')],
            [sg.Text('massa: '),sg.Input(key='-MASS-', size=(20,2))],
            [sg.Text('altura: '),sg.Input(key='-HEIGHT-', size=(21,2))],
            [sg.Push(),sg.Button('calcular IMC'),sg.Push()]
         ]

window = sg.Window('IMC',layout=layout,font='Arial 17')

while True:
    event, values = window.read()
    print(event,values)
    massa = float(values['-MASS-'])
    altura = float(values['-HEIGHT-'])
    imc = massa/(altura**2)
    sg.Popup(f'Seu IMC é {imc:.2f}', font='22')
    if event == sg.WIN_CLOSED or event == 'QUIT':
      break
