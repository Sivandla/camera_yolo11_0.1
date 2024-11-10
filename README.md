# 1. Thư viện sử dụng:
---

- cv2, YOLO

# 2. Nguyên lý hoạt động:
---

- Sử dụng camera ở trong máy thông qua thư viện cv2 và khởi tạo model của yolo11.
- Sau khi khởi tạo thành công camera, model sẽ đọc từng khung hình, đóng khung cũng như gán nhãn cho các đối tượng ở trong khung hình.
- Cuối cùng sẽ đưa ra giá trị của các đối tượng có trong khung.

  <img width="520" alt="camera_test" src="https://github.com/user-attachments/assets/724743d2-621f-4ddd-bbe3-2dcd2a0ff627">
