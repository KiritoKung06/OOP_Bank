class Account:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance  # Private variable
        print(f"[INFO] สร้างบัญชีสำหรับ {self.account_holder} ด้วยยอดเงิน {self.__balance}")
        

    def get_balance(self):
        return self.__balance

    def _update_balance(self, amount):
        self.__balance += amount
    def deposit(self, amount):
        print(f"[INFO]ยอดฝาก : {amount}")
        if not isinstance(amount, (int, float)):
            print("[Error] ยอดฝากที่พิมพ์ไม่ใช่ตัวเลข")
            raise TypeError("ยอดต้องเป็นตัวเลข")
        if amount <= 0:
            raise ValueError("ยอดเงินฝากเหลือน้อยกว่าหรือเท่ากับ 0")
        self._update_balance(amount)
    def withdraw(self, amount):
        print(f"[INFO] ยอดถอน : {amount}")
        if not isinstance(amount, (int,float)):
            print("[ERROR]ยอดถอนไม่ใช่ตัวเลข")
            raise TypeError("ยอดต้องเป็นตัวเลข")
        if amount <= 0:
            raise ValueError("ยอดเงินเหลือน้อยกว่าหรือเท่ากับ 0")
        if amount > self.get_balance():
            raise ValueError("ยอดเงินไม่เพียงพอ")
        self._update_balance(-amount)
class SavingsAccount(Account):
    def __init__(self, account_holder, balance=0, interest_rate =0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate
    def apply_interest(self):
        print("[INFO] เพิ่มดอกเบี้ย")
        if not isinstance(self.interest_rate, (int,float)):
            print("[ERROR]ดอกเบี้ยไม่ใช่ตัวเลข")
            raise TypeError("อัตราดอกเบี้ยต้องเป็นตัวเลข")
        if self.interest_rate < 0:
            print("[ERROR] อัตราดอกเบี้ย น้อยกว่า 0")
            raise ValueError("อัตราดอกเบี้ย ต้องไม่ติดลบ")
        interest = self.get_balance()*self.interest_rate
        print(f"[INFO] ดอกเบี้ยที่คำนวณ = {interest}")
        self.deposit(interest)
        print("[INFO] เพิ่มดอกเบี้ยทบสำเร็จ ")