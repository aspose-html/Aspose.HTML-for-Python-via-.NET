import os
import unittest
import aspose.html.dom.svg as ahsvg
import aspose.html.converters as conv
import aspose.html.saving as sav
import aspose.html.rendering.image as rim
import aspose.html.drawing as dr

class SvgExamplesTests(unittest.TestCase):

    def test_convert_svg_to_jpg(self):
        #ExStart:ConvertSvgToJpg
        output_dir = "output/"
        input_dir = "data/"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        document_path = os.path.join(input_dir, "tulips.svg")
        save_path = os.path.join(output_dir, "svg-to-image.jpg")
        document = ahsvg.SVGDocument(document_path)
        options = sav.ImageSaveOptions(rim.ImageFormat.JPEG)
        options.horizontal_resolution = dr.Resolution.from_dots_per_inch(200.0)
        options.vertical_resolution = dr.Resolution.from_dots_per_inch(200.0)
        conv.Converter.convert_svg(document, options, save_path)
        #ExEnd:ConvertSvgToJpg

    def test_convert_svg_to_pdf_with_save_options(self):
        #ExStart:ConvertSvgToPdfOpt
        output_dir = "output/"
        input_dir = "data/"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        document_path = os.path.join(input_dir, "flower.svg")
        save_path = os.path.join(output_dir, "svg-to-pdf.pdf")
        document = ahsvg.SVGDocument(document_path)
        options = sav.PdfSaveOptions()
        options.page_setup.any_page = dr.Page(dr.Size(600, 500), dr.Margin(20, 20, 10, 10))
        options.css.media_type.PRINT
        options.jpeg_quality = 80
        options.is_tagged_pdf = True
        conv.Converter.convert_svg(document, options, save_path)
        #ExEnd:ConvertSvgToPdfOpt

    def test_convert_svg_to_pdf(self):
        #ExStart:ConvertSvgToPdf
        output_dir = "output/"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        save_path = os.path.join(output_dir, "circles.pdf")
        svg_code = """
<svg xmlns="http://www.w3.org/2000/svg">
    <circle id="base" cx="100" cy="100" r="80" fill="teal" stroke="salmon" stroke-width="10" />
    <g> 
        <use href="#base" transform="translate(120, 10) scale(0.9)" />
        <use href="#base" transform="translate(240, 20) scale(0.8)" />
        <use href="#base" transform="translate(360, 30) scale(0.7)" />
        <use href="#base" transform="translate(480, 40) scale(0.6)" />
        <use href="#base" transform="translate(600, 50) scale(0.5)" />
    </g>
</svg>
"""
        options = sav.PdfSaveOptions()
        conv.Converter.convert_svg(svg_code, ".", options, save_path)
        #ExEnd:ConvertSvgToPdf

    def test_svg_to_jpg_from_code(self):
        #ExStart:SvgToJpgCode
        output_dir = "output/"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        save_path = os.path.join(output_dir, "circle.jpg")
        svg_code = """<svg xmlns="http://www.w3.org/2000/svg">
            <circle cx="100" cy="100" r="70" fill="teal" stroke="pink" stroke-width="10" />
            </svg>"""
        options = sav.ImageSaveOptions(rim.ImageFormat.JPEG)
        conv.Converter.convert_svg(svg_code, ".", options, save_path)
        #ExEnd:SvgToJpgCode

    def test_svg_to_jpg(self):
        #ExStart:SvgToJpg
        document = ahsvg.SVGDocument("flower.svg")
        options = sav.ImageSaveOptions(rim.ImageFormat.JPEG)
        conv.Converter.convert_svg(document, options, "output.jpeg")
        #ExEnd:SvgToJpg

    def test_svg_to_pdf(self):
        #ExStart:SvgToPdf
        document = ahsvg.SVGDocument("flower.svg")
        options = sav.PdfSaveOptions()
        conv.Converter.convert_svg(document, options, "output.pdf")
        #ExEnd:SvgToPdf

    def test_svg_to_png_with_save_options(self):
        #ExStart:SvgToPngOpt
        output_dir = "output/"
        input_dir = "data/"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        document_path = os.path.join(input_dir, "tulips.svg")
        save_path = os.path.join(output_dir, "tulips.png")
        document = ahsvg.SVGDocument(document_path)
        options = sav.ImageSaveOptions()
        options.page_setup.first_page = dr.Page(dr.Size(500, 500), dr.Margin(10, 10, 10, 10))
        options.css.media_type.PRINT
        conv.Converter.convert_svg(document, options, save_path)
        #ExEnd:SvgToPngOpt

    def test_svg_to_png(self):
        #ExStart:SvgToPng
        output_dir = "output/"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        save_path = os.path.join(output_dir, "circle.png")
        svg_code = """<svg xmlns="http://www.w3.org/2000/svg">
<circle cx="100" cy="100" r="60" fill="teal" stroke="salmon" stroke-width="10" />
</svg>"""
        options = sav.ImageSaveOptions()
        conv.Converter.convert_svg(svg_code, ".", options, save_path)
        #ExEnd:SvgToPng

if __name__ == "__main__":
    tests = SvgExamplesTests()
    tests.test_convert_svg_to_jpg()
    tests.test_convert_svg_to_pdf_with_save_options()
    tests.test_convert_svg_to_pdf()
    tests.test_svg_to_jpg_from_code()
    tests.test_svg_to_jpg()
    tests.test_svg_to_pdf()
    tests.test_svg_to_png_with_save_options()
    tests.test_svg_to_png()
    print("✅ Tests executed successfully.")