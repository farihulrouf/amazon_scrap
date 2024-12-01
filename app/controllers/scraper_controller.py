import requests
from bs4 import BeautifulSoup

def get_amazon_products(url: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
        'TE': 'Trailers',
    }

    # Lakukan permintaan HTTP ke halaman Amazon
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Halaman gagal dimuat, status code: {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')

    # Mengambil elemen produk
    product_containers = soup.find_all('div', class_='s-product-image-container')
    if not product_containers:
        raise Exception("Elemen produk tidak ditemukan.")
    
    products = []
    for product in product_containers:
        img_tag = product.find('img')
        if img_tag and 'src' in img_tag.attrs:
            img_url = img_tag['src']
        else:
            img_url = None
        
        link_tag = product.find('a', class_='a-link-normal')
        if link_tag and 'href' in link_tag.attrs:
            product_link = 'https://www.amazon.com' + link_tag['href']
        else:
            product_link = None
        
        # Simpan data produk dalam dictionary
        product_data = {
            "image_url": img_url,
            "product_link": product_link
        }
        products.append(product_data)

    return products
