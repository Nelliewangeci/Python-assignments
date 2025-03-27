# Create function called calculate_discount
def calculate_discount(price, discount_percent) :
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price  
    
 #Get user input, print final price after discount,if no discount print original price
def get_discounted_price():
    original_price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(original_price, discount_percent)
    
    if discount_percent < 20:
        print(f"No discount applied. The original price is: {original_price}")
    else:
        print(f"The final price after applying the discount is: {final_price}")
              
get_discounted_price()
 

