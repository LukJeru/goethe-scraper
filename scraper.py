import requests
from bs4 import BeautifulSoup
import csv

#Portugal, Spanien,Frankreich, Belgien, Niederlande, Irland, UK, Dänemark, Norwegen, Italien, Schweden, Kroatien, Serbien, Polen, Griechenland, Ungarn, Slowakei, Finnland, Litauen, Letland, Estland

Warschau = ["Warschau","https://www.goethe.de/ins/pl/de/sta/war/ueb/kar.html"]
Krakau = ["Krakau", "https://www.goethe.de/ins/pl/de/sta/kra/ueb/kar.html"]
Slowakei = ["Slowakei","https://www.goethe.de/ins/sk/de/ueb/kar.html"]
SanFran= ["San Francisco","https://www.goethe.de/ins/us/de/sta/sfr/ueb/kar.html"]
Boston = ["Boston", "https://www.goethe.de/ins/us/de/sta/bos/ueb/karriere-und-praktika.html" ]
LosAngeles = ["Los Angeles", "https://www.goethe.de/ins/us/de/sta/los/ueb/kar.html"]
Chicago = ["Chicago", "https://www.goethe.de/ins/us/de/sta/chi/ueb/kar.html"]
NewYork = ["New York", "https://www.goethe.de/ins/us/de/sta/ney/uun/kar.html"]
Washington = ["Washington", "https://www.goethe.de/ins/us/de/sta/wsh/ueb/kar.html"]
Montreal = ["Montreal","https://www.goethe.de/ins/ca/de/sta/mon/ueb/kar.html"]
Toronto = ["Toronto", "https://www.goethe.de/ins/ca/de/sta/tor/ueb/kar.html"]
Ottawa = ["Ottawa", "https://www.goethe.de/ins/ca/de/sta/ott/ueb/kar.html"]
Mexiko = ["Mexiko-Stadt","https://www.goethe.de/ins/mx/de/ueb/kar.html"]
Chile = ["Santiago de Chile", "https://www.goethe.de/ins/cl/de/ueb/kar.html"]
Argentinien = ["Argentinien", "https://www.goethe.de/ins/ar/de/ueb/kar.html"]
Ghana = ["Ghana", "https://www.goethe.de/ins/gh/de/ueb/kar.html"]
Senegal = ["Senegal", "https://www.goethe.de/ins/sn/de/ueb/kar.html"]
Tansania = ["Tansania", "https://www.goethe.de/ins/ts/de/ueb/kar.html"]
Namibia = ["Namibia", "https://www.goethe.de/ins/na/de/ueb/kar.html"]
Oman = ["Oman", "https://www.goethe.de/ins/ae/de/ueb/kar.html"]
Korea = ["Korea", "https://www.goethe.de/ins/kr/de/uun/kar.html"]
Kyoto = ["Kyoto", "https://www.goethe.de/ins/jp/de/sta/osa/ueb/kar.html"]
Tokyo = ["Tokyo", "https://www.goethe.de/ins/jp/de/sta/tok/ueb/kar.html"]
HoChiMinh = ["Ho-Chi-Minh-Stadt", "https://www.goethe.de/ins/vn/de/sta/hcm/ueb/kar.html"]
Hanoi = ["Hanoi", "https://www.goethe.de/ins/vn/de/sta/han/ueb/kar.html"]
Australien = ["Sydney", "https://www.goethe.de/ins/au/de/ueb/kar.html"]
Neuseeland = ["Auckland", "https://www.goethe.de/ins/nz/de/ueb/kar.html"]
Portugal = ["Portugal", "https://www.goethe.de/ins/pt/de/ueb/kar.html"]
Spanien = ["Spanien", "https://www.goethe.de/ins/es/de/ueb/kar.html"]
Frankreich = ["Frankreich", "https://www.goethe.de/ins/fr/de/ueb/kar.html"]
Irland = ["Irland", "https://www.goethe.de/ins/ie/de/ueb/kar.html"]
Großbritannien = ["Großbritannien", "https://www.goethe.de/ins/gb/de/ueb/kar/ste.html"]
Finnland = ["Finnland", "https://www.goethe.de/ins/fi/de/ueb/kar.html"]
Dänemark = ["Dänemark", "https://www.goethe.de/ins/dk/de/ueb/kar.html"]
Schweden = ["Schweden", "https://www.goethe.de/ins/dk/de/ueb/kar.html"]
Norwegen = ["Norwegen", "https://www.goethe.de/ins/no/de/ueb/kar.html"]
Italien = ["Italien", "https://www.goethe.de/ins/it/de/ueb/kar.html"]
Belgien = ["Belgien", "https://www.goethe.de/ins/be/de/ueb/kar.html"]
Niederlande = ["Niederlande", "https://www.goethe.de/ins/nl/de/ueb/kar.html"]
Tschechien = ["Tschechien", "https://www.goethe.de/ins/cz/de/ueb/kar.html"]
Bolivien = ["Bolivien", "https://www.goethe.de/ins/bo/de/ueb/kar.html"]
Elfenbeinküste = ["Elfenbeinküste", "https://www.goethe.de/ins/ci/de/ueb/kar.html"]
Estland = ["Estland", "https://www.goethe.de/ins/ee/de/ueb/kar.html"]
Griechenland = ["Griechenland", "https://www.goethe.de/ins/gr/de/ueb/kar.html"]
Kenia = ["Kenia", "https://www.goethe.de/ins/ke/de/ueb/kar.html"]
Kroatien = ["Kroatien", "https://www.goethe.de/ins/hr/de/ueb/kar.html"]
Lettland = ["Lettland", "https://www.goethe.de/ins/lv/de/uun/kar.html"]
Litauen = ["Litauen", "https://www.goethe.de/ins/lt/de/ueb/kar.html"]
Peru = ["Peru", "https://www.goethe.de/ins/pe/de/ueb/kar.html"]
Slowenien = ["Slowenine", "https://www.goethe.de/ins/si/de/ueb/kar.html"]
Taipei = ["Taipei", "https://www.goethe.de/ins/tw/de/ueb/kar.html"]
Ungarn = ["Ungarn", "https://www.goethe.de/ins/hu/de/ueb/kar.html"]
Deutschland = ["Deutschland", "https://www.goethe.de/ins/de/de/uun/job.html"]
Bangalore = ["Bangalore", "https://www.goethe.de/ins/in/de/sta/ban/ueb/kar.html"]
Chennai = ["Chennai", "https://www.goethe.de/ins/in/de/sta/che/ueb/kar.html"]
Kolkata = ["Kolkata", "https://www.goethe.de/ins/in/de/sta/kol/ueb/kar.html"]
Mumbai = ["Mumbai", "https://www.goethe.de/ins/in/de/sta/mum/ueb/kar.html"]
NewDelhi = ["New Delhi", "https://www.goethe.de/ins/in/de/sta/new/ueb/karriere.html"]
Pune = ["Pune", "https://www.goethe.de/ins/in/de/sta/pun/ueb/kar.html"]
Rio = ["Rio de Janeiro", "https://www.goethe.de/ins/br/de/sta/rio/ueb/kar.html"]
Salvador = ["Salvador", "https://www.goethe.de/ins/br/de/sta/sal/ueb/kar.html"]
PortoAlegre = ["Porto Alegre", "https://www.goethe.de/ins/br/de/sta/poa/ueb/kar.html"]
SaoPaulo = ["Sao Paulo", "https://www.goethe.de/ins/br/de/sta/sap/ueb/kar.html"]
Curitiba = ["Curitiba", "https://www.goethe.de/ins/br/de/sta/cur/ueb/kar.html"]
Südafrika = ["Südafrika", "https://www.goethe.de/ins/za/de/ueb/kar.html"]
Zypern = ["Zypern", "https://www.goethe.de/ins/cy/de/ueb/kar.html"]
Bosnien = ["Bosnien", "https://www.goethe.de/ins/ba/de/ueb/aus.html"]
Bulgarien = ["Bulgarien", "https://www.goethe.de/ins/bg/de/ueb/kar.html"]
Indonesien = ["Indonesien", "https://www.goethe.de/ins/id/de/ueb/kar.html"]
Israel = ["Israel", "https://www.goethe.de/ins/il/de/ueb/kar.html"]
Kamerun = ["Kamerun", "https://www.goethe.de/ins/cm/de/ueb/kar.html"]
Jordanien = ["Jordanien", "https://www.goethe.de/ins/jo/de/ueb/kar.html"]
Libanon = ["Libanon", "https://www.goethe.de/ins/lb/de/ueb/kar.html"]
Mongolei = ["Mongolei", "https://www.goethe.de/ins/mn/de/ueb/kar.html"]
Myanmar = ["Myanmar", "https://www.goethe.de/ins/mm/de/ueb/kar/stel.htmll"]
Nordmazedonien = ["Nordmazedonien", "https://www.goethe.de/ins/mk/de/ueb/kar.html"]
Rumänien = ["Rumänien", "https://www.goethe.de/ins/ro/de/ueb/kar/aktuelle-stellenangebote.html"]
Thailand = ["Thailand", "https://www.goethe.de/ins/th/de/ueb/kar.html"]
Alexandria = ["Alexandria", "https://www.goethe.de/ins/eg/de/sta/alx/ueb/kar.html"]
Kairo = ["Kairo", "https://www.goethe.de/ins/eg/de/sta/kai/ueb/kar.html"]
Tunesien = ["Tunsien", "https://www.goethe.de/ins/tn/de/ueb/kar.html"]

Länder = [Warschau, Krakau, Slowakei, SanFran, Boston, LosAngeles,
          NewYork, Washington, Montreal, Toronto, Ottawa, Mexiko, Chile,
          Argentinien, Ghana, Senegal, Tansania, Namibia, Oman, Korea, Kyoto,
          Tokyo, HoChiMinh, Hanoi, Australien, Neuseeland, Portugal, Spanien,
          Frankreich, Irland, Großbritannien, Finnland, Dänemark, Schweden,
          Norwegen, Italien, Belgien, Niederlande, Tschechien, Bolivien,
          Elfenbeinküste, Estland, Griechenland, Kenia, Kroatien,
          Lettland, Litauen, Peru, Slowenien, Taipei, Ungarn,
          Deutschland, Bangalore, Chennai, Kolkata, Mumbai, NewDelhi, Pune,
          Rio, Salvador, PortoAlegre, SaoPaulo, Curitiba, Südafrika, Zypern, Bosnien,
          Bulgarien, Indonesien, Israel, Kamerun, Jordanien, Libanon, Mongolei, Myanmar,
          Nordmazedonien, Rumänien, Thailand, Alexandria, Kairo, Tunesien
          ]
header = []
jobs = []
links = []
sum = 0
for Land in Länder:
    page = requests.get(Land[1])
    print(str(Länder.index(Land) )+ "/" + str(len(Länder) -1 ))
    soup = BeautifulSoup(page.content, "html.parser")
    job_elements = soup.find_all("h3") + soup.find_all(class_="w(719px) m-lr-a link-c Mt(40px)") + soup.find_all(class_="containerMRSORS") + soup.find_all("div", class_="dossier-infotext w(719px) m-lr-a Mb(50px)") +soup.find_all(class_="stretched-link") +soup.find_all(class_="link-text ")

    for job_element in job_elements:
        #link_element = job_element.find("a")
        #if link_element:
            if "Vielfalt, Neugierde und Offenheit" not in job_element.text and "Leider" not in job_element.text and "Folgen Sie uns" not in job_element.text and "Zurück zu" not in job_element.text and "Kontakt" not in job_element.text and "Praktikum" not in job_element.text and "Internship" not in job_element.text and "Grünes Diplom" not in job_element.text and "SCHULWÄRTS" not in job_element.text and "Kulturweit" not in job_element.text and "GRÜNES DIPLOM" not in job_element.text and "Grünes Diplom" not in job_element.text and "Lehrkräfte" not in job_element.text and "lehrkräfte" not in job_element.text and "Jugendfreiwilligendienst" not in job_element.text and "weltweit" not in job_element.text and "Initiativbewerbung" not in job_element.text and "Zurück zu" not in job_element.text and "Home" not in job_element.text and "thorsten" not in job_element.text and "Newsletter" not in job_element.text and "Stellenangebote" not in job_element.text:
            #if "Praktikum" not in link_element.text and "Internship" not in link_element.text and "Grünes Diplom" not in link_element.text and "SCHULWÄRTS" not in link_element.text and "Kulturweit" not in link_element.text and "GRÜNES DIPLOM" not in link_element.text and "Grünes Diplom" not in link_element.text and "Lehrkräfte" not in link_element.text and "lehrkräfte" not in link_element.text and "Jugendfreiwilligendienst" not in link_element.text and "weltweit" not in link_element.text and "Initiativbewerbung" not in link_element.text and "Zurück zu" not in link_element.text and "Home" not in link_element.text and "thorsten" not in link_element.text and "Newsletter" not in link_element.text:
                if job_element.text: #job wieder mit link austauschen
                    header.append(Land[0])
                    jobs.append(job_element.text) #job wieder mit link austauschen
                    links.append(Land[1])
                    sum +=1

print("{jobs} Jobs gefunden".format(jobs = sum))



with open('countries.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerow(jobs)
    writer.writerow(links)
