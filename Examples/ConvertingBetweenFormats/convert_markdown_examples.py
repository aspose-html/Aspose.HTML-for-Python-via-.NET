import os
import aspose.html.converters as conv
import aspose.html.saving as sav
import aspose.html.drawing as dr
import aspose.html.rendering.image as rim
import aspose.pydrawing as pd

class MarkdownExamples:
    def test_md_to_docx_with_save_options(self):
        #ExStart:MdToDocxOptions
        output_dir = "output/"
        input_dir = "data/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(input_dir, "document.md")
        save_path = os.path.join(output_dir, "md-to-docx-with-save-options.docx")
        document = conv.Converter.convert_markdown(document_path)
        options = sav.DocSaveOptions()
        options.page_setup.any_page = dr.Page(dr.Size(900, 700), dr.Margin(40, 10, 10, 10))
        options.document_format.DOCX
        options.font_embedding_rule.FULL
        conv.Converter.convert_html(document, options, save_path)
        #ExEnd:MdToDocxOptions

    def test_md_to_docx(self):
        #ExStart:MdToDocx
        document = conv.Converter.convert_markdown("document.md")
        options = sav.DocSaveOptions()
        conv.Converter.convert_html(document, options, "document.docx")
        #ExEnd:MdToDocx

    def test_md_to_html(self):
        #ExStart:MdToHtml
        document = conv.Converter.convert_markdown("document.md", "md-to-html.html")
        #ExEnd:MdToHtml

    def test_md_to_html1(self):
        #ExStart:MdToHtml1
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        source_path = os.path.join(output_dir, "document.md")
        code = "### Hello, World!\\nConvert Markdown to HTML!"
        with open(source_path, "w", encoding="utf-8") as file:
            file.write(code)
        save_path = os.path.join(output_dir, "document-output.html")
        conv.Converter.convert_markdown(source_path, save_path)
        #ExEnd:MdToHtml1

    def test_md_to_jpg_with_save_options(self):
        #ExStart:MdToJpgOptions
        output_dir = "output/"
        input_dir = "data/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(input_dir, "document.md")
        save_path = os.path.join(output_dir, "md-to-jpg-with-save-options.jpg")
        document = conv.Converter.convert_markdown(document_path)
        options = sav.ImageSaveOptions(rim.ImageFormat.JPEG)
        options.horizontal_resolution = dr.Resolution.from_dots_per_inch(150.0)
        options.vertical_resolution = dr.Resolution.from_dots_per_inch(150.0)
        options.css.media_type.PRINT
        conv.Converter.convert_html(document, options, save_path)
        #ExEnd:MdToJpgOptions

    def test_md_to_jpg(self):
        #ExStart:MdToJpg
        document = conv.Converter.convert_markdown("document.md")
        options = sav.ImageSaveOptions(rim.ImageFormat.JPEG)
        conv.Converter.convert_html(document, options, "output.jpeg")
        #ExEnd:MdToJpg

    def test_md_to_pdf_with_save_options(self):
        #ExStart:MdToPdfOptions
        output_dir = "output/"
        input_dir = "data/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(input_dir, "document.md")
        save_path = os.path.join(output_dir, "md-to-pdf-with-save-options.pdf")
        document = conv.Converter.convert_markdown(document_path)
        options = sav.PdfSaveOptions()
        options.page_setup.any_page = dr.Page(dr.Size(300, 300), dr.Margin(30, 10, 10, 10))
        options.css.media_type.PRINT
        options.jpeg_quality = 100
        conv.Converter.convert_html(document, options, save_path)
        #ExEnd:MdToPdfOptions

    def test_md_to_pdf(self):
        #ExStart:MdToPdf
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        source_path = os.path.join(output_dir, "document.md")
        save_path = os.path.join(output_dir, "markdown-to-pdf.pdf")
        code = "### Hello, World!\\nConvert Markdown to PDF!"
        with open(source_path, "w") as file:
            file.write(code)
        document = conv.Converter.convert_markdown(source_path)
        options = sav.PdfSaveOptions()
        conv.Converter.convert_html(document, options, save_path)
        #ExEnd:MdToPdf

    def test_md_to_png_with_save_options(self):
        #ExStart:MdToPngOptions
        output_dir = "output/"
        input_dir = "data/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(input_dir, "document.md")
        save_path = os.path.join(output_dir, "md-to-png-with-save-options.png")
        document = conv.Converter.convert_markdown(document_path)
        options = sav.ImageSaveOptions()
        options.page_setup.any_page = dr.Page(dr.Size(500, 500), dr.Margin(40, 10, 10, 10))
        options.horizontal_resolution = dr.Resolution.from_dots_per_inch(150.0)
        options.vertical_resolution = dr.Resolution.from_dots_per_inch(150.0)
        options.background_color = pd.Color.bisque
        conv.Converter.convert_html(document, options, save_path)
        #ExEnd:MdToPngOptions

    def test_md_to_png(self):
        #ExStart:MdToPng
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        source_path = os.path.join(output_dir, "document.md")
        code = "### Hello, World!\\nConvert Markdown to PNG!"
        with open(source_path, "w") as file:
            file.write(code)
        document = conv.Converter.convert_markdown(source_path)
        options = sav.ImageSaveOptions()
        save_path = os.path.join(output_dir, "markdown-to-image.png")
        conv.Converter.convert_html(document, options, save_path)
        #ExEnd:MdToPng

    def test_md_to_xps_with_save_options(self):
        #ExStart:MdToXpsOptions
        output_dir = "output/"
        input_dir = "data/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(input_dir, "document.md")
        save_path = os.path.join(output_dir, "md-to-xps-with-save-options.xps")
        document = conv.Converter.convert_markdown(document_path)
        options = sav.XpsSaveOptions()
        options.page_setup.any_page = dr.Page(dr.Size(300, 300), dr.Margin(30, 10, 10, 10))
        options.css.media_type.PRINT
        conv.Converter.convert_html(document, options, save_path)
        #ExEnd:MdToXpsOptions

if __name__ == "__main__":
    tests = MarkdownExamples()
    tests.test_md_to_docx_with_save_options()
    tests.test_md_to_docx()
    tests.test_md_to_html()
    tests.test_md_to_html1()
    tests.test_md_to_jpg_with_save_options()
    tests.test_md_to_jpg()
    tests.test_md_to_pdf_with_save_options()
    tests.test_md_to_pdf()
    tests.test_md_to_png_with_save_options()
    tests.test_md_to_png()
    tests.test_md_to_xps_with_save_options()
    print("✅ Files created successfully.")