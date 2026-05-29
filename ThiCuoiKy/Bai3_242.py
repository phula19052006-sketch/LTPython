# Ý 1: Kiểm tra bội số của 13 hoặc 19
def check_boi_so(n):
    return n % 13 == 0 or n % 19 == 0

# Ý 2: Kiểm tra loại tam giác
def check_tam_giac(a, b, c):
    # Điều kiện tồn tại tam giác
    if a + b > c and a + c > b and b + a > c:
        # Kiểm tra tam giác đều
        if a == b == c:
            return "Tam giác đều"
        
        # Kiểm tra tam giác vuông (Sử dụng định lý Pytago đảo)
        # Sử dụng làm tròn để tránh sai số số thực (nếu a, b, c là float)
        is_vuong = (round(a**2 + b**2, 2) == round(c**2, 2) or 
                    round(a**2 + c**2, 2) == round(b**2, 2) or 
                    round(b**2 + c**2, 2) == round(a**2, 2))
        
        # Kiểm tra tam giác cân
        is_can = (a == b or b == c or a == c)
        
        if is_vuong and is_can:
            return "Tam giác vuông cân"
        elif is_vuong:
            return "Tam giác vuông"
        elif is_can:
            return "Tam giác cân"
        else:
            return "Tam giác thường"
    else:
        return "Không phải là 3 cạnh của một tam giác"

if __name__ == "__main__":
    # Test thử hàm bội số
    n = int(input("Nhập n cần kiểm tra bội 13/19: "))
    print(f"Kết quả kiểm tra bội số: {check_boi_so(n)}")
    
    # Test thử hàm tam giác
    print("\n--- Kiểm tra tam giác ---")
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))
    print(f"Kết quả: {check_tam_giac(a, b, c)}")