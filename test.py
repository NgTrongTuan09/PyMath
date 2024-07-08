import cv2
import numpy as np

def detect_fingers(image):
    # Khởi tạo các biến
    fingers = []
    threshold = 0.7

    # Xác định các đường biên của bàn tay
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Lặp qua tất cả các đường biên
    for contour in contours:
        # Tính diện tích của đường biên
        area = cv2.contourArea(contour)

        # Nếu diện tích đường biên lớn hơn một ngưỡng nhất định
        if area > threshold:
            # Xác định các điểm đỉnh của đường biên
            points = cv2.convexHull(contour)

            # Tính số lượng các điểm đỉnh của đường biên
            num_points = len(points)

            # Nếu số lượng các điểm đỉnh là 5
            if num_points == 5:
                # Thêm đường biên này vào danh sách các ngón tay
                fingers.append(contour)

    return fingers

# Khởi tạo camera
cap = cv2.VideoCapture(0)

while True:
    # Đọc một khung hình từ camera
    ret, frame = cap.read()

    # Chuyển đổi khung hình sang màu xám
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Áp dụng bộ lọc Gaussian để giảm nhiễu
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Xác định các ngưỡng
    ret, thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)

    # Tìm các ngón tay
    fingers = detect_fingers(thresh)

    # Vẽ các ngón tay lên khung hình
    for finger in fingers:
        cv2.drawContours(frame, [finger], 0, (0, 255, 0), 3)

    # Hiển thị khung hình
    cv2.imshow("Frame", frame)

    # Chạm phím ESC để thoát
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

# Đóng camera
cap.release()

# Đóng tất cả các cửa sổ
cv2.destroyAllWindows()
