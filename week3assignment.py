# Create function called calculate_discount
def calculate_discount(price, discount_percent):
    if discount_percent > 20:
        discount_amount = (discount_percent/100)* price
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
 #Get user input, print final price after discount,if no discount print original price
    price =float(input("Enter original price:"))
    discount_percent =float(input("Enter discount percentage:"))

    final_price = calculate_discount(price, discount_percent)

    print("Final price:", final_price)
    
