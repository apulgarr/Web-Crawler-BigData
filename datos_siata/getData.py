from urllib2 import urlopen
import csv

class Data:

    def __init__(self, url, csv_extentions):
        self.csv_extentions = csv_extentions
        self.url = url


    def get_data(self, url):
        csv_data = urlopen(url).readlines()
        csv_data = csv_data
        csv = [csv.split(',') for csv in csv_data]
        return csv


    def get_item(self):
        data = {}

        for csv_extention in self.csv_extentions:
            data_csv = self.get_data(self.url+csv_extention)

            with open(csv_extention, 'w') as outfile:
                writer = csv.writer(outfile, delimiter=',', quotechar='"')
                for item in data_csv:
                    data['Fecha_Hora'] = item[0]
                    data['codigoSerial'] = item[1]
                    data['pm25'] = item[2]
                    data['calidad_pm25'] = item[3]
                    data['pm10'] = item[4]
                    data['calidad_pm10'] = item[5]
                    data['no'] = item[8]
                    data['calidad_no'] = item[9]
                    data['no2'] = item[10]
                    data['calidad_no2'] = item[11]
                    data['nox'] = item[12]
                    data['calidad_nox'] = item[13]
                    data['ozono'] = item[14]
                    data['calidad_ozono'] = item[15]
                    data['co'] = item[16]
                    data['calidad_co'] = item[17]
                    data['so2'] = item[18]
                    data['calidad_so2'] = item[19]
                    writer.writerow(data.values())





if __name__ == '__main__':
    instance = Data('https://siata.gov.co/descarga_siata//application/assets/assets-siata/downloads/HgMfhJBrrVvecoZ2TbTeJg/estacion_data_calidadaire_82_20180301_20180331.csv', 'estacion_data_calidadaire_82_20180301_20180331.csv')
    print instance.get_item()
