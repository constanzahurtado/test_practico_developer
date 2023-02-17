from django.db import models

class Network(models.Model):
    id_network = models.CharField(max_length= 100, blank=True)
    name_network = models.CharField(max_length= 100, blank=True)
    company_network = models.CharField(max_length= 100, blank=True)
    city_network = models.CharField(max_length= 150, blank=True)
    country_network = models.CharField(max_length= 100, blank=True)
    gbfs_href_network = models.CharField(max_length= 100, blank=True)
    href_network = models.CharField(max_length= 100, blank=True)
    latitude_network = models.IntegerField(null=True)
    longitude_network = models.IntegerField(null=True)
    
    def __str__(self):
        return self.name_network
        
class Station(models.Model):
    network_station = models.ForeignKey(Network, on_delete= models.CASCADE)
    id_station = models.CharField(max_length= 100)
    uid_station = models.CharField(max_length= 10)
    name_station = models.CharField(max_length= 100)
    adress_station = models.CharField(max_length= 100)
    payment_station = models.CharField(max_length= 100)
    payment_terminal_station = models.BooleanField()
    empty_slots_station = models.IntegerField()
    slots_station = models.IntegerField()
    renting_station = models.IntegerField()
    returning_station = models.IntegerField()
    normal_bikes_station = models.IntegerField()
    free_bikes_station = models.IntegerField()
    ebikes_station = models.IntegerField()
    has_ebikes_station = models.BooleanField()
    altitude_station = models.IntegerField()
    latitude_station = models.IntegerField()
    longitude_station = models.IntegerField()
    timestamp_station = models.DateTimeField()
    last_updated_station = models.IntegerField()
    

class TableSEA(models.Model):
    numero = models.CharField(max_length=250)
    nombre = models.CharField(max_length= 250)
    tipo = models.CharField(max_length= 250)
    region = models.CharField(max_length= 250)
    tipologia = models.CharField(max_length= 250)
    titular = models.CharField(max_length= 250)
    inversion = models.CharField(max_length= 200)
    fecha_presentacion = models.CharField(max_length= 250)
    estado = models.CharField(max_length= 250)

    def __str__(self):
        return self.nombre