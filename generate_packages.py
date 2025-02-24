import os

repo_path = "debs"
packages_file = "Packages"

if not os.path.exists(repo_path):
    print(f"❌ Lỗi: Thư mục {repo_path} không tồn tại!")
    exit()

deb_files = [f for f in os.listdir(repo_path) if f.endswith(".deb")]

if not deb_files:
    print("⚠️ Không tìm thấy file .deb nào trong thư mục debs/!")
    exit()

with open(packages_file, "w") as f:
    for deb in deb_files:
        size = os.path.getsize(os.path.join(repo_path, deb))
        f.write(f"Filename: debs/{deb}\nSize: {size}\n\n")

print("✅ Packages file created!")
