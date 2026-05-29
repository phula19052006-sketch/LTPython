def is_prime(n):
    if n <= 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
# Ý 1: In bảng cửu chương từ a đến b (hoặc b đến a)
def bang_cuu_chuong():
    raw_input = input("Nhập 2 số nguyên a, b cách nhau bởi dấu phẩy: ")
    a, b = map(int, raw_input.split(','))
    
    start = min(a, b)
    end = max(a, b)
    
    for i in range(start, end + 1):
        print(f"--- Bảng cửu chương {i} ---")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print()

# Ý 2: Liệt kê các số nguyên tố < n
def cu_phap_liet_ke_snt():
    n = int(input("Nhập số nguyên dương n để tìm các SNT nhỏ hơn n: "))
    primes = [i for i in range(2, n) if is_prime(i)]
    print(f"Các số nguyên tố nhỏ hơn {n} là: {primes}")

# Ý 3: Liệt kê ước số của n và lọc ra ước số là nguyên tố 
def uoc_so_nguyen_to():
    n = int(input("Nhập số nguyên dương n để tìm ước là SNT:"))
    all_divisors = [i for i in range(1, n + 1) if n % i == 0]
    prime_divisors = [i for i in all_divisors if is_prime(i)]
    print(f"Các ước số của {n} gồm: {all_divisors}")
    print(f"Các ước số vừa là số nguyên tố: {prime_divisors}")
if __name__ == "__main__":
    bang_cuu_chuong()
    print("="*30)
    cu_phap_liet_ke_snt()
    print("="*30)
    uoc_so_nguyen_to()


