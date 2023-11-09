import logging
import sys
import tkinter as tk
from tkinter import filedialog, messagebox, StringVar, OptionMenu, ttk
import subprocess
import os

# 配置日志记录器
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
logger = logging.getLogger(__name__)

def update_progressbar(progressbar, value):
    progressbar['value'] = value
    root.update_idletasks()  # 更新GUI

def convert_to_ebook(pdf_file_paths, output_format):
    total_files = len(pdf_file_paths)
    progressbar['maximum'] = total_files  # 设置进度条的最大值

    for index, pdf_file_path in enumerate(pdf_file_paths, start=1):
        ebook_file_path = os.path.splitext(pdf_file_path)[0] + output_format
        ebook_convert_path = 'C:\\Program Files\\Calibre2\\ebook-convert'  # 替换为您的ebook-convert实际路径

        try:
            subprocess.run([ebook_convert_path, pdf_file_path, ebook_file_path], check=True)
            messagebox.showinfo("转换成功", f"文件已转换并保存为：{ebook_file_path}")
            update_progressbar(progressbar, index)

        except subprocess.CalledProcessError as e:
            logger.error(f"文件转换失败：{e}")
            messagebox.showerror("转换失败", f"文件转换失败：{e}")


def select_pdfs_and_convert():
    # 让用户选择多个PDF文件
    pdf_file_paths = filedialog.askopenfilenames(
        title="选择PDF文件",
        filetypes=[("PDF 文件", "*.pdf")]
    )

    # 如果用户没有选择文件就退出
    if not pdf_file_paths:
        return

    # 获得用户选择的格式
    selected_format = format_var.get()
    convert_to_ebook(pdf_file_paths, selected_format)

# 创建主窗口
root = tk.Tk()
root.title("PDF 批量转 eBook 转换器")

# 创建格式选择变量和下拉菜单
format_var = StringVar(root)
format_var.set(".mobi")  # 设置默认值
format_options = [".mobi", ".epub"]
format_menu = OptionMenu(root, format_var, *format_options)
format_menu.pack()

# 创建一个按钮让用户选择PDF文件并进行转换
select_button = tk.Button(root, text="选择PDF文件并批量转换", command=select_pdfs_and_convert)
select_button.pack(expand=True)

# 创建一个选项卡来显示进度条
tab1 = tk.Notebook(root)
tab1.pack(expand=True)

# 创建一个子框架来显示进度条
frame1 = tk.Frame(tab1)
tab1.add(frame1, text="进度")

# 创建进度条
progressbar = ttk.Progressbar(frame1, orient='horizontal', length=200, mode='determinate')
progressbar.pack(expand=True)

# 启动GUI事件循环
root.mainloop()