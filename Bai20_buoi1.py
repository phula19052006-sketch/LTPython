def giai_quyet_bai_tap():
    # 1. Nhập dữ liệu đầu vào
    try:
        a = int(input("Nhập số tiền hàng cần trả (a): "))
        b = int(input("Nhập số tiền khách thực tế trả (b): "))
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ.")
        return

    # 2. Xử lý các trường hợp
    if a > b:
        print(f"Số tiền khách hàng còn thiếu là: {a - b}")
        return # Kết thúc chương trình
        
    elif a == b:
        print("Cám ơn khách hàng. Hẹn gặp lại")
        return # Kết thúc chương trình
        
    else:
        # Trường hợp a < b: Cần thối tiền
        tien_thoi = b - a
        print(f"So tien {tien_thoi} duoc doi thanh:")
        
        # Danh sách các mệnh giá tiền
        menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]
        
        tong_so_to = 0
        tong_so_loai = 0
        
        for loai in menh_gia:
            so_to = tien_thoi // loai  # Chia lấy nguyên để tìm số tờ
            
            if so_to > 0:
                print(f"Loai {loai} gom {so_to} to")
                tong_so_to += so_to
                tong_so_loai += 1
                tien_thoi %= loai  # Cập nhật số tiền dư còn lại
        
        print(f"TỔNG CỘNG CÓ {tong_so_to} TỜ")
        print(f"Tong so loai = {tong_so_loai}")
        
        # Đợi người dùng nhấn Enter
        input("\nNhấn Enter để kết thúc...")
        print("Cám ơn khách hàng. Hẹn gặp lại")

# Chạy chương trình
if __name__ == "__main__":
    giai_quyet_bai_tap()