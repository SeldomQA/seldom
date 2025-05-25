import inspect
import os
from pathlib import Path

try:
    from PIL import Image, ImageChops
except ModuleNotFoundError as e:
    raise ModuleNotFoundError("Please install the library. https://python-pillow.github.io")
from seldom.logging import log


def save_screenshot(page, file_path: str) -> None:
    """
    Capture and save a screenshot.

    :param page: Playwright or Selenium page object
    :param file_path: Path where the screenshot will be saved
    """
    if hasattr(page, 'screenshot'):
        page.screenshot(path=file_path)
    else:
        page.save_screenshot(file_path)


def compare_images(img1_path: str, img2_path: str, tolerance: int = 0) -> bool:
    """
    Compare two images and return True if they are the same, False otherwise.

    :param img1_path: Path of the first image
    :param img2_path: Path of the second image
    :param tolerance: Allowed pixel difference (default is 0)
    :return: True if images are the same, False if they are different
    """
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)

    if img1.size != img2.size:
        return False

    diff = ImageChops.difference(img1, img2)
    bbox = diff.getbbox()

    if bbox:
        if tolerance > 0:
            diff_data = diff.getdata()
            diff_count = sum(1 for pixel in diff_data if any(i > tolerance for i in pixel))
            if diff_count / len(diff_data) < tolerance:
                return True
        return False
    return True


def assert_screenshot(page, tolerance: int = 0, stack_t=None) -> bool | None:
    """
    Automatically capture a screenshot and compare it with the baseline image.

    :param page: Playwright or Selenium page object
    :param tolerance: Allowed pixel difference for comparison (default is 0)
    :param stack_t: Time to wait before comparing again
    :raises AssertionError: If images do not match
    """
    ins = inspect.getframeinfo(stack_t[1][0])
    file_path = Path(ins.filename).resolve()

    scr_dir = os.path.join(file_path.parent, "reports", "screenshots")
    if os.path.exists(scr_dir) is False:
        os.mkdir(scr_dir)

    file_name = file_path.stem
    class_name = stack_t[1][0].f_locals.get('self').__class__.__name__
    method_name = stack_t[1][3]

    base_img_name = f"{file_name}.py_{class_name}_{method_name}_base.png"
    diff_img_name = f"{file_name}.py_{class_name}_{method_name}_diff.png"
    base_img_path = os.path.join(scr_dir, base_img_name)
    diff_img_path = os.path.join(scr_dir, diff_img_name)

    if not os.path.exists(base_img_path):
        save_screenshot(page, base_img_path)
        log.info(f"Generate the base image file: {base_img_path}")
        return None
    else:
        if os.path.exists(diff_img_path):
            os.remove(diff_img_path)

        save_screenshot(page, diff_img_path)
        log.info(f"Generate the diff image file: {diff_img_path}")

        if not compare_images(base_img_path, diff_img_path, tolerance):
            log.error(f"Image assertion failed: {base_img_name} and {diff_img_name} are different")
            return False
        else:
            log.info(f"Image assertion passed: {base_img_name} and {diff_img_name} match")
            return True
