- Do phòng này bị lock sau Premium nên em ghi lại những kiến thức chính được đề cập tại phòng này.

## File transfering
- `scp` là một protocol dựa trên `ssh`, được thiết kế để chuyển file qua lại một cách bảo mật giữa host và remote
- Syntax: `scp _source_ _destination_`.
  - Ví dụ: Để chuyển một file `abc.txt` tại host working directory đến `/home` tại remote
  `scp abc.txt username@ip/home/abc.txt`
- Để sử dụng `wget` để tải file từ remote
  - Login vô remote bằng `ssh`
  - Tạo kết nối `http` bằng module sẵn của `python`: `python -m http.server`
  - Port mặc định là 8000, trên host sử dụng `wget http://<IP>:8000/myRemoteFie` để tải file

## Processes
- Để hiển thị những tiến trình trong terminal hiện tại sử dụng `$ ps`
- Để hiện thị tiến trình của mọi user cũng như system `$ ps aux`
- Process management:
  - `kill _PID_`: gửi tín hiệu kết thúc đến process
  - `kill -KILL _PID_`: kết thúc process ngay lập tức
  - `kill -TSTP _PID_`: tạm ngưng process
  - `kill -CONT _PID_`: tiếp tục process bị tạm ngưng

## Services 
- Syntax: `systemctl _action_ _service_
- Các action của `systemctl`:
  - `start`: Khởi chạy một service
  - `stop`: Kết thúc một service
  - `enable`: Start at boot một service
  - `dienable`: Xóa start at boot một service
## Scheduled tasks
- Trên một số distro của linux, `cron` là một package được cài sẵn để quản lý các scheduled tasks
- Để chỉnh sửa các tiến trình sử dụng `crontabs -e`
- Ví dụ output: `0 2 * * * /usr/local/bin/backup.sh` : Chạy script tại 2h
