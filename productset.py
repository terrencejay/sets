def products():
    category_product = set()
    while True:
        user_category = input("Enter 'quit' to stop or Enter the category of this product? ")
        if user_category.lower() == 'quit':
            print(category_product)
            break
        user_product = input(f"Enter the product you would like to add to {user_category}: ")
        print(f"now adding {user_product} to the {user_category}")
        category_product.add((user_category, user_product))
        print(f"Here is your catalog \n{category_product}")
        
products()
        
        