# Danh sách các mệnh giá tiền
menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]

x = int(input("Nhập số tiền X: "))
so_tien_ban_dau = x
tong_so_to = 0

print(f"\nSo tien {so_tien_ban_dau} duoc doi thanh:")

for gia in menh_gia:
    so_to = x // gia
    x = x % gia
    tong_so_to += so_to
    print(f"Loai {gia} gom {so_to} to")

print(f"TONG CONG CO {tong_so_to} TO")