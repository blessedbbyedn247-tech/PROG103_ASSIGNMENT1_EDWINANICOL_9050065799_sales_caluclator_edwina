"""
Small Business Sales Calculator with Inventory Management
Author: [Your Name]
Course: Structured Programming Assignment 1
Description: A terminal-based system for small businesses to track sales,
manage inventory, calculate profits, and generate receipts.
"""

# Constants
TAX_RATE = 0.15  # 15% sales tax (Sierra Leone standard)
SDG_GOAL = "SDG 8: Decent Work and Economic Growth"

# Initial inventory (product_name: [price, cost_price, quantity])
inventory = {
    "Rice": [2500, 1800, 100],
    "Sugar": [1800, 1200, 50],
    "Soap": [1500, 900, 75],
    "Oil": [3000, 2200, 40],
    "Flour": [2000, 1400, 60]
}

sales_records = []
receipt_counter = 1

# Function 1: Display inventory
def display_inventory():
    """
    Display current inventory with prices and quantities.
    """
    print("\n" + "="*80)
    print("CURRENT INVENTORY".center(80))
    print("="*80)
    print(f"{'Product':<15} {'Selling Price':<18} {'Cost Price':<15} {'Quantity':<10}")
    print("-"*80)
    
    for product, details in inventory.items():
        print(f"{product:<15} Le {details[0]:<15.2f} Le {details[1]:<12.2f} {details[2]:<10}")
    
    print("="*80)

# Function 2: Calculate sale details
def calculate_sale_details(quantity, price_per_unit, cost_per_unit):
    """
    Calculate total revenue, tax, profit, and net profit for a sale.
    
    Parameters:
    quantity: number of items sold
    price_per_unit: selling price per item
    cost_per_unit: cost price per item
    
    Returns: tuple (total_revenue, tax_amount, profit, net_profit)
    """
    total_revenue = quantity * price_per_unit
    tax_amount = total_revenue * TAX_RATE
    profit_before_tax = quantity * (price_per_unit - cost_per_unit)
    net_profit = profit_before_tax - tax_amount
    
    return total_revenue, tax_amount, profit_before_tax, net_profit

# Function 3: Generate receipt
def generate_receipt(sale_details):
    """
    Generate and display a receipt for a sale.
    
    Parameters:
    sale_details: dictionary containing all sale information
    """
    global receipt_counter
    
    print("\n" + "="*60)
    print("BUSINESS RECEIPT".center(60))
    print("="*60)
    print(f"Receipt Number: REC-{receipt_counter:05d}")
    print(f"Date: {sale_details['date']}")
    print("-"*60)
    print(f"Item: {sale_details['item']}")
    print(f"Quantity: {sale_details['quantity']}")
    print(f"Price per unit: Le {sale_details['selling_price']:.2f}")
    print("-"*60)
    print(f"Subtotal: Le {sale_details['revenue']:.2f}")
    print(f"Tax (15%): Le {sale_details['tax']:.2f}")
    print(f"Total Amount: Le {sale_details['total_payment']:.2f}")
    print("-"*60)
    print(f"Cost Price: Le {sale_details['cost_price']:.2f}")
    print(f"Net Profit: Le {sale_details['net_profit']:.2f}")
    print("="*60)
    print("Thank you for your purchase!")
    print("Supporting local business growth in Sierra Leone")
    print("="*60 + "\n")
    
    receipt_counter += 1

# Function 4: Display sales summary
def display_sales_summary():
    """
    Display a formatted summary of all sales records.
    """
    if not sales_records:
        print("\nNo sales records to display.")
        return
    
    print("\n" + "="*80)
    print("ALL SALES SUMMARY REPORT".center(80))
    print("="*80)
    print(f"{'Receipt':<10} {'Item':<12} {'Qty':<8} {'Revenue':<14} {'Tax':<12} {'Profit':<12}")
    print("-"*80)
    
    total_revenue_all = 0
    total_tax_all = 0
    total_profit_all = 0
    
    for record in sales_records:
        print(f"{record['receipt']:<10} {record['item']:<12} {record['quantity']:<8} "
              f"Le {record['revenue']:<11.2f} Le {record['tax']:<9.2f} Le {record['profit']:<11.2f}")
        total_revenue_all += record['revenue']
        total_tax_all += record['tax']
        total_profit_all += record['profit']
    
    print("-"*80)
    print(f"{'TOTAL':<10} {'':<12} {'':<8} Le {total_revenue_all:<11.2f} Le {total_tax_all:<9.2f} Le {total_profit_all:<11.2f}")
    print("="*80)
    print(f"\nSupporting {SDG_GOAL}")
    print(f"Total Transactions: {len(sales_records)}")
    print(f"Total Revenue: Le {total_revenue_all:.2f}")
    print(f"Total Tax Collected: Le {total_tax_all:.2f}")
    print(f"Total Net Profit: Le {total_profit_all:.2f}")

# Function 5: Check and update inventory
def update_inventory(product_name, quantity_sold):
    """
    Update inventory after a sale.
    
    Parameters:
    product_name: name of the product
    quantity_sold: quantity sold
    
    Returns: boolean (True if successful, False if insufficient stock)
    """
    if product_name in inventory:
        if inventory[product_name][2] >= quantity_sold:
            inventory[product_name][2] -= quantity_sold
            return True
        else:
            print(f"\nInsufficient stock! Only {inventory[product_name][2]} units available.")
            return False
    else:
        print(f"\nProduct '{product_name}' not found in inventory.")
        return False

# Function 6: Add new product to inventory
def add_new_product():
    """
    Add a new product to the inventory.
    """
    print("\n--- ADD NEW PRODUCT ---")
    product_name = input("Enter product name: ").strip().title()
    
    if product_name in inventory:
        print(f"Product '{product_name}' already exists in inventory.")
        return
    
    try:
        selling_price = float(input("Enter selling price per unit (Leones): "))
        if selling_price <= 0:
            print("Price must be positive.")
            return
        
        cost_price = float(input("Enter cost price per unit (Leones): "))
        if cost_price <= 0:
            print("Cost must be positive.")
            return
        
        quantity = int(input("Enter initial quantity: "))
        if quantity < 0:
            print("Quantity cannot be negative.")
            return
        
        inventory[product_name] = [selling_price, cost_price, quantity]
        print(f"\nProduct '{product_name}' added successfully!")
        
    except ValueError:
        print("Invalid input. Product not added.")

# Function 7: Restock existing product
def restock_product():
    """
    Add more quantity to an existing product.
    """
    print("\n--- RESTOCK PRODUCT ---")
    product_name = input("Enter product name to restock: ").strip().title()
    
    if product_name not in inventory:
        print(f"Product '{product_name}' not found in inventory.")
        print("Use 'Add New Product' option to add it.")
        return
    
    try:
        additional_quantity = int(input(f"Enter quantity to add to {product_name}: "))
        if additional_quantity <= 0:
            print("Quantity must be positive.")
            return
        
        inventory[product_name][2] += additional_quantity
        print(f"\nUpdated! {product_name} now has {inventory[product_name][2]} units.")
        
    except ValueError:
        print("Invalid input.")

# Main program
def main():
    print("\n" + "="*60)
    print("SMALL BUSINESS SALES CALCULATOR".center(60))
    print("="*60)
    print(f"Supporting {SDG_GOAL}")
    print(f"Tax Rate: {TAX_RATE * 100}%\n")
    
    from datetime import datetime
    
    while True:
        # Main menu
        print("\n" + "-"*50)
        print("MAIN MENU")
        print("-"*50)
        print("1. Make a Sale")
        print("2. View Inventory")
        print("3. Add New Product")
        print("4. Restock Product")
        print("5. View Sales Summary")
        print("6. Exit")
        print("-"*50)
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            # Make a sale
            print("\n--- PROCESS SALE ---")
            
            # Display available products
            print("\nAvailable Products:")
            for idx, (product, details) in enumerate(inventory.items(), 1):
                print(f"{idx}. {product} - Le {details[0]:.2f} (Stock: {details[2]})")
            
            # Select product
            product_name = input("\nEnter product name: ").strip().title()
            
            if product_name not in inventory:
                print(f"Product '{product_name}' not found in inventory.")
                continue
            
            product_price = inventory[product_name][0]
            product_cost = inventory[product_name][1]
            available_stock = inventory[product_name][2]
            
            if available_stock == 0:
                print(f"Sorry, {product_name} is out of stock!")
                continue
            
            print(f"\nProduct: {product_name}")
            print(f"Selling Price: Le {product_price:.2f}")
            print(f"Available Stock: {available_stock}")
            
            # Input quantity
            while True:
                try:
                    quantity = int(input("Enter quantity to sell: "))
                    if quantity <= 0:
                        print("Quantity must be positive. Please try again.")
                        continue
                    if quantity > available_stock:
                        print(f"Insufficient stock! Only {available_stock} units available.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            
            # Calculate sale details
            revenue, tax, profit_before, net_profit = calculate_sale_details(
                quantity, product_price, product_cost
            )
            
            total_payment = revenue  # Customer pays revenue including tax
            
            # Check profitability
            print("\n--- SALE ANALYSIS ---")
            if net_profit > 0:
                print(f"This sale is PROFITABLE! Net profit: Le {net_profit:.2f}")
            elif net_profit == 0:
                print(f"Break-even sale. No profit or loss.")
            else:
                print(f"This sale resulted in a LOSS of Le {abs(net_profit):.2f}")
            
            # Show breakdown
            print(f"\nSale Breakdown:")
            print(f"  * Total Revenue (including tax): Le {revenue:.2f}")
            print(f"  * Tax (15%): Le {tax:.2f}")
            print(f"  * Cost of Goods Sold: Le {quantity * product_cost:.2f}")
            print(f"  * Net Profit: Le {net_profit:.2f}")
            
            # Confirm sale
            confirm = input("\nConfirm this sale? (yes/no): ").strip().lower()
            if confirm in ['yes', 'y']:
                # Update inventory
                if update_inventory(product_name, quantity):
                    # Prepare sale record
                    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    
                    sale_record = {
                        'receipt': f"REC-{receipt_counter:05d}",
                        'date': current_date,
                        'item': product_name,
                        'quantity': quantity,
                        'selling_price': product_price,
                        'cost_price': product_cost,
                        'revenue': revenue,
                        'tax': tax,
                        'total_payment': total_payment,
                        'net_profit': net_profit,
                        'profit_before_tax': profit_before
                    }
                    
                    sales_records.append(sale_record)
                    
                    # Generate receipt
                    generate_receipt(sale_record)
                    
                    print(f"Sale completed successfully!")
                    print(f"Remaining stock of {product_name}: {inventory[product_name][2]}")
                else:
                    print("Sale cancelled due to inventory issue.")
            else:
                print("Sale cancelled.")
        
        elif choice == '2':
            # View inventory
            display_inventory()
        
        elif choice == '3':
            # Add new product
            add_new_product()
        
        elif choice == '4':
            # Restock product
            restock_product()
        
        elif choice == '5':
            # View sales summary
            display_sales_summary()
        
        elif choice == '6':
            # Exit
            print("\n" + "="*60)
            print("Thank you for using Small Business Sales Calculator!")
            print(f"Total sales processed: {len(sales_records)}")
            if sales_records:
                total_rev = sum(r['revenue'] for r in sales_records)
                total_prof = sum(r['net_profit'] for r in sales_records)
                print(f"Total Revenue: Le {total_rev:.2f}")
                print(f"Total Profit: Le {total_prof:.2f}")
            print("Keep supporting local business growth in Sierra Leone.")
            print("="*60 + "\n")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# Program entry point
if __name__ == "__main__":
    main()