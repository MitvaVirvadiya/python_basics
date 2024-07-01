import requests

def get_books():
    products = []
    url = "http://localhost:8080/api/v1/public/randomproducts?page=1&limit=10&inc=category%2Cprice%2Cthumbnail%2Cimages%2Ctitle%2Cid"
    response = requests.get(url)
    data = response.json()
    
    if data["statusCode"] and "data" in data:
        product_data = data["data"]["data"]
        for product in product_data:
            prod_name = product["title"]
            prod_price = product["price"]
            products.append({'name': prod_name, 'price': prod_price})
        return products
    else:
        raise Exception("Failed to fetch Books data")

def main():
    try:
        books = get_books()
        for book in books:
            print(f"Name: {book['name']} \nprice: {book['price']}\n")
            print('-'* 30)
    except Exception as e:
        print(e)
    
if __name__ == "__main__":
    main()
    
