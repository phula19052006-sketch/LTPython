import math

# 1. Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Kiểm tra từ 3 đến căn bậc hai của n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# 2. Hàm kiểm tra số Strobogrammatic (Gốc)
def is_strobogrammatic(n):
    s = str(n)
    # Các cặp chữ số tự đối xứng hoặc đổi chỗ cho nhau khi xoay 180 độ
    mapping = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
    
    rotated_str = ""
    # Duyệt ngược chuỗi để mô phỏng hành động xoay 180 độ
    for char in reversed(s):
        if char not in mapping:
            return False
        rotated_str += mapping[char]
        
    return rotated_str == s

# 3. Hàm kiểm tra số Strobogrammatic Mở rộng
def is_strobogrammatic_extended(n):
    s = str(n)
    # Bổ sung cặp '2':'2' và '5':'5' theo kết quả mẫu câu d
    mapping = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6', '2': '2', '5': '5'}
    
    rotated_str = ""
    for char in reversed(s):
        if char not in mapping:
            return False
        rotated_str += mapping[char]
        
    return rotated_str == s

# 4. Hàm xoay 180 độ một số bất kỳ (trả về chuỗi số sau khi xoay, hoặc None nếu chứa số không xoay được)
def rotate_180(n):
    s = str(n)
    # Định nghĩa tất cả các chữ số có thể xoay được 180 độ hợp lệ để tạo thành chữ số khác
    mapping = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6', '2': '2', '5': '5'}
    
    rotated_str = ""
    for char in reversed(s):
        if char not in mapping:
            return None
        rotated_str += mapping[char]
    return int(rotated_str)


# --- CHƯƠNG TRÌNH CHÍNH (MAIN) ---
if __name__ == "__main__":
    LIMIT = 1000000
    
    print("--- ĐANG XỬ LÝ DỮ LIỆU ---")
    
    # Tạo các danh sách chứa kết quả
    result_a = []
    result_b = []
    result_c = []
    result_d = []
    result_e = []
    
    # Duyệt từ 0 đến dưới 1 triệu
    for i in range(LIMIT):
        # Kiểm tra điều kiện câu a và b
        if is_strobogrammatic(i):
            result_a.append(i)
            if is_prime(i):
                result_b.append(i)
                
        # Kiểm tra điều kiện câu c và d
        if is_strobogrammatic_extended(i):
            result_c.append(i)
            if is_prime(i):
                result_d.append(i)
        
        # Kiểm tra điều kiện câu e
        # Không phải strobogrammatic gốc VÀ không phải số nguyên tố
        if not is_strobogrammatic(i) and not is_prime(i):
            rotated_val = rotate_180(i)
            # Sau khi xoay 180 độ, số mới phải là số nguyên tố
            if rotated_val is not None and is_prime(rotated_val):
                result_e.append(i)

    # --- IN KẾT QUẢ ---
    print("\na.- Các số strobogrammatic nhỏ hơn 1 triệu:")
    print(f"(Có {len(result_a)} số. Ví dụ 20 số đầu): {result_a[:20]}...")

    print("\nb.- Các số nguyên tố strobogrammatic nhỏ hơn 1 triệu:")
    print(result_b)

    print("\nc.- Các số strobogrammatic mở rộng nhỏ hơn 1 triệu:")
    print(f"(Có {len(result_c)} số. Ví dụ 20 số đầu): {result_c[:20]}...")

    print("\nd.- Các số nguyên tố strobogrammatic mở rộng nhỏ hơn 1 triệu:")
    print(result_d)

    print("\ne.- Các số không phải strobogrammatic, không phải số nguyên tố nhưng xoay 180 độ thành số nguyên tố:")
    print(f"(Có {len(result_e)} số. Ví dụ 20 số đầu): {result_e[:20]}...")