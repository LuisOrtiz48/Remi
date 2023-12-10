import remi.gui as gui
from remi import start, App
import subprocess

class Algoritmos(App):

    def main(self):
        container = gui.Container(width = '100%', height = '100%', margin ='auto auto', style={
            'background': '#3C86E6'
        })

        #Titulo
        self.barratitulo = gui.Container(width = '100%', height = '100px', margin = 'auto auto', style={
            'display':'flex',
            'position':'relative',
            'background': '#045EAD'
        })
        container.append(self.barratitulo)

        self.lblTitle = gui.Label('Algoritmos de Ordenamiento', width='100%', height='30px', style={
            'margin-top': '30px',
            'font-size': '30px',
            'color': '#FFFFFF',
            'text-align': 'center',
            'font-weight': 'bold'
        })
        self.barratitulo.append(self.lblTitle)

        #Barra Menu
        self.barramenu = gui.Container(width = '100%', height = '50px', margin = 'auto auto', style={
            'display':'block',
            'position':'relative',
            'background': '#3C86E6',
            'text-align': 'center'
        })
        container.append(self.barramenu)

        self.btnhome = gui.Button('Home', width=200, height=30, style={
            'margin': '10px',
            'margin-top': '11px',
            'align-item': 'left'
        })
        self.barramenu.append(self.btnhome)
        self.btnhome.set_enabled(False)

        self.btnselect = gui.Button('Selección', width=200, height=30, style={
            'margin': '10px',
            'margin-top': '11px'
        })
        self.btnselect.onclick.do(self.Select_page)
        self.barramenu.append(self.btnselect)

        self.btninsert = gui.Button('Inserción', width = 200, height = 30, style={
            'margin': '10px',
            'margin-top': '11px'
        })
        self.btninsert.onclick.do(self.Insert_page)
        self.barramenu.append(self.btninsert)

        self.btnBubble = gui.Button('Burbuja', width = 200, height = 30, style={
            'margin': '10px',
            'margin-top': '11px'
        })
        self.btnBubble.onclick.do(self.Bubble_page)
        self.barramenu.append(self.btnBubble)

        self.btnQuicksort = gui.Button('Quicksort', width = 200, height = 30, style={
            'margin': '10px',
            'margin-top': '11px'
        })
        self.btnQuicksort.onclick.do(self.Quicksort_page)
        self.barramenu.append(self.btnQuicksort)

        self.btnHeapsort = gui.Button('Heapsort', width = 200, height = 30, style={
            'margin': '10px',
            'margin-top': '11px'
        })
        self.btnHeapsort.onclick.do(self.Heapsort_page)
        self.barramenu.append(self.btnHeapsort) 

        self.btnBucket_Sort = gui.Button('Bucket Sort', width = 200, height = 30, style={
            'margin': '10px',
            'margin-top': '11px'
        })
        self.btnBucket_Sort.onclick.do(self.Bucket_Sort_page)
        self.barramenu.append(self.btnBucket_Sort)

        #Zona de trabajo
        self.zona1 = gui.Container(width = '30%', height = '84%', margin = 'auto auto', style={
            'display':'flex',
            'position':'relative',
            'background': '#FFFFFF',
            'float': 'left',
            'overflow':'hidden',
            'align-items':'center', 
            'justify-content':'center'
        })
        container.append(self.zona1)

        img = gui.Image(width='218px', height='220px', margin='15px', style={
            'max-width':'100%', 
            'max-height':'100%',
            'margin-top': '-13px'
        })
        img.attributes['src'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/640px-Python-logo-notext.svg.png' 

        self.zona1.append(img)

        self.zona2 = gui.Container(width = '40%', height = '84%', margin = 'auto auto', style={
            'display':'block',
            'position':'relative',
            'background': '#FFFFFF',
            'float': 'left'
        })
        container.append(self.zona2)

        self.titlezone1 = gui.Label('Python', width='100%', height='30px', style={
            'font-size' : '3vh',
            'text-align': 'center',
            'margin-top': '41%',
            'font-weight': 'bold',
            'font-style': 'italic',
            'color': '#ffdc51'
        })
        self.zona2.append(self.titlezone1)

        self.titlezone2 = gui.Label('Algoritmos de ordenamiento', width='100%', height='30px', style={
            'font-size' : '3vh',
            'text-align': 'center',
            'margin-top': '15px',
            'font-weight': 'bold',
            'font-style': 'italic',
            'color': '#3c79a9'
        })
        self.zona2.append(self.titlezone2)

        self.zona3 = gui.Container(width = '30%', height = '84%', margin = 'auto auto', style={
            'display':'flex',
            'position':'relative',
            'background': '#FFFFFF',
            'float': 'left',
            'overflow':'hidden',
            'align-items':'center', 
            'justify-content':'center'
        })
        container.append(self.zona3)

        img2 = gui.Image(width='218px', height='220px', margin='15px', style={
            'max-width':'100%', 
            'max-height':'100%',
            'margin-top': '-13px'
        })
        img2.attributes['src'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/640px-Python-logo-notext.svg.png'

        self.zona3.append(img2)

        return container
    
    #Eventos Memu
    def Select_page(self, widget):
        subprocess.Popen(["python", "Seleccion.py"])

    def Insert_page(self, widget):
        subprocess.Popen(["python", "Insercion.py"])
    
    def Bubble_page(self, widget):
        subprocess.Popen(["python", "Burbuja.py"])

    def Quicksort_page(self, widget):
        subprocess.Popen(["python", "Quicksort.py"])
    
    def Heapsort_page(self, widget):
        subprocess.Popen(["python", "Heapsort.py"])
    
    def Bucket_Sort_page(self, widget):
        subprocess.Popen(["python", "Bucketsort.py"])

if __name__ == "__main__":
   start(Algoritmos)

