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
    product_containers = soup.find_all('div', class_='s-result-item')  # Menggunakan kelas 's-result-item'
    if not product_containers:
        raise Exception("Elemen produk tidak ditemukan.")
    
    products = []
    for product in product_containers:
        # Mencari judul produk
        title_tag = product.find('span', class_='a-text-normal')
        if not title_tag:
            title_tag = product.find('h2', class_='a-size-mini')
        if not title_tag:
            title_tag = product.find('a', class_='a-link-normal')  # Coba tag <a> dengan class tertentu
        if title_tag:
            product_title = title_tag.get_text(strip=True)
        else:
            product_title = None
        
        # Jika judul kosong, lewati produk ini
        if not product_title:
            continue
        
        # Mengambil URL gambar
        img_tag = product.find('img')
        if img_tag and 'src' in img_tag.attrs:
            img_url = img_tag['src']
        else:
            img_url = None
        
        # Mengambil link produk
        link_tag = product.find('a', class_='a-link-normal')
        if link_tag and 'href' in link_tag.attrs:
            product_link = 'https://www.amazon.com' + link_tag['href'] if link_tag['href'].startswith('/') else link_tag['href']
        else:
            product_link = None
        
        # Mengambil harga produk
        price_tag = product.find('span', class_='a-offscreen')
        if price_tag:
            product_price = price_tag.get_text(strip=True)
        else:
            product_price = None
        
        # Simpan data produk dalam dictionary
        product_data = {
            "title": product_title,
            "image_url": img_url,
            "product_link": product_link,
            "price": product_price
        }
        products.append(product_data)

    # Menyaring produk yang memiliki judul kosong dan menghitung total produk
    products_filtered = [product for product in products if product['title']]
    total_items = len(products_filtered)

    return {"success": True, "total_items": total_items, "data": products_filtered}

# Uji dengan URL yang Anda berikan
#url = "https://www.amazon.com/s?k=best+2024+laptop+deals&crid=CG1KHU2C4WB2&sprefix=best+2024+laptop%2Caps%2C945&ref=nb_sb_ss_ts-doa-p_1_16"
#result = get_amazon_products(url)
#print(result)
