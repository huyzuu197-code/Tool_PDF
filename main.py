import fitz  # PyMuPDF
import os
 
def xu_ly_pdf_A4_A3():
    input_folder = os.getcwd()
    output_folder = os.path.join(input_folder, "KET_QUA_GOM_FILE")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
 
    files = [f for f in os.listdir(input_folder) if f.lower().endswith(".pdf")]
    file_a4 = next((f for f in files if "(A4)" in f), None)
    file_a3 = next((f for f in files if "(A3)" in f), None)
 
    page_counter = 1
    blue = (0, 0, 1)
 
    # =========================
    # 1. XỬ LÝ FILE A4
    # =========================
    if file_a4:
        doc = fitz.open(os.path.join(input_folder, file_a4))
 
        for page in doc:
            rect = page.rect
 
            # BƯỚC 1: Xoay counterclockwise nếu trang ngang
            if rect.width > rect.height:
                # CCW = 90
                page.set_rotation((page.rotation + 90) % 360)
 
            # Lấy lại rect sau khi xoay
            rect = page.rect
 
            # BƯỚC 2: Đánh số trang – Right Footer
            text = f"Page {page_counter}"
            pos = fitz.Point(rect.width - 100, rect.height - 40)
 
            page.insert_text(
                pos,
                text,
                fontsize=11,
                fontname="helv",
                color=blue,
                overlay=True
            )
 
            page_counter += 1
 
        doc.save(os.path.join(output_folder, f"Checked_{file_a4}"))
        doc.close()
 
    # =========================
    # 2. XỬ LÝ FILE A3
    # =========================
    if file_a3:
        doc = fitz.open(os.path.join(input_folder, file_a3))
 
        for page in doc:
            rect = page.rect
 
            # KHÔNG XOAY – CHỈ ĐÁNH SỐ
            text = f"Page {page_counter}"
            pos = fitz.Point(rect.width - 130, rect.height - 50)
 
            page.insert_text(
                pos,
                text,
                fontsize=13,
                fontname="helv",
                color=blue,
                overlay=True
            )
 
            page_counter += 1
 
        doc.save(os.path.join(output_folder, f"Checked_{file_a3}"))
        doc.close()
 
 
if __name__ == "__main__":
    xu_ly_pdf_A4_A3()
