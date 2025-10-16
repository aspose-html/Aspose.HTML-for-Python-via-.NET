import os
import aspose.html.converters as conv
import aspose.html.saving as sav
import aspose.html.drawing as dr
import aspose.pydrawing as pd
import aspose.html.rendering.image as rim

class EpubExamples:
    def test_epub_to_docx_with_save_options(self):
        #ExStart:EpubToDocxOptions
        output_dir = "output/"
        input_dir = "data/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(input_dir, "input.epub")
        save_path = os.path.join(output_dir, "epub-to-docx.docx")
        with open(document_path, "rb") as stream:
            options = sav.DocSaveOptions()
            options.page_setup.any_page = dr.Page(dr.Size(900, 700), dr.Margin(10, 10, 10, 10))
            options.font_embedding_rule.FULL
            options.document_format.DOCX
            options.css.media_type.SCREEN
            conv.Converter.convert_epub(stream, options, save_path)
        #ExEnd:EpubToDocxOptions

    def test_epub_to_docx(self):
        #ExStart:EpubToDocx
        with open("input.epub", "rb") as stream:
            options = sav.DocSaveOptions()
            conv.Converter.convert_epub(stream, options, "output.docx")
        #ExEnd:EpubToDocx

    def test_epub_to_jpg_with_save_options(self):
        #ExStart:EpubToJpgOptions
        output_dir = "output/"
        input_dir = "data/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(input_dir, "input.epub")
        save_path = os.path.join(output_dir, "epub-to-image.jpg")
        with open(document_path, "rb") as stream:
            options = sav.ImageSaveOptions(rim.ImageFormat.JPEG)
            options.horizontal_resolution = dr.Resolution.from_dots_per_inch(150.0)
            options.vertical_resolution = dr.Resolution.from_dots_per_inch(150.0)
            options.background_color = pd.Color.bisque
            options.page_setup.any_page.size = dr.Size(500, 1000)
            conv.Converter.convert_epub(stream, options, save_path)
        #ExEnd:EpubToJpgOptions

    def test_epub_to_jpg(self):
        #ExStart:EpubToJpg
        with open("input.epub", "rb") as stream:
            options = sav.ImageSaveOptions(rim.ImageFormat.JPEG)
            conv.Converter.convert_epub(stream, options, "output.jpg")
        #ExEnd:EpubToJpg

    def test_epub_to_pdf_with_save_options(self):
        #ExStart:EpubToPdfOptions
        output_dir = "output/"
        input_dir = "data/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(input_dir, "input.epub")
        save_path = os.path.join(output_dir, "epub-to-pdf.pdf")
        with open(document_path, "rb") as stream:
            options = sav.PdfSaveOptions()
            options.page_setup.any_page = dr.Page(dr.Size(800, 600), dr.Margin(10, 10, 10, 10))
            options.css.media_type.PRINT
            conv.Converter.convert_epub(stream, options, save_path)
        #ExEnd:EpubToPdfOptions

    def test_epub_to_pdf(self):
        #ExStart:EpubToPdf
        with open("input.epub", "rb") as stream:
            options = sav.PdfSaveOptions()
            conv.Converter.convert_epub(stream, options, "output.pdf")
        #ExEnd:EpubToPdf

    def test_epub_to_png_with_save_options(self):
        #ExStart:EpubToPngOptions
        output_dir = "output/"
        input_dir = "data/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(input_dir, "input.epub")
        save_path = os.path.join(output_dir, "epub-to-image.png")
        with open(document_path, "rb") as stream:
            options = sav.ImageSaveOptions()
            options.horizontal_resolution = dr.Resolution.from_dots_per_inch(150.0)
            options.vertical_resolution = dr.Resolution.from_dots_per_inch(150.0)
            options.page_setup.any_page.size = dr.Size(500, 1000)
            options.css.media_type.SCREEN
            options.text.use_hinting = True
            conv.Converter.convert_epub(stream, options, save_path)
        #ExEnd:EpubToPngOptions

    def test_epub_to_xps_with_save_options(self):
        #ExStart:EpubToXpsOptions
        output_dir = "output/"
        input_dir = "data/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(input_dir, "input.epub")
        save_path = os.path.join(output_dir, "output.xps")
        with open(document_path, "rb") as stream:
            options = sav.XpsSaveOptions()
            options.page_setup.any_page = dr.Page(dr.Size(600, 600), dr.Margin(40, 40, 10, 10))
            options.css.media_type.PRINT
            options.background_color = pd.Color.bisque
            conv.Converter.convert_epub(stream, options, save_path)
        #ExEnd:EpubToXpsOptions

if __name__ == "__main__":
    tests = EpubExamples()
    tests.test_epub_to_docx_with_save_options()
    tests.test_epub_to_docx()
    tests.test_epub_to_jpg_with_save_options()
    tests.test_epub_to_jpg()
    tests.test_epub_to_pdf_with_save_options()
    tests.test_epub_to_pdf()
    tests.test_epub_to_png_with_save_options()
    tests.test_epub_to_xps_with_save_options()
    print("✅ Files created successfully.")