import os
import aspose.html as ah
import aspose.html.rendering.pdf as rp

class EditHTMLExamples:

    def test_edit_html_dom(self):
        #ExStart:EditHTMLDom
        output_dir = "output/"
        output_path = os.path.join(output_dir, "edit-document-tree.html")
        os.makedirs(output_dir, exist_ok=True)
        document = ah.HTMLDocument()
        body = document.body
        p = document.create_element("p")
        p.set_attribute("id", "my-paragraph")
        text = document.create_text_node("The Aspose.Html.Dom namespace provides an API for representing and interfacing with HTML, XML, or SVG documents.")
        p.append_child(text)
        body.append_child(p)
        document.save(output_path)
        #ExEnd:EditHTMLDom

    def test_edit_html(self):
        #ExStart:EditHTML
        output_dir = "output/"
        save_path = os.path.join(output_dir, "edit-document.html")
        os.makedirs(output_dir, exist_ok=True)
        document = ah.HTMLDocument()
        style = document.create_element("style")
        style.text_content = ".col { color: teal }"
        head = document.get_elements_by_tag_name("head")[0]
        head.append_child(style)
        p = document.create_element("p")
        p.class_name = "col"
        text = document.create_text_node("Edit HTML document")
        p.append_child(text)
        document.body.append_child(p)
        document.save(save_path)
        #ExEnd:EditHTML

    def test_edit_inline_css(self):
        #ExStart:InlineCSS
        content = "<p>Edit inline CSS using Aspose.HTML for Python via .NET</p>"
        document = ah.HTMLDocument(content, ".")
        paragraph = document.get_elements_by_tag_name("p")[0]
        paragraph.set_attribute("style", "font-size: 150%; font-family: arial; color: teal")
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        html_path = os.path.join(output_dir, "edit-inline-css.html")
        document.save(html_path)
        pdf_path = os.path.join(output_dir, "edit-inline-css.pdf")
        with rp.PdfDevice(pdf_path) as device:
            document.render_to(device)
        #ExEnd:InlineCSS

    def test_use_inner_html(self):
        #ExStart:InnerHTML
        document = ah.HTMLDocument()
        print(document.document_element.outer_html)
        document.body.inner_html = "<p>HTML is the standard markup language for Web pages.</p>"
        p = document.get_elements_by_tag_name("p")[0]
        print(p.inner_html)
        print(document.document_element.outer_html)
        #ExEnd:InnerHTML

    def test_edit_internal_css(self):
        #ExStart:InternalCSS
        content = "<div><h1>Internal CSS</h1><p>An internal CSS is used to define a style for a single HTML page</p></div>"
        document = ah.HTMLDocument(content, ".")
        style = document.create_element("style")
        style.text_content = (
            ".frame1 { margin-top:50px; margin-left:50px; padding:25px; width:360px; height:90px; "
            "background-color:#82011a; font-family:arial; color:#fff5ee;} \r\n"
            ".frame2 { margin-top:-70px; margin-left:160px; text-align:center; padding:20px; width:360px; "
            "height:100px; background-color:#ebd2d7;}"
        )
        head = document.get_elements_by_tag_name("head")[0]
        head.append_child(style)
        header = document.get_elements_by_tag_name("h1")[0]
        header.class_name = "frame1"
        header.set_attribute("style", "font-size: 200%; text-align: center;")
        paragraph = document.get_elements_by_tag_name("p")[0]
        paragraph.class_name = "frame2"
        paragraph.set_attribute("style", "color: #434343; font-size: 150%; font-family: verdana;")
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        html_path = os.path.join(output_dir, "edit-internal-css.html")
        document.save(html_path)
        pdf_path = os.path.join(output_dir, "edit-internal-css.pdf")
        with rp.PdfDevice(pdf_path) as device:
            document.render_to(device)
        #ExEnd:InternalCSS

if __name__ == "__main__":
    tests = EditHTMLExamples()
    tests.test_edit_html_dom()
    tests.test_edit_html()
    tests.test_edit_inline_css()
    tests.test_use_inner_html()
    tests.test_edit_internal_css()
    print("✅ Files created successfully.")