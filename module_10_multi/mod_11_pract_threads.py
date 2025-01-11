import multiprocessing as mp
from PIL import Image


def resize_image(image_paths, queue):
    for image_path in image_paths:
        image = Image.open(image_path)
        image = image.resize((800,600))
        queue.put((image_path, image))

def change_color(queue):
    while True:
        try:
            image_path, image = queue.get(timeout=5)
        except Exception as err:
            break
        image = image.convert('L')
        image.save(image_path)

if __name__ == '__main__':
    data = []
    queue = mp.Queue()
    for image in range(1,12):
        data.append(f'./images/00{image}.png')

    resize_proc = mp.Process(target=resize_image, args=(data, queue,))
    change_proc = mp.Process(target=change_color, args=(queue,))

    resize_proc.start()
    change_proc.start()

    resize_proc.join()
    change_proc.join()


try:
    print('')
except Exception as err:
    pass
finally:
    print('')
