def khoi_phuc_chuoi(cipher_text):
    plain_text = ""
    i = 0
    while i < len(cipher_text):
        # Nếu gặp ký tự đặc biệt #
        if cipher_text[i] == '#':
            # Lấy số lượng (nằm ngay sau #)
            so_luong = int(cipher_text[i+1])
            # Lấy ký tự cần lặp (nằm sau con số)
            ky_tu = cipher_text[i+2]
            
            # Cộng chuỗi đã lặp vào kết quả
            plain_text += ky_tu * so_luong
            
            # Nhảy qua 3 ký tự vừa xử lý (#, số, ký tự)
            i += 3
        else:
            # Nếu là ký tự bình thường, chỉ việc cộng vào
            plain_text += cipher_text[i]
            i += 1
            
    return plain_text

# Chạy thử nghiệm
print("--- CHƯƠNG TRÌNH KHÔI PHỤC CHUỖI ---")
input_cipher = input("Nhập chuỗi nén (cipher text): ")
result = khoi_phuc_chuoi(input_cipher)

print(f"Chuỗi gốc (plain text): {result}")