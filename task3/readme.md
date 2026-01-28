# Linux Forensics

## 📑 Mục Lục
- [1. Một số lệnh trong Linux](#1-một-số-lệnh-trong-linux)
- [2. Tìm hiểu về Filesystem](#2-tìm-hiểu-về-filesystem)
- [3. Các file log trong Linux](#3-các-file-log-trong-linux)


---

## 1. Một số lệnh trong Linux 
- `pwd` (Print working directory) 
  - In ra đường dẫn tuyệt đối của thư mục hiện tại.
  <img width="438" height="150" alt="image" src="https://github.com/user-attachments/assets/4ca3c5d5-c189-4c09-be90-b83fd69e6d3a" />
  
- `cd` (Change directory)
  - Thay đổi thư mục làm việc.
  <img width="438" height="150" alt="image" src="https://github.com/user-attachments/assets/4ca3c5d5-c189-4c09-be90-b83fd69e6d3a" />

- `ls` (List)
  - Liệt kê các file và thư mục con trong thư mục hiện tại.
  <img width="438" height="150" alt="image" src="https://github.com/user-attachments/assets/111c34ca-4c7d-41ba-8208-4dafb4fc8c1c" />



- `mv` (Move)
  - Di chuyển thư mục hoăc file.
  - Đối với file thi có thể dùng để đổi tên file.
  <img width="438" height="150" alt="image" src="https://github.com/user-attachments/assets/f50c3575-94a8-491f-af2a-b08ff6e6cbd5" />

- `rm` (Remove)
  - Xóa file hoặc thư mục.
  - Đối với thư mục cần thêm flag recursive -r.
  <img width="438" height="150" alt="image" src="https://github.com/user-attachments/assets/7f165007-a226-45e6-8cd0-a1d063c623d5" />
  
- `echo` 
  - Tạo ra một chuối văn bản và in ra sdout hoặc một file.
  <img width="438" height="150" alt="image" src="https://github.com/user-attachments/assets/53e77d49-f581-4e98-b674-88909a0b2c5d" />
  

- `cat` 
  - Copy dữ liệu raw của file và in ra sdout.
  <img width="438" height="150" alt="image" src="https://github.com/user-attachments/assets/bb744570-6edc-43b5-a9bf-9e11f8814380" />
  
- `find`
  - Tìm kiếm vị trí của thư mục hoặc trong hệ thống dựa trên name, size, timestamps, etc.
  <img width="438" height="150" alt="image" src="https://github.com/user-attachments/assets/15d20842-52a3-4683-b50f-4746a3d6dd1e" />

- `grep`
  - Tìm kiếm một chuỗi ký tự nằm bên trong nội dung của file.
  <img width="438" height="150" alt="image" src="https://github.com/user-attachments/assets/df68fd72-166b-43b1-bdeb-e19f916fd9bc" />

- `file`
  - Xác định loại file bằng cách xét duyệt header của file.
  <img width="438" height="150" alt="image" src="https://github.com/user-attachments/assets/fe3e43fc-575c-4f44-abf6-05fe8fa182ed" />

- `strings`
  - Đọc dữ liệu của file và in ra các ký tự đọc được.
  <img width="438" height="150" alt="image" src="https://github.com/user-attachments/assets/d1868663-fe32-4c1e-b081-f75432141259" />

- `xxd`
  - Tạo hex dump của file hoặc đảo ngược lại.
  <img width="438" height="150" alt="image" src="https://github.com/user-attachments/assets/440a5251-7d4d-4651-8570-9acaa8acdcce" />
  <img width="438" height="150" alt="image" src="https://github.com/user-attachments/assets/f21a75b3-2f8c-4eea-8654-5c7cc26b28c8" />

- `ps`
  - Hiển thị danh sách các tiến trình đang chạy trên hệ thống.
  <img width="438" height="150" alt="image" src="https://github.com/user-attachments/assets/1a58992b-49aa-49de-ad5c-e5e0dbfa55bf" />

## 2. Tìm hiểu về Filesystem
- File System là phương pháp và cấu trúc dữ liệu mà hệ điều hành sử dụng để quản lý cách dữ liệu được lưu trữ / truy xuất trên ổ đĩa.
- Có nhiều File System khác nhau như:
  - FAT32 -> Ban đầu được thiết kế dành cho DOS và Microsoft Windows. Vào thời nay được dùng rộng rãi cho các thiết bị lưu trữ ngoại
  - NTFS  -> File system được sử dụng bởi Microsoft Windows hiện đại.
  - EXT4  -> File system được sử dụng bởi các distro Linux 
  - APFS  -> File system được sử dụng bởi Apple
- Tập trung vào 2 file systems phổ biến nhất:
  ### NTFS
  - Là file system của Microsoft Windows, hỗ trợ hạn chế trên Linux.
  - Trong NTFS, tất cả mọi file sẽ được lưu dưới dạng bảng ghi. Bảng ghi này được lưu trữ trong metadata file `$MFT`.
  - Khi cần lưu một file mới hệ thống sẽ ghi vào vị trí đầu tiên tim được. Vì vậy dễ bị phân mảnh.
  - Nếu như kích thước file vượt quá giới hạn của bảng ghi thì sẽ được lưu ngoài bảng ghi. Khi đó bảng ghi sẽ chỉ lưu địa chỉ của file thay vì nội dung file.
  - Alternate data stream: Một file có thể có nhiều stream dữ liệu khác nhau.
  - Journaling: Ghi lại metadata vào `$LogFile`. Nếu sập nguồn, nó dùng file này để sửa lại cấu trúc thư mục.
  - Compression & Encryption: Người dùng có thể nén hay mã hóa file trực mà không cần cài thêm phần mềm.
  ### EXT4
  - Là file system của các distro Linux, chỉ hỗ trợ read-only trên Windows
  - Trong EXT4, metadata được lưu trong cấu trúc gọi là Inode (Index Node). Inode lưu tất cả thuộc tính (quyền, kích thước, thời gian...) ngoại trừ tên file.
  - Sử dụng cơ chế Delayed Allocation: Hệ thống không ghi ngay lập tức mà đợi gom đủ dữ liệu để tìm vùng trống phù hợp. Vì vậy rất ít bị phân mảnh.
  - Dữ liệu được quản lý bằng Extents. Thay vì liệt kê địa chỉ từng block lẻ tẻ (như các bản ext cũ), Extents chỉ lưu "địa chỉ bắt đầu" và "độ dài liên tục", giúp tăng tốc độ xử lý file lớn.
  - Không có Alternate data stream, nếu copy một file có ADS từ NTFS vào EXT4, ADS sẽ bị mất.
  - Có hỗ trợ Journaling.
  - Có hỗ trợ Encryption trên các kernel mới. Tuy nhiên không hỗ trợ Compression, cần phải cài thêm phần mềm thứ 3.

## 3. Các file log trong Linux
### Journald
- Trước đây, log được gửi đến một deamon như **syslogd** hay **rsyslog**, sau đó được lưu vào file dưới dạng **plain text** tại thư mục `/var/log`.
- Với sự ra đời của **systemd**, **systemd-journald** đóng vai trò thu thập log thay cho các deamon syslog cũ. Log sẽ được chuyển đến journald và được lưu vào file dưới dạng **binary journal**. Khác với syslogd hay rsyslog, journald có thể được cấu hình để:
  - lưu persistent tại `/var/log/journal`,  hoặc
  - chỉ lưu in-memory tại `/run/log/journal`.
- Để chỉnh sửa cấu hình của **journald**, truy cập `etc/systemd/journald.conf`.
- Để đảm bảo tính tương thích ngược, **journald** có thể forward log đến **rsyslog** để tạo các log dạng **plain text** tại `/var/log/` tương tự các phiên bản cũ.
- Để đọc các file log của journald, có thể sử dụng lệnh `$ journalctl`
- Trong đa số trường hợp, `journalctl` sẽ được sử dụng kèm với các flags như `-r` và `-u`.
- Để in các log gần đây, sử dụng `$ journalctl -r`.
<img width="800" height="200" alt="image" src="https://github.com/user-attachments/assets/c6d52f73-33a6-4e5f-82ea-dbbcafb16d6b" />

- Để in các log của một service cụ thể, sử dụng `$ journalctl -u 00service_name`
<img width="800" height="200" alt="image" src="https://github.com/user-attachments/assets/22d540c3-a1d6-4d3b-be99-a28a119e0375" />

- Để theo dõi một file log trong thời gian thực, sử dụng flag `-f` :  `$ journalctl -f -u 00service_name`
- Để ghi thủ công một log vào journald, sử dụng `$ logger 00message_content`
<img width="800" height="200" alt="image" src="https://github.com/user-attachments/assets/c3114115-a3d4-4d71-a30e-ba6e9943464b" />

### Bash history
- Bash history được dùng để ghi lại các lệnh được thực thi sau khi người dùng nhấn Enter.

- Theo mặc định, các lệnh sẽ được lưu tạm thời trong memory trong suốt phiên làm việc hiện tại. Khi người dùng logout, Bash sẽ ghi các lệnh này vào file history tại `~/.bash_history`
<img width="701" height="230" alt="image" src="https://github.com/user-attachments/assets/01c4eaec-4458-40f4-a1fa-efd06dcee0a1" />

- Khác với Journal, bash_history có thể dễ dàng bị chỉnh sửa nên cần cân nhắc khi phân tích.
---







