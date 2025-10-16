import os
import aspose.html.converters as conv
import aspose.html.saving as sav
import aspose.html.drawing as dr
import aspose.html.rendering.image as rim
import aspose.pydrawing as pd

class MhtmlExamples:
    def test_mhtml_to_docx_with_save_options(self):
        #ExStart:MhtmlToDocxOptions
        output_dir = "output/"
        input_dir = "data/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(input_dir, "document.mht")
        save_path = os.path.join(output_dir, "document.docx")
        with open(document_path, "rb") as stream:
            options = sav.DocSaveOptions()
            options.page_setup.any_page.size = dr.Size(1000, 800)
            options.document_format.DOCX
            options.css.media_type.SCREEN
            conv.Converter.convert_mhtml(stream, options, save_path)
        #ExEnd:MhtmlToDocxOptions

    def test_mhtml_to_jpg_with_save_options(self):
        #ExStart:MhtmlToJpgOptions
        output_dir = "output/"
        input_dir = "data/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(input_dir, "document.mht")
        save_path = os.path.join(output_dir, "mhtml-to-image.jpg")
        with open(document_path, "rb") as stream:
            options = sav.ImageSaveOptions(rim.ImageFormat.JPEG)
            options.horizontal_resolution = dr.Resolution.from_dots_per_inch(200.0)
            options.vertical_resolution = dr.Resolution.from_dots_per_inch(200.0)
            options.css.media_type.SCREEN
            options.text.use_hinting = True
            conv.Converter.convert_mhtml(stream, options, save_path)
        #ExEnd:MhtmlToJpgOptions

    def test_mhtml_to_jpg(self):
        #ExStart:MhtmlToJpg
        with open("document.mht", "rb") as stream:
            options = sav.ImageSaveOptions(rim.ImageFormat.JPEG)
            conv.Converter.convert_mhtml(stream, options, "document.jpeg")
        #ExEnd:MhtmlToJpg

    def test_mhtml_to_pdf_with_save_options(self):
        #ExStart:MhtmlToPdfOptions
        output_dir = "output/"
        input_dir = "data/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(input_dir, "document.mht")
        save_path = os.path.join(output_dir, "document.pdf")
        with open(document_path, "rb") as stream:
            options = sav.PdfSaveOptions()
            options.page_setup.any_page.size = dr.Size(800, 600)
            options.css.media_type.PRINT
            options.jpeg_quality = 100
            conv.Converter.convert_mhtml(stream, options, save_path)
        #ExEnd:MhtmlToPdfOptions

    def test_mhtml_to_pdf(self):
        #ExStart:MhtmlToPdf
        with open("document.mht", "rb") as stream:
            options = sav.PdfSaveOptions()
            conv.Converter.convert_mhtml(stream, options, "document.pdf")
        #ExEnd:MhtmlToPdf

    def test_mhtml_to_png_with_save_options(self):
        #ExStart:MhtmlToPngOptions
        output_dir = "output/"
        input_dir = "data/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(input_dir, "document.mht")
        save_path = os.path.join(output_dir, "mhtml-to-image.png")
        with open(document_path, "rb") as stream:
            options = sav.ImageSaveOptions()
            options.page_setup.any_page.size = dr.Size(800, 600)
            options.page_setup.any_page.margin = dr.Margin(40, 40, 20, 20)
            options.css.media_type.PRINT
            conv.Converter.convert_mhtml(stream, options, save_path)
        #ExEnd:MhtmlToPngOptions

    def test_mhtml_to_xps_with_save_options(self):
        #ExStart:MhtmlToXpsOptions
        output_dir = "output/"
        input_dir = "data/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(input_dir, "document.mht")
        save_path = os.path.join(output_dir, "document.xps")
        with open(document_path, "rb") as stream:
            options = sav.XpsSaveOptions()
            options.page_setup.any_page.size = dr.Size(600, 600)
            options.page_setup.any_page.margin = dr.Margin(20, 20, 10, 10)
            options.css.media_type.PRINT
            conv.Converter.convert_mhtml(stream, options, save_path)
        #ExEnd:MhtmlToXpsOptions

if __name__ == "__main__":
    tests = MhtmlExamples()
    tests.test_mhtml_to_docx_with_save_options()
    tests.test_mhtml_to_jpg_with_save_options()
    tests.test_mhtml_to_jpg()
    tests.test_mhtml_to_pdf_with_save_options()
    tests.test_mhtml_to_pdf()
    tests.test_mhtml_to_png_with_save_options()
    tests.test_mhtml_to_xps_with_save_options()
    print("✅ Files created successfully.")