### Which Linux distribution is being used on this machine?
> kali
<img width="1287" height="92" alt="image" src="https://github.com/user-attachments/assets/7154981f-834f-4cc6-84b4-8dadd3f7e95e" />
- Truy cập config của grub trong thư mục boot và search menuentry

### What is the MD5 hash of the Apache access.log file?
> d41d8cd98f00b204e9800998ecf8427e
<img width="675" height="327" alt="image" src="https://github.com/user-attachments/assets/383ad615-b2af-4d47-af02-d6795edc2995" />
- Sử dụng FTK Imager và export checksum của file 

### It is suspected that a credential dumping tool was downloaded. What is the name of the downloaded file?
> mimikatz_trunk.zip
<img width="364" height="406" alt="image" src="https://github.com/user-attachments/assets/4cec70ef-507a-442c-a5f9-836b580c0eba" />
- Kiểm tra thư mục Downloads

### A super-secret file was created. What is the absolute path to this file?
> /root/Desktop/SuperSecretFile.txt
<img width="1131" height="557" alt="image" src="https://github.com/user-attachments/assets/1af76056-a21e-4dde-a7d9-c1d0643df0c2" />
- Kiểm tra `bash_history`

### What program used the file didyouthinkwedmakeiteasy.jpg during its execution?
> binwalk
<img width="713" height="630" alt="image" src="https://github.com/user-attachments/assets/8a0736f9-0d64-4d1c-b810-2cf46e20d9e2" />
- Kiểm tra `bash_history`

### What is the third goal from the checklist Karen created?
> Profit
<img width="860" height="495" alt="image" src="https://github.com/user-attachments/assets/e680ce4d-667e-49d6-b08b-80716cd4ac24" />
- Kiểm tra các thư mục trong `bash_history`, Desktop có một file Checklist  

### How many times was Apache run?
> 0
<img width="911" height="247" alt="image" src="https://github.com/user-attachments/assets/9674b388-7281-4693-a26e-7fe948939856" />
- Log của Apache chưa được khởi tạo

### This machine was used to launch an attack on another. Which file contains the evidence for this?
> irZLAohL.jpeg
<img width="1549" height="783" alt="image" src="https://github.com/user-attachments/assets/6f52f066-e198-4d06-b5ad-41db4f84156c" />
- Trong `~` có một file `.jpeg` khả nghi

### It is believed that Karen was taunting a fellow computer expert through a bash script within the Documents directory. Who was the expert that Karen was taunting?
> Young
<img width="1029" height="578" alt="image" src="https://github.com/user-attachments/assets/f502b795-67b5-4578-b4d9-3d4714cf39fe" />
- Kiểm tra content của file script

### A user executed the su command to gain root access multiple times at 11:26. Who was the user?
> postgres
<img width="603" height="25" alt="image" src="https://github.com/user-attachments/assets/f206c764-9d7f-42bd-99ba-1ede432c945b" />
- Truy xuất file `auth.log` trong `/var/log/`, search mốc thời gian được cung cấp

### Based on the bash history, what is the current working directory?
> /root/Documents/myfirsthack/
<img width="274" height="69" alt="image" src="https://github.com/user-attachments/assets/b333088f-6ac3-4de2-a2b3-65060d3b890e" />
- Lần `cd` cuối cùng trong `bash_history`



