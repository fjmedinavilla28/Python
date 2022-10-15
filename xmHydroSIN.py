# -*- coding: cp1252 -*-
from arcgis.gis import GIS
from arcgis.features import Table
from configManager.Config import Config
from configManager.WDistributionConfig import WDistributionConfig
from datetime import date, timedelta, datetime
import json
from logger import messaging
from logger.LogFile import LogFile
import urllib3
import urllib.parse
#from testing import setPortalParameters, setXMSINParameters

def getXml(url):
    """Obtiene los datos de embalses y rios de las regiones del portal de XM. 

    param string url: url del api del detalle de las regiones de XM
    return los datos obtenidos del api en formato json como un diccionario
    """
    try:
        file = urllib.request.urlopen(url)
        data = file.read()
        file.close()
        dict = json.loads(data.decode('utf-8'))
        return dict
    except Exception as e:
        logFile.write("{} - {} - Error obteniendo los datos de XM".format(dateNow, e))
        return False

def getEmbalses(dataEmbalses):
    """Construye una lista de datos de embalses con la estructura de la base de datos, 
    tambien transforma los datos de Regiones para dejarlos textos completos.

    param dataEmbalses dict: diccionario con los datos de embalses obtenidos del api de XM.
    return los datos de embalses con la estructura de la tabla de la base de datos
    """
    embalseList=[]
    try:
        for emb in dataEmbalses:        
            attrs = {
                "NOMBRE": emb["Nombre"],
                "FECHA": emb["Fecha"],
                "REGION": emb["RegionId"],
                "VOLUMENUTIL": emb["VolumenUtil"],
                "PORCENTAJEVOLUMENTUTIL": emb["PorcentajeVolumenUtil"],
                }
            embalseList.append(attrs)

        for x in embalseList:   
            if x['REGION'] == 'ANTI':
                regAnti = {'REGION': 'ANTIOQUIA'}
                x.update(regAnti)
            elif x['REGION'] == 'CARI':
                regAnti = {'REGION': 'CARIBE'}
                x.update(regAnti)
            elif x['REGION'] == 'CENT':
                regAnti = {'REGION': 'CENTRO'}
                x.update(regAnti)
            elif x['REGION'] == 'ORIE':
                regAnti = {'REGION': 'ORIENTE'}
                x.update(regAnti)
            elif x['REGION'] == 'VALL':
                regAnti = {'REGION': 'VALLE'}
                x.update(regAnti)
        return embalseList

    except Exception as e:
        logFile.write("{} - {} - Error construyendo los datos de embalses".format(dateNow, e))
        return False

def changeDate(list):
    """Cambia el formato de fecha para que coincida con el formato de la base de datos.

    param list list: lista de datos con la estructura general de la tabla de la base de datos
    return los datos recibidos como parametro pero con la fecha en el formato de la base de datos
    """
    try:
        for x in list:
            fecha = x['FECHA']
            year = fecha[0:4]
            month = fecha[5:7]
            day = fecha[8:10]
            newDate = {'FECHA': '{}/{}/{} 12:00:00'.format(month,day,year)}
            x.update(newDate)
        return list

    except Exception as e:
        logFile.write("{} - {} - Error cambiando el formato de fecha".format(dateNow, e))
        return False

def getRios(dataRios):
    """Construye una lista de datos de rios con la estructura de la base de datos,
    tambien transforma los datos de Regiones para dejarlos textos completos.

    param dataRios dict: diccionario con los datos de rios obtenidos del api de XM.
    return los datos de rios con la estructura de la tabla de la base de datos
    """
    riosList=[]
    try:
        for rio in dataRios:        
            attrs = {
                    "FECHA": rio["Fecha"],
                    "NOMBRE": rio["Nombre"],
                    "PORCENTAJEVOLUMENTUTIL": rio["PorcentajeVolumenUtil"],
                    "REGION": rio["RegionId"],
                    "VOLUMENUTIL": rio["VolumenUtil"],
                    "MEDIAHISTORICA": rio["MediaHistorica"],
                    "PSS": rio["PSS"],
                }
            riosList.append(attrs)
        
        for x in riosList:
            if x['REGION'] == 'ANTI':
                regAnti = {'REGION': 'ANTIOQUIA'}
                x.update(regAnti)
            elif x['REGION'] == 'CARI':
                regAnti = {'REGION': 'CARIBE'}
                x.update(regAnti)
            elif x['REGION'] == 'CENT':
                regAnti = {'REGION': 'CENTRO'}
                x.update(regAnti)
            elif x['REGION'] == 'ORIE':
                regAnti = {'REGION': 'ORIENTE'}
                x.update(regAnti)
            elif x['REGION'] == 'VALL':
                regAnti = {'REGION': 'VALLE'}
                x.update(regAnti)

        return riosList

    except Exception as e:
        logFile.write("{} - {} - Error construyendo los datos de rios".format(dateNow, e))
        return False

def addDams(dictDams):
    """Guarda los datos en el servicio de ArcGIS

    param dictDams dict: diccionario con los datos que se van a almacenar en la base de datos por medio del servicio de ArcGIS.
    """
    try:
        fl = Table(damService, gis=gis)
        fl.edit_features(adds=dictDams)
    except Exception as e:
        logFile.write("{} - {} - Error guardando los datos de embalses en el servicio".format(dateNow, e))
        return False

def addRivers(dictRivers):
    """Guarda los datos en el servicio de ArcGIS

    param dictRivers dict: diccionario con los datos que se van a almacenar en la base de datos por medio del servicio de ArcGIS.
    """
    try:
        fl = Table(riverService, gis=gis)
        fl.edit_features(adds=dictRivers)
    except Exception as e:
        logFile.write("{} - {} - Error guardando los datos de rios en el servicio".format(dateNow, e))
        return False
        
def setPortalParameters():
    print("\n-> setPortalParameters")
    try:        
        config = Config()
        portalUrl = config.portal.getUrl()
        portalUser = config.portal.getUsername()
        portalPass = config.portal.getPassword()        

        #print("Parametros GIS OK!, imprimiendo resultados...")
        #print("portalUrl: {}".format(portalUrl))
        #print("portalUser: {}".format(portalUser))
        #print("portalPass: {}".format(portalPass))
        return portalUrl, portalUser, portalPass
    except:
        print("Error al leer parametros generales....")

def setXMSINParameters():
    try:
        WDistConfig = WDistributionConfig()
        print("Parametros XM SIN OK!, imprimiendo resultados...")
        #LOG
        xmLogsPath = WDistConfig.parameters.get("logs_xm_sin_path")
        print("xmLogsPath: {}".format(xmLogsPath))
        #XM
        xmSINEndPoint = WDistConfig.parameters.get("xm_sin_endpoint")
        print("xmEndPoint: {}".format(xmSINEndPoint))
        #SERVICIOS DE PORTAL
        portalXmDamEndPoint = WDistConfig.parameters.get("portal_xm_dam_endpoint")
        portalXmRiverEndPoint = WDistConfig.parameters.get("portal_xm_river_endpoint")
        print("portalXmDamEndOoint: {}".format(portalXmDamEndPoint))
        print("portalXmRiverEndOoint: {}".format(portalXmRiverEndPoint))
        return xmLogsPath, xmSINEndPoint, portalXmDamEndPoint, portalXmRiverEndPoint
    except:
        print("Error al leer parametros de Aportes Hidricos de XM....")        

logFilePath, urlDetalleRegion, damService, riverService = setXMSINParameters()
logFile = LogFile(logFilePath)

yesterday = (date.today() - timedelta(1)).strftime("%Y-%m-%d")
dateNow = datetime.now()
urlDetalleRegion = '{}?fecha={}'.format(urlDetalleRegion, yesterday)

portal, user, password = setPortalParameters()
gis = GIS(portal, user, password, verify_cert=False)

todayStr = date.today().strftime("%Y-%m-%d")

if __name__ == '__main__':
    xmlData = getXml(urlDetalleRegion)

    if xmlData != False:
        # Procesamiento de datos de embalses
        embalses = xmlData['Embalses']
        dataEmbalses = getEmbalses(embalses)
        if dataEmbalses != False:
            dataDam = changeDate(dataEmbalses)
            damDict =[]
            for x in dataDam:
                val = {"attributes" : x}
                damDict.append(val)     
            saveDams = addDams(damDict)
            if saveDams != False:
                logFile.write("{} - Datos de embalses guardados correctamente".format(dateNow))
            else:
                logFile.write("{} - Se ha producido un error guardando los datos de Embalses en el servicio".format(dateNow))
        else:
            logFile.write("{} - Se ha producido un error con los datos de Embalses".format(dateNow))

        # Procesamiento de datos de rios
        rios = xmlData['Rios']
        dataRios = getRios(rios)
        if dataRios != False:
            dataRiver = changeDate(dataRios)
            riverDict =[]
            for x in dataRiver:
                val = {"attributes" : x}
                riverDict.append(val)     
            saveRivers = addRivers(riverDict)
            if saveRivers != False:
                logFile.write("{} - Datos de ríos guardados correctamente".format(dateNow))
            else:
                logFile.write("{} - Se ha producido un error guardando los datos de ríos en el servicio".format(dateNow))
        else:
            logFile.write("{} - Se ha producido un error con los datos de Embalses".format(dateNow))
    else:
        logFile.write("{} - Se ha producido un error obteniendo los datos de DetalleRegion".format(dateNow))
    