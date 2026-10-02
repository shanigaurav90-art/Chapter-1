import qrcode

class QRGenerator:

    def text_to_qr(self):
        text = input("Enter text or message: ")

        img = qrcode.make(text)
        img.save("text_qr.png")

        print("\nText QR saved as text_qr.png")

    def website_to_qr(self):
        url = input("Enter website URL (https://...): ")

        img = qrcode.make(url)
        img.save("website_qr.png")

        print("\nWebsite QR saved as website_qr.png")

    def upi_payment_qr(self):
        print("\n===== AUTO PAY QR =====")

        upi_id = input("Enter UPI ID : ")
        name = input("Enter Payee Name: ")
        amount = input("Enter Amount (Optional): ")

        if amount == "":
            upi_link = f"upi://pay?pa={upi_id}&pn={name}"
        else:
            upi_link = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR"

        img = qrcode.make(upi_link)
        file_name = input("Enter file name: ")
        if not file_name.endswith(".png"):
            file_name += ".png"

        img.save(file_name)

        print("\nUPI Payment QR saved as", file_name)

        

    def menu(self):
        while True:
            print("\n===== QR GENERATOR MENU =====")
            print("1. Text to QR")
            print("2. Website to QR")
            print("3. UPI Payment QR")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.text_to_qr()
            elif choice == "2":
                self.website_to_qr()
            elif choice == "3":
                self.upi_payment_qr()
            elif choice == "4":
                print("=== Bye ===")
                break
            else:
                print("Invalid choice")

qr = QRGenerator()
qr.menu()