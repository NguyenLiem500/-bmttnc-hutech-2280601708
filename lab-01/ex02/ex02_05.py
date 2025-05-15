so_gio_lam=float(input("nhập số giờ làm mỗi tuần: "))
luong_gio=float(input("Nhập số thù lao trên mỗ giờ làm tiêu chuẩn: "))
Gio_tieu_chuan=44
gio_vuot_chuan=max(0, so_gio_lam - Gio_tieu_chuan)
thuc_linh= Gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5
print(f"số tiền thực lĩnh của nhân viên: {thuc_linh}")