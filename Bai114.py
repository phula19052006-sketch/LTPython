import math

def dao_nguoc(n):
    # Chuyển số thành chuỗi, đảo ngược, rồi chuyển lại thành số
    return int(str(n)[::-1])

def giai_bai_114():
    print("--- CHƯƠNG TRÌNH TÌM SỐ THÂN THIỆN ---")
    try:
        # Nhập a và b (nhập từng số để tránh lỗi)
        a = int(input("Nhập số a: "))
        b = int(input("Nhập số b: "))
        
        # Đảm bảo a <= b, nếu không thì đảo lại
        if a > b:
            a, b = b, a
            
        danh_sach = []
        
        # Duyệt từ a đến b
        for i in range(a, b + 1):
            so_dao = dao_nguoc(i)
            # Nếu Ước chung lớn nhất của i và số đảo ngược là 1
            if math.gcd(i, so_dao) == 1:
                danh_sach.append(i)
        
        # In kết quả
        print("\nCác số thân thiện tìm được:")
        # In các số cách nhau bởi dấu cách
        print(*(danh_sach))
        
        print(f"\nSố lượng số thân thiện: {len(danh_sach)}")
        
    except ValueError:
        print("Lỗi: Bạn phải nhập vào số nguyên dương!")

if __name__ == "__main__":
    giai_bai_114()