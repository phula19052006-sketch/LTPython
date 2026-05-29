# 1. ĐỊNH NGHĨA CÁC HÀM LAMBDA (Đảm bảo trả về kiểu Boolean)
# Cách 1 dùng all(): Tất cả các chữ số trong chuỗi phải giống chữ số đầu tiên
is_dong_nhat_all = lambda k: k > 0 and all(char == str(k)[0] for char in str(k))

# Cách 2 dùng any(): Không có bất kỳ chữ số nào khác chữ số đầu tiên
is_dong_nhat_any = lambda k: k > 0 and not any(char != str(k)[0] for char in str(k))

# Số hoàn thiện: Tổng các ước từ 1 đến n//2 bằng chính n
is_hoan_thien = lambda n: n > 1 and sum(i for i in range(1, n // 2 + 1) if n % i == 0) == n

# 2. DUYỆT VÀ IN KẾT QUẢ TRONG KHOẢNG [1, 10000]
if __name__ == "__main__":
    print("--- TÌM SỐ ĐỒNG NHẤT (Từ 1 đến 10000) ---")
    # Sử dụng hàm lambda cách 1 (all) để lọc
    ds_dong_nhat_1 = [x for x in range(1, 10001) if is_dong_nhat_all(x)]
    print(f"Cách 1 (Sử dụng all): {ds_dong_nhat_1}\n")
    
    # Sử dụng hàm lambda cách 2 (any) để lọc
    ds_dong_nhat_2 = [x for x in range(1, 10001) if is_dong_nhat_any(x)]
    print(f"Cách 2 (Sử dụng any): {ds_dong_nhat_2}\n")
    
    print("--- TÌM SỐ HOÀN THIỆN (Từ 1 đến 10000) ---")
    ds_hoan_thien = [x for x in range(1, 10001) if is_hoan_thien(x)]
    print(f"Kết quả số hoàn thiện: {ds_hoan_thien}")