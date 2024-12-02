import requests
from bs4 import BeautifulSoup
import time
import random
from fake_useragent import UserAgent

def get_amazon_products(url: str, retries: int = 3, delay: int = 5):
    ua = UserAgent()
    
    headers = {
        'User-Agent': ua.random,  # Randomize User-Agent to avoid detection
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
        'TE': 'Trailers',
        'Referer': 'https://www.amazon.com/',  # Set a Referer header
    }

    # Retry mechanism in case of 503 error
    for attempt in range(retries):
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            break  # Exit loop if request is successful
        elif response.status_code == 503 and attempt < retries - 1:
            print(f"Server returned 503, retrying... ({attempt + 1}/{retries})")
            time.sleep(random.randint(5, 10))  # Random delay between retries
        else:
            raise Exception(f"Halaman gagal dimuat, status code: {response.status_code}")
    
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting product details
    product_containers = soup.find_all('div', class_='s-result-item')
    if not product_containers:
        raise Exception("Elemen produk tidak ditemukan.")
    
    products = []
    for product in product_containers:
        title_tag = product.find('span', class_='a-text-normal')
        if not title_tag:
            title_tag = product.find('h2', class_='a-size-mini')
        if not title_tag:
            title_tag = product.find('a', class_='a-link-normal')
        if title_tag:
            product_title = title_tag.get_text(strip=True)
        else:
            product_title = None
        
        if not product_title:
            continue
        
        img_tag = product.find('img')
        img_url = img_tag['src'] if img_tag and 'src' in img_tag.attrs else None
        
        link_tag = product.find('a', class_='a-link-normal')
        product_link = 'https://www.amazon.com' + link_tag['href'] if link_tag and 'href' in link_tag.attrs else None
        
        # Extracting price from a-price a-text-price
        price_tag = product.find('span', class_='a-price a-text-price')
        if price_tag:
            price_offscreen_tag = price_tag.find('span', class_='a-offscreen')
            product_price = price_offscreen_tag.get_text(strip=True) if price_offscreen_tag else None
        else:
            product_price = None
        
        # Extract additional price information
        additional_price_tag = product.find('span', class_='a-offscreen')
        if additional_price_tag:
            additional_price = additional_price_tag.get_text(strip=True)
        else:
            additional_price = None
        
        # Extracting coupon text (if available)
        coupon_tag = product.find('span', class_='s-coupon-clipped aok-hidden')
        coupon_text_tag = coupon_tag.find('span', class_='a-color-base') if coupon_tag else None
        coupon_text = coupon_text_tag.get_text(strip=True) if coupon_text_tag else None
        
        product_data = {
            "title": product_title,
            "image_url": img_url,
            "product_link": product_link,
            "price": product_price,  # Main price from a-price a-text-price
            "x_price": additional_price,  # Additional price from a-offscreen
            "coupon_text": coupon_text  # Include coupon text if found
        }

        # Filter out products where the price is null
        if not product_data["price"]:
            continue
        
        products.append(product_data)

    total_items = len(products)

    return {"success": True, "total_items": total_items, "data": products}

