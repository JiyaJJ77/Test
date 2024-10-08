print("Create Your account")
name=input("Enter Your Name")
print(name)
phone=input("Enter phone number")
if len(phone)==11:
 print('phone number',phone)
else:
   print("You entered a wrong number")
Cnic=input("Enter Your CNIC Number")
if len(Cnic)==13:
   print('Cnic number:',Cnic)
else:
   print("You entered a wrong Cnic number")
gender=input("Enter your gender: (Female/male)")
if gender.lower()=="female":
    print('female')
elif gender.lower()=="male":
    print('male')
else:
    print("Invalid input.Please enter either 'female' or 'male'.")
account=name[2:3]+phone[1:7]+Cnic[2:8]
print('Your account number is:',account)
mpin=input("Enter Your MPIN Code")
if len(mpin)==4:
   print('MPin is:',mpin)
credit=100000

#file handling to insert the record of current user account
file_name = 'accounts.txt'
with open(file_name,'a')as file:
   file.write(f"{name} {phone} {Cnic} {gender} {account} {mpin} {credit},")

file_path = 'accounts.txt'
with open(file_path, 'r') as f:
    file_data = f.read()
                                               
records_list = file_data.split(',')
mpin = input('please enter mpin')
# now confirm the mpin exists in this data or not 
for rec in records_list:
    if rec != '':
        name, phone, cnic, gender, accno, mpin_, balance = rec.split(' ')
        if mpin == mpin_:
            sender_record = 0     
            receiver_accno=input("Enter receiver account number")
            receiver_record=0 
            for records in records_list:
                if records != '':
                    name_rec, phone_rec, cnic_rec, gender_rec, accno_rec, mpin__rec, balance_rec = records.split(' ')
                    if accno_rec ==receiver_accno:                                                                                                                                                                                                                                     
                        receiver_record=balance_rec
                        amount = int(input("Enter the amount to transfer: "))
                        sender_record=int(balance)
                        receiver_record=int(balance_rec)
                        sender_record -= amount
                        receiver_record += amount
                        notification_message = f" from {accno} to {receiver_accno} amount {amount} successfully sent to ."
                        file_path='notifications.txt'
                        with open((file_path),'a')as file:
                            file.write(notification_message)
                            print("Transaction Successfull")  
                            print('account_no', accno)
                    else:
                        print("reciever account not found")
        else:
            print('sender account not found yet')
    