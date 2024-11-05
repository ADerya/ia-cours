import os
from datetime import datetime
from PIL import Image, ImageOps


class ImageProcessor:

    def __init__(self, path: str) -> None:
        self._path = path

    def process_folder(self, target_size: int) -> None:
        """
        Processes all image files in the folder, resizes the target size, and adds padding

        Args:
            target_size: dimension for the output image

        Returns:

        """
        unique_id = datetime.now().strftime("%Y%m%d%H%M%S")
        output_folder = f"datasets/{unique_id}"

        try:
            os.makedirs(output_folder, exist_ok=True)
        except OSError as e:
            print(f"An error occurred while creating the folder : {e}")

        for name_file in os.listdir(self._path):
            image_path = os.path.join(self._path, name_file)
            if os.path.isfile(image_path):
                self._process_image(image_path, output_folder, target_size)

    def _process_image(
        self, image_path: str, output_folder: str, target_size: int
    ) -> None:
        """
        Resizes an image with the target size and adds padding

        Args:
            image_path: Path to the image
            output_folder: Directory where the resized image will be saved
            target_size: Dimension for the output image

        Returns:

        """
        img = Image.open(image_path)

        try:
            new_width, new_height = self._calculate_new_dimensions(img, target_size)
            image_resized = img.resize((new_width, new_height))
            image_with_padding = self._add_padding_for_image(
                image_resized, target_size, img.mode
            )
            self._save_image(image_with_padding, output_folder, image_path)

        finally:
            img.close()

    def _add_padding_for_image(
        self, image_resized: Image.Image, target_size: int, mode: str
    ) -> Image.Image:
        """
        Adds padding to the resized image to make it square

        Args:
            image_resized: Resized image
            target_size: Dimension for the output image
            mode: Image mode to determine the fill color

        Returns:
            Image.Image: The image with padding added

        """
        fill_color = self._get_fill_color(mode)
        padding_width = target_size - image_resized.width
        padding_height = target_size - image_resized.height
        padding = (0, 0, padding_width, padding_height)
        image_resized = ImageOps.expand(image_resized, padding, fill_color)
        return image_resized

    @staticmethod
    def _calculate_new_dimensions(img, target_size) -> tuple[int, int]:
        """
        Calculates the new dimensions for resizing based on the ratio's image

        Args:
            img: Image to resize
            target_size: Dimension for the output image

        Returns:
            tuple: New width and height for the resized image

        """
        ratio = img.width / img.height
        if img.width > img.height:
            # Image wider than tall: add padding at bottom
            new_width = target_size
            new_height = int(target_size / ratio)

        else:
            # Image taller than wide: add padding to right
            new_width = int(target_size * ratio)
            new_height = target_size
        return new_width, new_height

    @staticmethod
    def _get_fill_color(mode: str) -> tuple[int, int, int] | int:
        """
        Determines the padding color based on the image mode

        Args:
            mode: image mode (RGB or L for black and white image)

        Returns:
            tuple or integer representing the fill color for padding

        """
        return (114, 114, 144) if mode == "RGB" else 114

    @staticmethod
    def _save_image(image: Image.Image, output_folder: str, image_path: str) -> None:
        """
        Saves the new image to the output folder

        Args:
            image: image to save
            output_folder: directory where new image will be saved
            image_path: original path of image

        Returns:

        """
        final_path = os.path.join(output_folder, os.path.basename(image_path))
        image.save(final_path)
