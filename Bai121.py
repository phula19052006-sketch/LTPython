def generate_strobogrammatic(n, pairs, is_final=True):
    # Các chữ số có thể nằm ở giữa nếu n là số lẻ (chỉ lấy các số tự đối xứng)
    self_rotating = [d for d, r in pairs.items() if d == r]
    
    def helper(m):
        if m == 0:
            return [""]
        if m == 1:
            return self_rotating
        
        inner_list = helper(m - 2)
        res = []
        for inner in inner_list:
            for left, right in pairs.items():
                # Không được để số 0 ở đầu (nếu là lớp ngoài cùng)
                if left == "0" and m == n:
                    continue
                res.append(left + inner + right)
        return res

    return sorted(helper(n), key=lambda x: int(x))

# --- Chương trình chính ---
try:
    n = int(input("Nhập số nguyên n (2 <= n <= 10): "))
    if 2 <= n <= 10:
        # a. Cấu hình cặp cho số Strobogrammatic cơ bản
        pairs_a = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        result_a = generate_strobogrammatic(n, pairs_a)
        
        # b. Cấu hình cặp cho số Strobogrammatic mở rộng
        # (Thêm 2 và 5 theo quy tắc tự đối xứng của font digital)
        pairs_b = {'0': '0', '1': '1', '2': '2', '5': '5', '8': '8', '6': '9', '9': '6'}
        result_b = generate_strobogrammatic(n, pairs_b)

        print(f"\na.- Tất cả các số strobogrammatic gồm {n} chữ số:")
        print(f"Số lượng tìm thấy: {len(result_a)}")
        print(", ".join(result_a))

        print(f"\nb.- Tất cả các số strobogrammatic mở rộng gồm {n} chữ số:")
        print(f"Số lượng tìm thấy: {len(result_b)}")
        print(", ".join(result_b))
    else:
        print("Vui lòng nhập n trong khoảng từ 2 đến 10.")
except ValueError:
    print("Dữ liệu nhập vào không hợp lệ.")