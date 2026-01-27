# Linux Forensics

## 📑 Mục Lục
- [1. Một số lệnh trong Linux](#1-một-số-lệnh-trong-linux)
- [2. Tìm hiểu về Filesystem](#2-tìm-hiểu-về-filesystem)
- [3. Các file log trong Linux](#3-các-file-log-trong-linux)


---

## 1. Một số lệnh trong Linux 
`pwd` (Print working directory) 
- In ra đường dẫn tuyệt đối của thư mục hiện tại.

`ls` (List)
- Liệt kê các file và thư mục con trong thư mục hiện tại.

`cd` (Change directory)
- Thay đổi thư mục làm việc.

`mv` (Move)
- Di chuyển thư mục hoăc file.
- Đối với file thi có thể dùng để đổi tên file.

`rm` (Remove)
- Xóa file hoặc thư mục.
- Đối với thư mục cần thêm flag recursive -r.

`echo` 
- Tạo ra một chuối văn bản và in ra sdout.

`cat` 
- Copy dữ liệu raw của file và in ra sdout.
  
`find`
- Tìm kiếm vị trí của thư mục hoặc trong hệ thống dựa trên name, size, timestamps, etc.

`grep`
- Tìm kiếm một chuỗi ký tự nằm bên trong nội dung của file.

`file`
- Xác định loại file bằng cách xét duyệt header của file.

`strings`
- Đọc dữ liệu của file và in ra các ký tự đọc được.
`xxd`
- Tạo hex dump của file hoặc đảo ngược lại.

`ps`
- Hiển thị danh sách các tiến trình đang chạy trên hệ thống.

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

