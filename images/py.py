from PIL import Image

def resize_and_overwrite_image(image_path):
    # 打开图片
    with Image.open(image_path) as img:
        # 调整图片大小至720x720
        resized_img = img.resize((720, 720))
        
        # 覆盖原始图片
        resized_img.save('/Users/ivanlee/Desktop/lowestbuaaer.github.io/images/my1.png')

# 输入图片地址
image_path = '/Users/ivanlee/Desktop/lowestbuaaer.github.io/images/my.png'
resize_and_overwrite_image(image_path)

print(f"Image '{image_path}' has been resized to 720x720 and overwritten.")
