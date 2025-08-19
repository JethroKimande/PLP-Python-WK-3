# Function to calculate the final price after applying a discount if it meets the threshold
def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    
    Parameters:
    - price (float): The original price of the item.
    - discount_percent (float): The discount percentage to apply.
    
    Returns:
    - float: The final price after discount if discount_percent >= 20, otherwise the original price.
    
    This function aligns with real-world retail practices where discounts below a certain threshold (e.g., 20%) may not be applied to maintain profit margins or comply with promotional policies. It demonstrates conditional logic and basic arithmetic operations, key in academic programming curricula.
    """
    if discount_percent >= 20:
        # Apply discount: subtract the discount amount from the original price
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
    else:
        # No discount applied if below threshold
        final_price = price
    return final_price

# Main program to interact with the user
if __name__ == "__main__":
    try:
        # Prompt user for input, ensuring robustness against invalid entries
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Calculate and print the final price
        final_price = calculate_discount(price, discount_percent)
        if discount_percent >= 20:
            print(f"Final price after {discount_percent}% discount: {final_price:.2f}")
        else:
            print(f"No discount applied (less than 20%). Original price: {final_price:.2f}")
    
    except ValueError:
        # Handle real-world input errors gracefully
        print("Invalid input. Please enter numeric values for price and discount percentage.")