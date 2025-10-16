import os
import aspose.html as ah
import aspose.html.converters as conv
import aspose.html.saving as sav
import aspose.html.rendering.pdf as rp
import aspose.html.rendering.image as rim
import aspose.html.drawing as dr
import aspose.pydrawing as pd
import aspose.html.rendering.pdf.encryption as rpe

class ConvertHTMLExamples:
    def test_flatten_pdf(self):
        #ExStart:FlattenPdf
        data_dir = "data/"
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        source_path = os.path.join(data_dir, "SampleHtmlForm.html")
        result_path = os.path.join(output_dir, "form-flattened.pdf")
        doc = ah.HTMLDocument(source_path)
        options = sav.PdfSaveOptions()
        options.form_field_behaviour = rp.FormFieldBehaviour.FLATTENED
        conv.Converter.convert_html(doc, options, result_path)
        #ExEnd:FlattenPdf

    def test_html_to_docx_with_save_options(self):
        #ExStart:HtmlToDocxOptions
        output_dir = "output/"
        input_dir = "data/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(input_dir, "nature.html")
        save_path = os.path.join(output_dir, "nature.docx")
        doc = ah.HTMLDocument(document_path)
        options = sav.DocSaveOptions()
        options.page_setup.any_page.size = dr.Size(1300, 1000)
        options.page_setup.any_page.margin = dr.Margin(0, 0, 10, 10)
        options.document_format.DOCX
        options.font_embedding_rule.FULL
        options.css.media_type.PRINT
        options.horizontal_resolution = dr.Resolution.from_dots_per_inch(300.0)
        options.vertical_resolution = dr.Resolution.from_dots_per_inch(300.0)
        options.background_color = pd.Color.bisque
        conv.Converter.convert_html(doc, options, save_path)
        #ExEnd:HtmlToDocxOptions

    def test_html_to_docx(self):
        #ExStart:HtmlToDocx
        conv.Converter.convert_html("document.html", sav.DocSaveOptions(), "document.docx")
        #ExEnd:HtmlToDocx

    def test_html_to_gif(self):
        #ExStart:HtmlToGif
        output_dir = "output/"
        input_dir = "data/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(input_dir, "document.html")
        save_path = os.path.join(output_dir, "html-to-image.gif")
        document = ah.HTMLDocument(document_path)
        options = sav.ImageSaveOptions(rim.ImageFormat.GIF)
        options.horizontal_resolution = dr.Resolution.from_dots_per_inch(96.0)
        options.vertical_resolution = dr.Resolution.from_dots_per_inch(96.0)
        options.css.media_type.PRINT
        conv.Converter.convert_html(document, options, save_path)
        #ExEnd:HtmlToGif

    def test_html_to_jpg_with_save_options_margins(self):
        #ExStart:HtmlToJpgOptionsMargins
        output_dir = "output/"
        input_dir = "data/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(input_dir, "nature.html")
        save_path = os.path.join(output_dir, "nature.jpg")
        document = ah.HTMLDocument(document_path)
        options = sav.ImageSaveOptions(rim.ImageFormat.JPEG)
        options.horizontal_resolution = dr.Resolution.from_dots_per_inch(50.0)
        options.vertical_resolution = dr.Resolution.from_dots_per_inch(50.0)
        options.background_color = pd.Color.bisque
        options.page_setup.any_page = dr.Page(dr.Size(680, 500), dr.Margin(100, 10, 10, 10))
        options.text.use_hinting = True
        options.compression = rim.Compression.NONE
        options.css.media_type.SCREEN
        conv.Converter.convert_html(document, options, save_path)
        #ExEnd:HtmlToJpgOptionsMargins

    def test_html_to_jpg_with_save_options(self):
        #ExStart:HtmlToJpgOptions
        output_dir = "output/"
        input_dir = "data/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(input_dir, "nature.html")
        save_path = os.path.join(output_dir, "nature.jpg")
        document = ah.HTMLDocument(document_path)
        options = sav.ImageSaveOptions(rim.ImageFormat.JPEG)
        options.horizontal_resolution = dr.Resolution.from_dots_per_inch(50.0)
        options.vertical_resolution = dr.Resolution.from_dots_per_inch(50.0)
        options.background_color = pd.Color.bisque
        options.page_setup.any_page.size = dr.Size(1500, 1000)
        options.use_antialiasing = True
        options.text.use_hinting = True
        options.compression = rim.Compression.NONE
        options.css.media_type.SCREEN
        conv.Converter.convert_html(document, options, save_path)
        #ExEnd:HtmlToJpgOptions

    def test_html_to_jpg(self):
        #ExStart:HtmlToJpg
        document = ah.HTMLDocument("document.html")
        options = sav.ImageSaveOptions(rim.ImageFormat.JPEG)
        conv.Converter.convert_html(document, options, "output.jpeg")
        #ExEnd:HtmlToJpg

    def test_html_to_md_feature(self):
        #ExStart:HtmlToMdFeature
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        save_path = os.path.join(output_dir, "options-output.md")
        code = "<h1>Header 1</h1><h2>Header 2</h2><p>Hello, World!!</p><a href='https://docs.aspose.com/'>aspose</a>"
        with open(os.path.join(output_dir, "options.html"), "w") as file:
            file.write(code)
        options = sav.MarkdownSaveOptions()
        options.features = sav.MarkdownFeatures.LINK | sav.MarkdownFeatures.AUTOMATIC_PARAGRAPH
        conv.Converter.convert_html(os.path.join(output_dir, "options.html"), options, save_path)
        #ExEnd:HtmlToMdFeature

    def test_html_to_md_git(self):
        #ExStart:HtmlToMdGit
        code = "<h1>Header 1</h1><h2>Header 2</h2><p>Hello World!!</p>"
        with open("document.html", "w", encoding="utf-8") as f:
            f.write(code)
        conv.Converter.convert_html("document.html", sav.MarkdownSaveOptions.git, "output.md")
        #ExEnd:HtmlToMdGit

    def test_html_to_md_inline(self):
        #ExStart:HtmlToMdInline
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        save_path = os.path.join(output_dir, "inline-html.md")
        code = "text<div markdown='inline'><code>text</code></div>"
        with open(os.path.join(output_dir, "inline.html"), "w") as file:
            file.write(code)
        conv.Converter.convert_html(os.path.join(output_dir, "inline.html"), sav.MarkdownSaveOptions(), save_path)
        #ExEnd:HtmlToMdInline

    def test_html_to_md(self):
        #ExStart:HtmlToMd
        document = ah.HTMLDocument("document.html")
        options = sav.MarkdownSaveOptions()
        conv.Converter.convert_html(document, options, "output.md")
        #ExEnd:HtmlToMd

    def test_html_to_mhtml_in_one_line(self):
        #ExStart:HtmlToMhtmlOne
        conv.Converter.convert_html("document.html", sav.MHTMLSaveOptions(), "document.mht")
        #ExEnd:HtmlToMhtmlOne

    def test_html_to_mhtml_with_save_options(self):
        #ExStart:HtmlToMhtmlOpt
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        with open("document1.html", "w") as file:
            file.write("<span>Hello, World!!</span> <a href='document2.html'>click</a>")
        with open("document2.html", "w") as file:
            file.write("<span>Hello, World!!</span>")
        save_path = os.path.join(output_dir, "output-options.mht")
        options = sav.MHTMLSaveOptions()
        options.resource_handling_options.max_handling_depth = 1
        conv.Converter.convert_html("document.html", options, save_path)
        #ExEnd:HtmlToMhtmlOpt

    def test_html_to_pdf_with_save_options(self):
        #ExStart:HtmlToPdfOptions
        output_dir = "output/"
        input_dir = "data/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(input_dir, "nature.html")
        save_path = os.path.join(output_dir, "nature-options.pdf")
        doc = ah.HTMLDocument(document_path)
        options = sav.PdfSaveOptions()
        options.page_setup.any_page.size = dr.Size(680, 500)
        options.page_setup.any_page.margin = dr.Margin(0, 10, 10, 10)
        options.css.media_type.PRINT
        options.horizontal_resolution = dr.Resolution.from_dots_per_inch(50.0)
        options.vertical_resolution = dr.Resolution.from_dots_per_inch(50.0)
        options.background_color = pd.Color.bisque
        options.jpeg_quality = 90
        options.encryption = rpe.PdfEncryptionInfo(
            user_password="user123",
            owner_password="owner123",
            permissions=rpe.PdfPermissions.PRINT_DOCUMENT | rpe.PdfPermissions.EXTRACT_CONTENT,
            encryption_algorithm=rpe.PdfEncryptionAlgorithm.RC4_128
        )
        conv.Converter.convert_html(doc, options, save_path)
        #ExEnd:HtmlToPdfOptions

    def test_html_to_pdf(self):
        #ExStart:HtmlToPdf
        document = ah.HTMLDocument("document.html")
        options = sav.PdfSaveOptions()
        conv.Converter.convert_html(document, options, "output.pdf")
        #ExEnd:HtmlToPdf

    def test_html_to_png_in_one_line(self):
        #ExStart:HtmlToPngOne
        conv.Converter.convert_html("document.html", sav.ImageSaveOptions(), "output.png")
        #ExEnd:HtmlToPngOne

    def test_html_to_png_with_save_options(self):
        #ExStart:HtmlToPngOptions
        output_dir = "output/"
        input_dir = "data/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(input_dir, "banner.html")
        save_path = os.path.join(output_dir, "banner-options-resolution.png")
        document = ah.HTMLDocument(document_path)
        options = sav.ImageSaveOptions()
        options.horizontal_resolution = dr.Resolution.from_dots_per_inch(200.0)
        options.vertical_resolution = dr.Resolution.from_dots_per_inch(200.0)
        conv.Converter.convert_html(document, options, save_path)
        #ExEnd:HtmlToPngOptions

    def test_html_to_xhtml(self):
        #ExStart:HtmlToXhtml
        document = ah.HTMLDocument("document.html")
        options = sav.HTMLSaveOptions()
        options.document_type = sav.HTMLSaveOptions.XHTML
        document.save("output.xhtml", options)
        #ExEnd:HtmlToXhtml

if __name__ == "__main__":
    tests = ConvertHTMLExamples()
    tests.test_flatten_pdf()
    tests.test_html_to_docx_with_save_options()
    tests.test_html_to_docx()
    tests.test_html_to_gif()
    tests.test_html_to_jpg_with_save_options_margins()
    tests.test_html_to_jpg_with_save_options()
    tests.test_html_to_jpg()
    tests.test_html_to_md_feature()
    tests.test_html_to_md_git()
    tests.test_html_to_md_inline()
    tests.test_html_to_md()
    tests.test_html_to_mhtml_in_one_line()
    tests.test_html_to_mhtml_with_save_options()
    tests.test_html_to_pdf_with_save_options()
    tests.test_html_to_pdf()
    tests.test_html_to_png_in_one_line()
    tests.test_html_to_png_with_save_options()
    tests.test_html_to_xhtml()
    print("✅ Files created successfully.")