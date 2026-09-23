import requests
import urllib3

# SSL sertifika uyarılarını kapatıyoruz
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://erp.leanbilisim.com:86/Cari"

# Kötü niyetli başka bir web sitesinden istek atıyormuş gibi Origin veriyoruz
headers = {
    "Origin": "https://tehlikeli-site.com",
    "User-Agent": "Mozilla/5.0"
}

try:
    response = requests.get(url, headers=headers, verify=False, timeout=5)

    # Sunucunun döndürdüğü CORS başlıklarını alıyoruz
    allow_origin = response.headers.get("Access-Control-Allow-Origin", "Yok")
    allow_credentials = response.headers.get("Access-Control-Allow-Credentials", "Yok")

    print(f"[*] Test Edilen URL: {url}")
    print(f"-> Durum Kodu: {response.status_code}")
    print(f"-> Access-Control-Allow-Origin: {allow_origin}")
    print(f"-> Access-Control-Allow-Credentials: {allow_credentials}")

    # Değerlendirme
    if allow_origin == "*" or allow_origin == "https://tehlikeli-site.com":
        print("\n[!] DİKKAT: Gevşek CORS yapılandırması (Misconfiguration) tespit edildi!")
        if allow_credentials == "true":
            print("[!] KRİTİK: Hem dış kaynaklara izin veriliyor hem de kimlik bilgileri (credentials) kabul ediliyor!")
    else:
        print("\n[-] Güvenli: Hedef URL dış kaynaklı origin isteklerine izin vermiyor veya kısıtlı.")

except Exception as e:
    print(f"[!] Hata oluştu: {e}")