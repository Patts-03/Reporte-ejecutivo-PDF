from fpdf import FPDF
import matplotlib.pyplot as plt

def escribir_tit_doc(pdf,titulo, image = None):
    
    pdf.set_font('Arial', 'B', 20)
    if image:
        insert_image(pdf,image,[40,30],[160,2])
        
    pdf.cell(0, 6, f'{titulo}' , 0 , 1, 'L', 0)
    pdf.ln(1)

    return

def escribir_tit_seccion(pdf,titulo):
    
    pdf.set_font('Arial', 'B', 12)
    pdf.ln(4)
    pdf.cell(0, 6, f'{titulo}' , 'B', 1, 'L', 0)
    
    return

def escribir_par(pdf,texto):
    
    pdf.ln(4)
    pdf.set_font('Arial', '', 11)
    pdf.multi_cell(0, 5, texto)
    
    return

def insert_image(pdf,im_name, tamaño, pos = None):
    
    if pos:
        pdf.image(im_name,x = pos[0],y = pos[1], w = tamaño[0], h = tamaño[1])
    else:
        pdf.image(im_name, w = tamaño[0], h = tamaño[1])
    pdf.ln(4)
    
    return

def insert_espacio(pdf,lon):
    
    pdf.ln(lon)
    
    return

def obtener_txt(name):
    
    file = open(name, 'r')
    texto = file.read()
    file.close()
    
    return texto

if __name__ == '__main__':
    
    pdf = FPDF()
    pdf.set_author = 'Patricia Renart'
    pdf.set_title = 'Reporte ejecutivo Maven Pizzas'
    pdf.add_page()
    
    escribir_tit_doc(pdf,'Reporte ejecutivo - Maven Pizzas','logo_2.png')
    insert_espacio(pdf, 4)
    
    ### Primera página ###
    
    # Escribimos la introducción
    intro = obtener_txt('intro.txt')
    escribir_tit_seccion(pdf,'Introducción')
    escribir_par(pdf,intro)
    
    # Mostramos la recomendación de ingredientes
    reco = obtener_txt('recomendacion.txt')
    escribir_tit_seccion(pdf,'Análisis de ingredientes - Cantidad semanal estimada')
    escribir_par(pdf,reco)
    insert_espacio(pdf,4)
    insert_image(pdf,'recom_ingredientes.png',[105,120],[52.5,pdf.get_y()])
    
    ### Segunda página ###
    
    pdf.add_page()
    escribir_tit_doc(pdf,'Reporte ejecutivo - Maven Pizzas','logo_2.png')
    insert_espacio(pdf, 4)
    
    # Mostramos las Top 5 pizzas del año
    top5 = obtener_txt('top5.txt')
    low5 = obtener_txt('low5.txt')
    escribir_tit_seccion(pdf,'Análisis de pizzas - Ratings')
    escribir_par(pdf,top5)
    insert_espacio(pdf,4)
    insert_image(pdf,'top5_anuales.png',[120,105],[45,pdf.get_y()])
    
    insert_espacio(pdf,100)
    escribir_par(pdf,low5)
    insert_espacio(pdf,4)
    insert_image(pdf,'low5_anuales.png',[120,105],[45,pdf.get_y()])
    
    
    ### Tercera página ###
    pdf.add_page()
    escribir_tit_doc(pdf,'Reporte ejecutivo - Maven Pizzas','logo_2.png')
    insert_espacio(pdf, 4)
    
    # Insertamos el estudio de las modas
    
    modas = obtener_txt('modas.txt')
    escribir_tit_seccion(pdf,'Análisis de pizzas - Modas')
    escribir_par(pdf,modas)
    insert_espacio(pdf,4)
    insert_image(pdf,'modas.png',[105,120],[52.5,pdf.get_y()])
    
    pdf.output('reporte_MPizzas.pdf', 'F')
