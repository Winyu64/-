import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from tabulate import tabulate

class QuotationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ใบเสนอราคา")
        
        self.customer_name_label = tk.Label(root, text="ชื่อลูกค้า:")
        self.customer_name_label.grid(row=0, column=0, padx=10, pady=5)
        self.customer_name_entry = tk.Entry(root)
        self.customer_name_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.quotation_number_label = tk.Label(root, text="เลขที่ใบเสนอราคา:")
        self.quotation_number_label.grid(row=1, column=0, padx=10, pady=5)
        self.quotation_number_entry = tk.Entry(root)
        self.quotation_number_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.tax_id_label = tk.Label(root, text="เลขที่ผู้เสียภาษี:")
        self.tax_id_label.grid(row=2, column=0, padx=10, pady=5)
        self.tax_id_entry = tk.Entry(root)
        self.tax_id_entry.grid(row=2, column=1, padx=10, pady=5)
        
        self.address_label = tk.Label(root, text="ที่อยู่:")
        self.address_label.grid(row=3, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(root)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)
        
        self.contact_number_label = tk.Label(root, text="เบอร์ติดต่อ:")
        self.contact_number_label.grid(row=4, column=0, padx=10, pady=5)
        self.contact_number_entry = tk.Entry(root)
        self.contact_number_entry.grid(row=4, column=1, padx=10, pady=5)
        
        self.items = []
        
        self.item_name_label = tk.Label(root, text="รายการสินค้า:")
        self.item_name_label.grid(row=5, column=0, padx=10, pady=5)
        self.item_name_entry = tk.Entry(root)
        self.item_name_entry.grid(row=5, column=1, padx=10, pady=5)
        
        self.quantity_label = tk.Label(root, text="จำนวน:")
        self.quantity_label.grid(row=6, column=0, padx=10, pady=5)
        self.quantity_entry = tk.Entry(root)
        self.quantity_entry.grid(row=6, column=1, padx=10, pady=5)
        
        self.unit_price_label = tk.Label(root, text="ราคาต่อหน่วย:")
        self.unit_price_label.grid(row=7, column=0, padx=10, pady=5)
        self.unit_price_entry = tk.Entry(root)
        self.unit_price_entry.grid(row=7, column=1, padx=10, pady=5)
        
        self.add_item_button = tk.Button(root, text="เพิ่มรายการสินค้า", command=self.add_item)
        self.add_item_button.grid(row=8, column=1, padx=10, pady=5)
        
        self.show_quotation_button = tk.Button(root, text="แสดงใบเสนอราคา", command=self.show_quotation)
        self.show_quotation_button.grid(row=9, column=1, padx=10, pady=5)
        
        self.total_amount = 0

    def add_item(self):
        item_name = self.item_name_entry.get()
        try:
            quantity = int(self.quantity_entry.get())
            unit_price = float(self.unit_price_entry.get())
        except ValueError:
            messagebox.showerror("Error", "กรุณากรอกจำนวนและราคาต่อหน่วยเป็นตัวเลข")
            return
        
        amount = quantity * unit_price
        self.items.append([len(self.items) + 1, item_name, quantity, unit_price, amount])
        self.total_amount += amount
        
        self.item_name_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.unit_price_entry.delete(0, tk.END)
        
        messagebox.showinfo("Success", "เพิ่มรายการสินค้าเรียบร้อยแล้ว")
    
    def show_quotation(self):
        customer_name = self.customer_name_entry.get()
        quotation_number = self.quotation_number_entry.get()
        tax_id = self.tax_id_entry.get()
        address = self.address_entry.get()
        contact_number = self.contact_number_entry.get()
        
        vat = self.total_amount * 0.07
        total_with_vat = self.total_amount + vat
        
        headers = ["ลำดับที่", "รายการสินค้า", "จำนวน", "ราคาต่อหน่วย", "จำนวนเงิน"]
        items_table = tabulate(self.items, headers=headers, tablefmt="grid")
        
        quotation_text = (
            f"ใบเสนอราคา บริษัท ดิจิทัลเทคโนโลยี\n"
            f"123 ต.หนองกองเกาะ อ.เมือง จ.หนองคาย 43000\n\n"
            f"ชื่อลูกค้า: {customer_name}\n"
            f"เลขที่ใบเสนอราคา: {quotation_number}\n"
            f"เลขที่ผู้เสียภาษี: {tax_id}\n"
            f"วันที่: {datetime.now().strftime('%d/%m/%Y')}\n"
            f"ที่อยู่: {address}\n"
            f"เบอร์ติดต่อ: {contact_number}\n\n"
            f"{items_table}\n\n"
            f"ราคารวม: {self.total_amount:,.2f} บาท\n"
            f"ภาษีมูลค่าเพิ่ม (7%): {vat:,.2f} บาท\n"
            f"ราคารวมทั้งหมด: {total_with_vat:,.2f} บาท"
        )
        
        messagebox.showinfo("ใบเสนอราคา", quotation_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuotationApp(root)
    root.mainloop()
