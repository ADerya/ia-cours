from src.image_processor import ImageProcessor

if __name__ == "__main__":
    path_images = "input_images"
    target_size = 640
    processor = ImageProcessor(path_images)
    processor.process_folder(target_size)
