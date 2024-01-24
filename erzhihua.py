import cv2
import os

def batch_binarize(input_folder, output_folder, threshold=127):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 获取输入文件夹中的所有图片文件
    image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

    # 遍历每张图片进行二值化
    for image_file in image_files:
        input_path = os.path.join(input_folder, image_file)
        output_path = os.path.join(output_folder, image_file)

        # 读取图片
        img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

        # 二值化处理
        _, inverted_binary_img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)

        # 保存二值化后的图片
        cv2.imwrite(output_path, inverted_binary_img)

if __name__ == "__main__":
    # 输入文件夹路径（包含要处理的图片）
    input_folder = './dataset/GLAS/test/labelcol'

    # 输出文件夹路径（保存处理后的图片）
    output_folder = './tran/test'

    # 二值化阈值（可根据需要调整）
    threshold_value = 0

    # 执行批量二值化
    batch_binarize(input_folder, output_folder, threshold_value)