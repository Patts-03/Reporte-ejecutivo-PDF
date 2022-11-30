import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re


if __name__ == '__main__':
    
    # Especificamos un tema común para todas las gráficas
    
    sns.set_theme(style='darkgrid', palette = "crest",  font='sans-serif', font_scale= 0.95, color_codes=True, rc=None)
    
    # Crear la imagen de la predicción ingredientes
    
    df_rec = pd.read_csv('recomendacion_ingredientes.csv',encoding='latin')
    df_rec_sort = df_rec.sort_values('Unidades a comprar',ascending=False)
    fig = plt.figure(figsize=(10, 10))
    
    plt.rcParams.update({'font.size': 10})
    fig = sns.barplot(data=df_rec_sort, x="Unidades a comprar", y="Ingredientes", palette = 'crest')
    
    
    plt.title('Recomendación semanal de ingredientes', fontsize=20)
    plt.ylabel('Ingredientes', fontsize=15)
    plt.xlabel('Cantidades', fontsize=15)
    plt.tight_layout()
    plt.savefig('recom_ingredientes.png')
    
    # Crear el gráfico de modas anuales por pizza por semana
    
    plt.rcParams.update({'font.size': 12})
    df_semanas = pd.read_csv('analisis_pedidos_semanales.csv',encoding='latin')
    df_tipos = pd.read_csv('pizza_types.csv',encoding='latin')
    df_modas = df_semanas.sort_values('Moda_anual',ascending=False)
    fig2 = plt.figure(figsize=(10, 10))
      
    names = {}
    for index in range(len(df_tipos['pizza_type_id'])):
        id = df_tipos['pizza_type_id'][index]
        name = df_tipos['name'][index]
        name = re.sub('The ','', name)
        name = re.sub(' Pizza','', name)
        names[id] = name
    
    for index in range(len(df_modas['Tipo_pizza'])):
        id = df_modas['Tipo_pizza'][index]
        df_modas['Tipo_pizza'][index] = names[id]
        
 
    fig2 = sns.barplot(data=df_modas, y="Tipo_pizza", x="Moda_anual" , palette = 'crest')
    
    fig2.bar_label(fig2.containers[0],padding = 5)
    plt.title('Moda semanal en un año por pizzas', fontsize=20)
    plt.ylabel('Pizzas', fontsize=15)
    plt.xlabel('Moda de pedidos', fontsize=15)
    plt.tight_layout()
    plt.savefig('modas.png')
    
    # Creo el gráfico del top 5 pizzas según el número total de pedidos anual de cada pizza
    '''
    df_modas será el dataframe que utilizaremos ya que 
    tiene la info de pedidos anuales por pizza y los nombres acualizados
    '''
    
    df_anual = df_modas.sort_values('Pedidos_anuales',ascending=False)
    df_top = df_anual.iloc[0:5]
    
    fig3 = plt.figure(figsize=(10, 10))
    fig3 = sns.barplot(data=df_top, x ="Tipo_pizza", y ="Pedidos_anuales")
    fig3.bar_label(fig3.containers[0],padding = 5)
    plt.title('Top 5 pizzas más pedidas en el año', fontsize=20)
    plt.xlabel('Pizzas', fontsize=15)
    plt.ylabel('Pedidos anuales', fontsize=15)
    plt.tight_layout()
    plt.savefig('top5_anuales.png')
    
    
    # Creo el gráfico de las 5 pizzas menos vendidas
    
    df_low = df_anual.iloc[-6:-1]
    
    fig5 = plt.figure(figsize=(10, 10))
    fig5 = sns.barplot(data=df_low, x ="Tipo_pizza", y ="Pedidos_anuales")
    
    fig5.bar_label(fig5.containers[0],padding = 5)
    
    plt.title('Top 5 pizzas menos pedidas en el año', fontsize=20)
    plt.xlabel('Pizzas', fontsize=15)
    plt.ylabel('Pedidos anuales', fontsize=15)
    plt.tight_layout()
    plt.savefig('low5_anuales.png')
    
    
    
    
    
    
    