from bs4 import BeautifulSoup
from cloudscraper import create_scraper
import json

scraper = create_scraper()

# We need to provide an User-Agent, error 403 instead
headers = { "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0"}

# URL for WhatsApp variants
base_url = "https://www.apkmirror.com/"
variants_url = f"{base_url}apk/whatsapp-inc/whatsapp/#variants"

def get_WhatsApp_metadata():
    
    try:
        content = scraper.get(variants_url, headers=headers)
        print(f"Status : {content.status_code}")
    except Exception as e:
        print(f"ERROR: {str(e)}")
    
    soup = BeautifulSoup(content.text, "html.parser")
    
    variants = get_WhatsApp_variants(soup)
    whatsnew = get_WhatsApp_whatsnew(soup)
    
    return {
        "Variants" : variants,
        "Whats New" : whatsnew
    }

def get_WhatsApp_whatsnew(soup : BeautifulSoup):
    
    html_features = soup.find("div", {"class" : "notes wrapText"}).find_all("p")
    
    whatsnew = []
    
    for feature in html_features:
        
        feature = feature.text.strip().split("\n")
        for item in feature:
            
            whatsnew.append(item)
        
    return whatsnew

def get_WhatsApp_variants(soup : BeautifulSoup):
    
    html_variants = soup.find_all("div", {"class" : "table-row headerFont"})
    
    scrapped_variants = []
    # get_variant_whatsNew(html_variants[1])
    
    # The first item is just the header of the variants
    for i in range(1, len(html_variants)):
        
        data = html_variants[i].find_all("div", {"class" : "table-cell rowheight addseparator expand pad dowrap"})
        
        version_info = data[0].find_all('span')
        version = version_info[0].text.strip()
        date = version_info[1].text.strip()
        
        scrapped_variants.append({
            "Version" : str(version) + " " + str(date),
            "arquitectura: " : data[1].text.strip(),
            "version minima de Android: " : data[2].text.strip(),
            "screen_dpi: " : data[3].text.strip()
        })
        
    return scrapped_variants

variants = get_WhatsApp_metadata()
print(variants['Whats New'])
print(variants)