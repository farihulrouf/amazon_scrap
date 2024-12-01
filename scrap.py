import requests
from bs4 import BeautifulSoup

def get_amazon_products(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
        'TE': 'Trailers',
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Halaman gagal dimuat, status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    product_containers = soup.find_all('div', class_='s-product-image-container')
    if not product_containers:
        print("Elemen produk tidak ditemukan.")
        return

    for i, product in enumerate(product_containers, start=1):
        img_tag = product.find('img')
        if img_tag and 'src' in img_tag.attrs:
            img_url = img_tag['src']
            print(f"URL Gambar {i}: {img_url}")
        
        link_tag = product.find('a', class_='a-link-normal')
        if link_tag and 'href' in link_tag.attrs:
            product_link = 'https://www.amazon.com' + link_tag['href']
            print(f"Link Produk {i}: {product_link}")

# URL halaman Amazon yang ingin di-scrape
amazon_url = 'https://www.amazon.com/s?k=laptop'
get_amazon_products(amazon_url)
