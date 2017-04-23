"""
module solely made for testing purposes
"""

from bs4 import BeautifulSoup
import requests
import calendar

URL = 'http://www.guatecompras.gt/Proveedores/ConsultaProveeAdj.aspx'
BASE_URL_PROVEEDORES = "http://www.guatecompras.gt/Proveedores"
BASE_URL_COMPRADORES = "http://www.guatecompras.gt/compradores"
BASE_URL_ADJUDICACIONES = "http://www.guatecompras.gt/Concursos/consultaDetalleCon.aspx?"
HEADERS = requests.utils.default_headers()
HEADERS.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0'})
SESSION = requests.Session()
my_c = calendar.Calendar()
mc_ew = my_c.itermonthdates(2016,1)

LA_URL = 'http://guatecompras.gt/proveedores/consultaadvprovee.aspx'
def alternativa_dias():
    """
    este metodo obtiene las adjudicaciones hechas en cada dia de cada mes del year especificado
    """
    req = requests.Request('GET', LA_URL, headers=HEADERS)
    prepped = SESSION.prepare_request(req)
    response = SESSION.send(prepped)
    print response.status_code
    contenido = response.content
    mydf = open('pag1.html', 'w')
    mydf.writelines(response.content)
    mydf.close()
    soup = BeautifulSoup(contenido, 'lxml')
    event_tgt = soup.find('input', attrs={'id': '__EVENTTARGET'})
    event_arg = soup.find('input', attrs={'id': '__EVENTARGUMENT'})
    event_arg = soup.find('input', attrs={'id': '__LASTFOCUS'})
    viewstate = soup.find('input', attrs={'id': '__VIEWSTATE'})
    viewstate_gen = soup.find('input', attrs={'id': '__VIEWSTATEGENERATOR'})
    event_val = soup.find('input', attrs={'id': '__EVENTVALIDATION'})
    #MasterGC%24ContentBlockHolder%24ScriptManager1
    #MasterGC$ContentBlockHolder$ScriptManager1|MasterGC$ContentBlockHolder$rdbOpciones$4
    #eventTarget
    #MasterGC$ContentBlockHolder$rdbOpciones$4
#MasterGC$ContentBlockHolder$ScriptManager1|MasterGC$ContentBlockHolder$rdbOpciones$4
    data = {'MasterGC$ContentBlockHolder$ScriptManager1': 'MasterGC$ContentBlockHolder$ScriptManager1|MasterGC$ContentBlockHolder$rdbOpciones$4',
            'MasterGC$ContentBlockHolder$rdbOpciones': '5',
            '__EVENTTARGET': 'MasterGC$ContentBlockHolder$rdbOpciones$4',
            '__EVENTARGUMENT':'',
            '__LASTFOCUS': '',
            '__VIEWSTATE': viewstate,
            '__VIEWSTATEGENERATOR': viewstate_gen,
            '__EVENTVALIDATION': event_val,
            '__ASYNCPOST': 'true'}


    req = requests.Request('POST', LA_URL, headers=HEADERS, data=data)
    prepped = SESSION.prepare_request(req)
    response = SESSION.send(prepped)
    print response.content
    mydf = open('pag2.html', 'w')
    mydf.writelines(response.content)
    mydf.close()
    #print viewstate_gen.get('value')
    year = 2016
    

alternativa_dias()
def getyear():
    """asdfr
    """
    year = 2016
    year_page = "{}{}{}".format(BASE_URL_PROVEEDORES, '/consultaProveeAdjLst.aspx?lper=', str(year))
    req = requests.Request('GET', year_page, headers=HEADERS)
    prepped = SESSION.prepare_request(req)
    response = SESSION.send(prepped)
    mls = response.content
    soup = BeautifulSoup(mls, 'lxml')
    tabla = soup.find('table', attrs={'id': 'MasterGC_ContentBlockHolder_dgResultado'})
    print soup

#getyear()

def test2():
    req = requests.Request('GET', 'http://guatecompras.gt/proveedores/consultaadvprovee.aspx', headers=HEADERS)
    prepped = SESSION.prepare_request(req)
    response = SESSION.send(prepped)

    f = open("obtener-adjudicados-year.txt")
    req_body = f.read()
    f.close()
    req_body = req_body.format(2016, 2016)
    req = requests.Request('POST', 'http://guatecompras.gt/proveedores/consultaadvprovee.aspx', headers=HEADERS)
    prepped = SESSION.prepare_request(req)
    prepped.body = req_body
    response = SESSION.send(prepped)
    mkl = response.content
    soup = BeautifulSoup(mkl, "lxml")
    print soup.prettify()


def voyhacer():
    """sdeqwe
    """

    response = SESSION.get(URL, headers=HEADERS)
    ml = response.content()
    soup = BeautifulSoup(ml, "lxml")
    tabla = soup.find('table', attrs={'class': 'Tabla1'})
    print tabla[1]

