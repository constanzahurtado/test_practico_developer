from django.shortcuts import render
import requests
from . models import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, NoSuchWindowException
import time
import json
import pandas as pd


def index(request):
    return render(request, 'App/index.html')

# Obtención Datos API
def get_data_API():
    response = requests.get('http://api.citybik.es/v2/networks/bikesantiago')
    data = response.json()
    network_values = data["network"]
    
    if not Network.objects.filter(id_network = network_values["id"]).exists():
        obj = Network.objects.create(
            id_network = network_values["id"],
            name_network = network_values["name"],
            company_network = network_values["company"],
            city_network = network_values["location"]["city"],
            country_network = network_values["location"]["country"],
            gbfs_href_network = network_values["gbfs_href"],
            href_network= network_values["href"],
            latitude_network = network_values["location"]["latitude"],
            longitude_network = network_values["location"]["longitude"],
            
            
        )
        obj.save()
    else:
        print('The data already exists')
    
    station = network_values['stations']
    for sta in station: 
        if not Station.objects.filter(id_station = sta["id"]).exists():
            obj2 = Station(
                network_station = obj,
                id_station = sta["id"],    
                uid_station = sta["extra"]["uid"],
                name_station = sta["name"],
                adress_station = sta["extra"]["address"],
                payment_station = sta["extra"]["payment"],
                payment_terminal_station = sta["extra"]["payment-terminal"],
                empty_slots_station = sta["empty_slots"],
                slots_station = sta["extra"]["slots"],
                renting_station = sta["extra"]["renting"],
                returning_station = sta["extra"]["returning"],
                normal_bikes_station = sta["extra"]["normal_bikes"],
                free_bikes_station = sta["free_bikes"],
                ebikes_station = sta["extra"]["ebikes"],
                has_ebikes_station = sta["extra"]["has_ebikes"],
                altitude_station = sta["extra"]["altitude"],
                latitude_station = sta["latitude"],
                longitude_station = sta["longitude"],
                timestamp_station = sta["timestamp"],
                last_updated_station = sta["extra"]["last_updated"],
        )
            obj2.save()
            print('saved')
            
        else:
            print('The data already exists')


def data(request):
    station = Station.objects.all()
    return render(request, 'App/tarea1.html',{'station': station})

    
#Web Scrapping Selenium

def web_scrapping():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    web_page = "https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php"

    driver.get(web_page)
    driver.maximize_window()

    id_list = []
    name_list = []
    type_list = []
    region_list = []
    typology_list = []
    titular_list = []
    investment_list = []
    presentation_date_list = []
    list_state = []

    contador = 1

    while contador <= 200:
        
        ids = driver.find_elements(By.XPATH, '/html/body/div/div/div/div/div/div/table/tbody/tr/td[1]')
        for i in ids:
            id_list.append(i.text)
        
        names = driver.find_elements(By.XPATH, '/html/body/div/div/div/div/div/div/table/tbody/tr/td[2]')
        for name in names:
            name_list.append(name.text)
        
        types = driver.find_elements(By.XPATH, '/html/body/div/div/div/div/div/div/table/tbody/tr/td[3]')
        for type in types:
            type_list.append(type.text)
        
        regions = driver.find_elements(By.XPATH, '/html/body/div/div/div/div/div/div/table/tbody/tr/td[4]')
        for region in regions:
            region_list.append(region.text)
        
        typologys = driver.find_elements(By.XPATH, '/html/body/div/div/div/div/div/div/table/tbody/tr/td[5]')
        for typology in typologys:
            typology_list.append(typology.text)
        
        titular = driver.find_elements(By.XPATH, '/html/body/div/div/div/div/div/div/table/tbody/tr/td[6]')
        for t in titular:
            titular_list.append(t.text)
        
        investments = driver.find_elements(By.XPATH, '/html/body/div/div/div/div/div/div/table/tbody/tr/td[7]')
        for investment in investments:
            investment_list.append(investment.text)
        
        presentation_date = driver.find_elements(By.XPATH, '/html/body/div/div/div/div/div/div/table/tbody/tr/td[8]')
        for dates in presentation_date:
            presentation_date_list.append(dates.text)
        
        states = driver.find_elements(By.XPATH, '/html/body/div/div/div/div/div/div/table/tbody/tr/td[9]')
        for state in states:
            list_state.append(state.text)


        try:
            time.sleep(5)
            select_element = driver.find_element(By.NAME, 'pagina_offset')
            select = Select(select_element)
            time.sleep(10)
            select.select_by_index(contador)
            time.sleep(10)
            contador += 1
        except StaleElementReferenceException:
            pass

    
    df = pd.DataFrame(list(zip(id_list, name_list,type_list,region_list,typology_list,titular_list,investment_list,presentation_date_list,list_state)),
                columns =['Id', 'Name','Type','Region', 'Typology', 'Titular', 'Investment', 'Presentation_Date','state'])

    df = df.to_dict(orient='records')
    with open("mydata.json", "w",  encoding="utf-8") as f:
        json.dump(df, f, ensure_ascii=False)




def get_data_json():
    archivo = open('C:/proyectos/PruebaTecnica/Proyecto/App/mydata.json', encoding="utf8")
    datos_unidades = json.load(archivo)
    for i in datos_unidades:
            obj = TableSEA.objects.create(
                numero  =  i["Id"],
                nombre = i["Name"],
                tipo = i["Type"],
                region = i["Region"],
                tipologia = i["Typology"],
                titular = i["Titular"],
                inversion = i["Investment"],
                fecha_presentacion = i["Presentation_Date"],
                estado = ["state"]     
            )
            obj.save()

