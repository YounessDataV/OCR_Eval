# https://www.geeksforgeeks.org/how-to-extract-images-from-pdf-in-python/
import pathlib
import fitz

if __name__ == "__main__":

    image_pdf = pathlib.Path("/media/ml/Document 3.pdf")
    text_pdf = pathlib.Path("/media/ml/fables.pdf")

    images_path = pathlib.Path('data/images')
    truth_path = pathlib.Path('data/truth')

    images_path.mkdir(parents=True, exist_ok=True)
    truth_path.mkdir(parents=True, exist_ok=True)

    pdf_file = fitz.open(image_pdf)

    for page_index in range(len(pdf_file)):

        page = pdf_file[page_index]
        image_list = page.getImageList()
        image = image_list[0]

        xref = image[0]

        base_image = pdf_file.extractImage(xref)

        image_bytes = base_image["image"]
        image_ext = base_image["ext"]

        with open(images_path / f"Sample_{page_index}.{image_ext}", "wb") as f:
            f.write(image_bytes)

    pdf_file = fitz.open(text_pdf)

    for page_index in range(len(pdf_file)):

        page = pdf_file[page_index]

        text = page.getText()

        with open(truth_path / f"Sample_{page_index}.txt", "w") as f:
            f.write(text)
