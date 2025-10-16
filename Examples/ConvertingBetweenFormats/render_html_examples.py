import os
import unittest
import aspose.html as ah
import aspose.html.rendering as rn
import aspose.html.rendering.pdf as rp
import aspose.html.rendering.doc as rd
import aspose.html.rendering.image as ri
import aspose.html.rendering.xps as rx
import aspose.html.drawing as dr
import aspose.html.rendering.pdf.encryption as rpe
import aspose.pydrawing as pd

class RenderHtmlExamplesTests(unittest.TestCase):
    def setUp(self):
        self.output_dir = "output/"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def test_doc_device(self):
        #ExStart:DocDevice
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        save_path = os.path.join(output_dir, "document.doc")
        doc = ah.HTMLDocument("https://docs.aspose.com/html/files/document.html")
        device = rd.DocDevice(save_path)
        doc.render_to(device)
        #ExEnd:DocDevice

    def test_doc_rendering_options(self):
        #ExStart:DocRenderingOptions
        data_dir = "data/"
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(data_dir, "nature.html")
        doc = ah.HTMLDocument(document_path)
        options = rd.DocRenderingOptions()
        options.page_setup.any_page = dr.Page(dr.Size(dr.Length.from_inches(8.0), dr.Length.from_inches(10.0)))
        options.font_embedding_rule = rd.FontEmbeddingRule.FULL
        save_path = os.path.join(output_dir, "nature-options.docx")
        device = rd.DocDevice(options, save_path)
        doc.render_to(device)
        #ExEnd:DocRenderingOptions

    def test_epub_renderer(self):
        #ExStart:EpubRenderer
        data_dir = "data/"
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        epub_path = os.path.join(data_dir, "input.epub")
        save_path = os.path.join(output_dir, "convert-epub-options.docx")
        with open(epub_path, "rb") as stream:
            renderer = rn.EpubRenderer()
            options = rd.DocRenderingOptions()
            options.page_setup.any_page = dr.Page(dr.Size(800, 400))
            device = rd.DocDevice(options, save_path)
            renderer.render(device, stream)
        #ExEnd:EpubRenderer

    def test_html_renderer(self):
        #ExStart:HtmlRenderer
        data_dir = "data/"
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(data_dir, "document.html")
        doc = ah.HTMLDocument(document_path)
        renderer = rn.HtmlRenderer()
        save_path = os.path.join(output_dir, "convert-html-options.pdf")
        options = rp.PdfRenderingOptions()
        options.page_setup.any_page = dr.Page(dr.Size(600, 200))
        options.encryption = rpe.PdfEncryptionInfo(
            user_password="user_pwd",
            owner_password="owner_pwd",
            permissions=rpe.PdfPermissions.PRINT_DOCUMENT,
            encryption_algorithm=rpe.PdfEncryptionAlgorithm.RC4_128
        )
        device = rp.PdfDevice(options, save_path)
        renderer.render(device, doc)
        #ExEnd:HtmlRenderer

    def test_image_device(self):
        #ExStart:ImageDevice
        data_dir = "data/"
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(data_dir, "drawing.html")
        save_path = os.path.join(output_dir, "drawing-output.jpg")
        doc = ah.HTMLDocument(document_path)
        image_options = ri.ImageRenderingOptions(ri.ImageFormat.JPEG)
        device = ri.ImageDevice(image_options, save_path)
        doc.render_to(device)
        #ExEnd:ImageDevice

    def test_image_rendering_options(self):
        #ExStart:ImageRenderingOptions
        data_dir = "data/"
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(data_dir, "html_file.html")
        save_path = os.path.join(output_dir, "document.tiff")
        doc = ah.HTMLDocument(document_path)
        image_options = ri.ImageRenderingOptions(ri.ImageFormat.TIFF)
        image_options.compression = ri.Compression.NONE
        device = ri.ImageDevice(image_options, save_path)
        doc.render_to(device)
        #ExEnd:ImageRenderingOptions

    def test_is_tagged_pdf(self):
        #ExStart:IsTaggedPdf
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        save_path = os.path.join(output_dir, "tagged-document.pdf")
        code = """
            <html>
            <head><title>Tagged PDF Example</title></head>
            <body>
                <h1>Hello, World!</h1>
                <p>This PDF is generated with tagging enabled.</p>
                <ul>
                <li>Accessibility</li>
                <li>Logical structure</li>
                <li>Better content extraction</li>
                </ul>
            </body>
            </html>
            """
        doc = ah.HTMLDocument(code, ".")
        pdf_options = rp.PdfRenderingOptions()
        pdf_options.is_tagged_pdf = True
        device = rp.PdfDevice(pdf_options, save_path)
        doc.render_to(device)
        #ExEnd:IsTaggedPdf

    def test_mhtml_renderer(self):
        #ExStart:MhtmlRenderer
        data_dir = "data/"
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        mhtml_path = os.path.join(data_dir, "document.mht")
        save_path = os.path.join(output_dir, "convert-mhtml-options.pdf")
        with open(mhtml_path, 'rb') as stream:
            renderer = rn.MhtmlRenderer()
            options = rp.PdfRenderingOptions()
            options.page_setup.any_page = dr.Page(dr.Size(800, 400))
            options.background_color = pd.Color.bisque
            device = rp.PdfDevice(options, save_path)
            renderer.render(device, stream)
        #ExEnd:MhtmlRenderer

    def test_page_set_up(self):
        #ExStart:PageSetUp
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        code = """<style>div { page-break-after: always; }</style>
            <div>First Page</div>
            <div>Second Page</div>
            <div>Third Page</div>
            <div>Fourth Page</div>"""
        doc = ah.HTMLDocument(code, ".")
        options = rp.PdfRenderingOptions()
        options.page_setup.set_left_right_page(
            dr.Page(dr.Size(400, 150)),
            dr.Page(dr.Size(400, 50))
        )
        save_path = os.path.join(output_dir, "output-custom-page-size.pdf")
        device = rp.PdfDevice(options, save_path)
        doc.render_to(device)
        #ExEnd:PageSetUp

    def test_pdf_device(self):
        #ExStart:PdfDevice
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        save_path = os.path.join(output_dir, "document.pdf")
        code = "<span>Hello, World!!</span>"
        doc = ah.HTMLDocument(code, ".")
        device = rp.PdfDevice(save_path)
        doc.render_to(device)
        #ExEnd:PdfDevice

    def test_pdf_encryption(self):
        #ExStart:PdfEncryption
        data_dir = "data/"
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(data_dir, "document.html")
        doc = ah.HTMLDocument(document_path)
        renderer = rn.HtmlRenderer()
        save_path = os.path.join(output_dir, "convert-html-to-pdf-with-encryption.pdf")
        options = rp.PdfRenderingOptions()
        options.encryption = rpe.PdfEncryptionInfo(
            user_password="user_pwd",
            owner_password="owner_pwd",
            permissions=rpe.PdfPermissions.PRINT_DOCUMENT,
            encryption_algorithm=rpe.PdfEncryptionAlgorithm.RC4_128
        )
        device = rp.PdfDevice(options, save_path)
        renderer.render(device, doc)
        #ExEnd:PdfEncryption

    def test_render_html_to_pdf_few_lines(self):
        #ExStart:RenderHtmlToPdfFewLines
        doc = ah.HTMLDocument("https://docs.aspose.com/html/files/document.html")
        doc.render_to(rp.PdfDevice("output/document.pdf"))
        #ExEnd:RenderHtmlToPdfFewLines

    def test_svg_renderer(self):
        #ExStart:SvgRenderer
        data_dir = "data/"
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        doc_path = os.path.join(data_dir, "flower.svg")
        save_path = os.path.join(output_dir, "convert-svg-options.pdf")
        doc = ah.dom.svg.SVGDocument(doc_path)
        renderer = rn.SvgRenderer()
        options = rp.PdfRenderingOptions()
        options.page_setup.any_page = dr.Page(dr.Size(600, 200))
        device = rp.PdfDevice(options, save_path)
        renderer.render(device, doc)
        #ExEnd:SvgRenderer

    def test_svg_to_png_renderer(self):
        #ExStart:SvgToPngRenderer
        data_dir = "data/"
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        doc_path = os.path.join(data_dir, "flower.svg")
        save_path = os.path.join(output_dir, "convert-svg-options.png")
        doc = ah.dom.svg.SVGDocument(doc_path)
        renderer = rn.SvgRenderer()
        options = ri.ImageRenderingOptions()
        options.page_setup.any_page = dr.Page(dr.Size(400, 300))
        device = ri.ImageDevice(options, save_path)
        renderer.render(device, doc)
        #ExEnd:SvgToPngRenderer

    def test_use_background_color(self):
        #ExStart:UseBackgroundColor
        data_dir = "data/"
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(data_dir, "drawing.html")
        save_path = os.path.join(output_dir, "drawing-background.pdf")
        doc = ah.HTMLDocument(document_path)
        pdf_options = rp.PdfRenderingOptions()
        pdf_options.background_color = pd.Color.bisque
        device = rp.PdfDevice(pdf_options, save_path)
        doc.render_to(device)
        #ExEnd:UseBackgroundColor

    def test_use_media_type(self):
        #ExStart:UseMediaType
        data_dir = "data/"
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(data_dir, "drawing.html")
        save_path = os.path.join(output_dir, "drawing-media.pdf")
        doc = ah.HTMLDocument(document_path)
        pdf_options = rp.PdfRenderingOptions()
        pdf_options.css.media_type.PRINT
        device = rp.PdfDevice(pdf_options, save_path)
        doc.render_to(device)
        #ExEnd:UseMediaType

    def test_use_resolution(self):
        #ExStart:UseResolution
        data_dir = "data/"
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(data_dir, "drawing.html")
        doc = ah.HTMLDocument(document_path)
        save_path1 = os.path.join(output_dir, "output_resolution_50.png")
        save_path2 = os.path.join(output_dir, "output_resolution_300.png")
        options1 = ri.ImageRenderingOptions(ri.ImageFormat.PNG)
        options1.horizontal_resolution = dr.Resolution.from_dots_per_inch(50.0)
        options1.vertical_resolution = dr.Resolution.from_dots_per_inch(50.0)
        device1 = ri.ImageDevice(options1, save_path1)
        doc.render_to(device1)
        options2 = ri.ImageRenderingOptions(ri.ImageFormat.PNG)
        options2.horizontal_resolution = dr.Resolution.from_dots_per_inch(300.0)
        options2.vertical_resolution = dr.Resolution.from_dots_per_inch(300.0)
        device2 = ri.ImageDevice(options2, save_path2)
        doc.render_to(device2)
        #ExEnd:UseResolution

    def test_use_widest_page_size(self):
        #ExStart:WidestPageSize
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        code = """<style>
            div { page-break-after: always; }
            </style>
            <div style='border: 1px solid red; width: 300px'>First Page</div>
            <div style='border: 1px solid red; width: 500px'>Second Page</div>"""
        doc = ah.HTMLDocument(code, ".")
        options = rp.PdfRenderingOptions()
        options.page_setup.any_page = dr.Page(dr.Size(400, 200))
        options.page_setup.adjust_to_widest_page = True
        save_path = os.path.join(output_dir, "output-widest-page-size.pdf")
        device = rp.PdfDevice(options, save_path)
        doc.render_to(device)
        #ExEnd:WidestPageSize

    def test_xps_device(self):
        #ExStart:XpsDevice
        data_dir = "data/"
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(data_dir, "drawing.html")
        save_path = os.path.join(output_dir, "drawing-output.xps")
        doc = ah.HTMLDocument(document_path)
        xps_options = rx.XpsRenderingOptions()
        device = rx.XpsDevice(xps_options, save_path)
        doc.render_to(device)
        #ExEnd:XpsDevice

    def test_xps_rendering_options(self):
        #ExStart:XpsRenderingOptions
        data_dir = "data/"
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        document_path = os.path.join(data_dir, "document.html")
        doc = ah.HTMLDocument(document_path)
        options = rx.XpsRenderingOptions()
        options.page_setup.any_page = dr.Page(dr.Size(dr.Length.from_inches(5.0), dr.Length.from_inches(2.0)))
        save_path = os.path.join(output_dir, "document-options.xps")
        device = rx.XpsDevice(options, save_path)
        doc.render_to(device)
        #ExEnd:XpsRenderingOptions

if __name__ == "__main__":
    tests = RenderHtmlExamplesTests()
    tests.test_doc_device()
    tests.test_doc_rendering_options()
    tests.test_epub_renderer()
    tests.test_html_renderer()
    tests.test_image_device()
    tests.test_image_rendering_options()
    tests.test_mhtml_renderer()
    tests.test_page_set_up()
    tests.test_pdf_device()
    tests.test_pdf_encryption()
    tests.test_render_html_to_pdf_few_lines()
    tests.test_svg_renderer()
    tests.test_svg_to_png_renderer()
    tests.test_use_background_color()
    tests.test_use_media_type()
    tests.test_use_resolution()
    tests.test_use_widest_page_size()
    tests.test_xps_device()
    tests.test_xps_rendering_options()
    print("✅ All render-html example tests executed successfully.")