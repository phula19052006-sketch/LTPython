def tinh_khoi_hinh_chu_nhat():
    # Nhập dữ liệu từ bàn phím và ép kiểu số thực
    length = float(input("Nhập chiều dài đáy hình khối chữu nhật (cm):"))
    width = float(input("Nhập chiều rộng đáy hình khối chữ nhật (cm):"))
    height = float(input("Nhập chiều cao hình khối chữ nhật (cm):"))

    # Nhập số lượng số lẻ cần hiển thị
    decimal_places = int(input("Số lượng số lẻ cần hiển thị: "))

    # tính toán diện tích đáy và thể tích
    base_area = length * width
    volume = base_area * height
    
    # Định dạng chuỗi hiển thị theo số chữ số thập phân yêu cầu
    fmt = f".{decimal_places}f"
    
    # Xuất kết quả kèm ký tự unicode mũ 2 (\u00B2) và mũ 3 (\u00B3)
    print(f"Diện tích đáy hình chữ nhật = {format(base_area, fmt)} cm\u00B2")
    print(f"Thể tích hình khối = {format(volume, fmt)} cm\u00B3")

if __name__ == "__main__":
    tinh_khoi_hinh_chu_nhat() 