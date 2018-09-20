import scrapy
from scrapy.spiders import CSVFeedSpider
from scrapy.item import Item, Field

class CalidadAire(scrapy.Item):
    Fecha_Hora = scrapy.Field()
    codigoSerial = scrapy.Field()
    pm25 = scrapy.Field()
    calidad_pm25 = scrapy.Field()
    pm10 = scrapy.Field()
    calidad_pm10 = scrapy.Field()
    no = scrapy.Field()
    calidad_no = scrapy.Field()
    no2 = scrapy.Field()
    calidad_no2 = scrapy.Field()
    nox = scrapy.Field()
    calidad_nox = scrapy.Field()
    ozono = scrapy.Field()
    calidad_ozono = scrapy.Field()
    co = scrapy.Field()
    calidad_co = scrapy.Field()
    so2 = scrapy.Field()
    calidad_so2 = scrapy.Field()


class SiataSpider(CSVFeedSpider):
    name = 'siataSpider'
    allowed_domain = 'siata.gov.co'
    start_urls = ['https://siata.gov.co/descarga_siata/application/assets/assets-siata/downloads/ZAMAXOnFo1vXAW9Bwam8ug/estacion_data_calidadaire_3_20180401_20180430.csv']
    headers = ['Fecha_Hora','codigoSerial','pm25','calidad_pm25','pm10','calidad_pm10','pm1','calidad_pm1','no','calidad_no','no2','calidad_no2','nox','calidad_nox','ozono','calidad_ozono','co','calidad_co','so2','calidad_so2','pst','calidad_pst','dviento_ssr','calidad_dviento_ssr','haire10_ssr','calidad_haire10_ssr','p_ssr','calidad_p_ssr','pliquida_ssr','calidad_pliquida_ssr','rglobal_ssr','calidad_rglobal_ssr','taire10_ssr','calidad_taire10_ssr','vviento_ssr','calidad_vviento_ssr']
    #delimiter = ","
    #quotechar = "'"


    def parse_row(self, response, row):
        self.logger.info('Hi, this is a row %r' % row)

        item = CalidadAire()
        item['Fecha_Hora'] = row['Fecha_Hora']
        item['codigoSerial'] = row['codigoSerial']
        item['pm25'] = row['pm25']
        item['calidad_pm25'] = row['calidad_pm25']
        item['pm10'] = row['pm10']
        item['calidad_pm10'] = row['calidad_pm10']
        item['no'] = row['no']
        item['calidad_no'] = row['no']
        item['no2'] = row['no2']
        item['calidad_no2'] = row['calidad_no2']
        item['nox'] = row['nox']
        item['calidad_nox'] = row['nox']
        item['ozono'] = row['ozono']
        item['calidad_ozono'] = row['calidad_ozono']
        item['co'] = row['co']
        item['calidad_co'] = row['calidad_co']
        item['so2'] = row['so2']
        item['calidad_so2'] = row['calidad_so2']
        yield item
