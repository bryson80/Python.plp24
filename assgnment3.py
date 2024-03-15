def calculate_discount(price, discount_percentage):
    original_price = input("Enter the original price of the item")
    discount_percentage = input("Enter the discount percentage")
    if discount_percentage >= 20:
        discount_amount = price * (discount_percentage / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    if final_price != original_price:
        print(f"The final price after applying a discount is")
    else:
        print("No discount applied. The original price remains")