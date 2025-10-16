import os
import aspose.html as ah
import aspose.html.net as ahnet
from aspose.html import *

class ExtractDataFromHTMLDocumentsExamples:
    def test_extract_data(self):
        #ExStart:ExtractData
        document = HTMLDocument("https://www.wikipedia.org/")
        elements = document.query_selector_all("h2")
        if elements.length > 0:
            first_heading = elements[0]
            content = first_heading.text_content.strip() if first_heading.text_content else ""
            print("Text of the first heading:")
            print(content)
        else:
            print("No <h1> elements found on the page")
        #ExEnd:ExtractData
        
    def test_extract_icons(self):
        #ExStart:ExtractIcons
        output_dir = "output/icons/"
        os.makedirs(output_dir, exist_ok=True)
        document = ah.HTMLDocument("https://docs.aspose.com/html/python-net/")
        links = document.get_elements_by_tag_name("link")
        icons = [link for link in links if link.get_attribute("rel") == "icon"]
        urls = {icon.get_attribute("href") for icon in icons}
        abs_urls = [ah.Url(url, document.base_uri) for url in urls]
        for url in abs_urls:
            request = ahnet.RequestMessage(url)
            response = document.context.network.send(request)
            if response.is_success:
                file_path = os.path.join(output_dir, os.path.basename(url.pathname))
                with open(file_path, 'wb') as file:
                    file.write(response.content.read_as_byte_array())
        #ExEnd:ExtractIcons
        
    def test_extract_images_from_website(self):
        #ExStart:ExtractImagesFromWebsite
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        with ah.HTMLDocument("https://docs.aspose.com/svg/net/drawing-basics/svg-color/") as doc:
            images = doc.get_elements_by_tag_name("img")
            urls = set(img.get_attribute("src") for img in images)
            abs_urls = [ah.Url(url, doc.base_uri) for url in urls]
            for url in abs_urls:
                request = ahnet.RequestMessage(url)
                response = doc.context.network.send(request)
                if response.is_success:
                    file_name = os.path.basename(url.pathname)
                    with open(os.path.join(output_dir, file_name), "wb") as f:
                        f.write(response.content.read_as_byte_array())
        #ExEnd:ExtractImagesFromWebsite
        
    def test_extract_svg_inline(self):
        #ExStart:ExtractSvgInline
        output_dir = "output/svg/"
        os.makedirs(output_dir, exist_ok=True)
        with ah.HTMLDocument("https://docs.aspose.com/svg/net/drawing-basics/svg-shapes/") as document:
            images = document.get_elements_by_tag_name("svg")
            for i, image in enumerate(images):
                with open(os.path.join(output_dir, f"{i}.svg"), 'w', encoding='utf-8') as file:
                    file.write(image.outer_html)
        #ExEnd:ExtractSvgInline
        
    def test_extract_svg(self):
        #ExStart:ExtractSvg
        output_dir = "output/svg/"
        os.makedirs(output_dir, exist_ok=True)
        document = ah.HTMLDocument("https://products.aspose.com/html/python-net/")
        images = document.get_elements_by_tag_name("img")
        urls = set(img.get_attribute("src") for img in images)
        svg_urls = [url for url in urls if url.endswith(".svg")]
        abs_urls = [ah.Url(url, document.base_uri) for url in svg_urls]
        for url in abs_urls:
            request = ahnet.RequestMessage(url.href)
            response = document.context.network.send(request)
            if response.is_success:
                file_path = os.path.join(output_dir, os.path.basename(url.pathname))
                with open(file_path, "wb") as f:
                    f.write(response.content.read_as_byte_array())
        #ExEnd:ExtractSvg
        
    def test_extract_tables(self):
        #ExStart:ExtractTables
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        with ah.HTMLDocument("https://docs.aspose.com/html/net/edit-html-document/") as doc:
            tables = doc.get_elements_by_tag_name("table")
            if tables.length > 0:
                for i, table in enumerate(tables):
                    file_name = f"table{i}.htm"
                    file_path = os.path.join(output_dir, file_name)
                    new_doc = ah.HTMLDocument(table.outer_html, file_path)
                    new_doc.save(file_path)
            else:
                print("No tables found in the document.")
        #ExEnd:ExtractTables
        
    def test_navigate_html(self):
        #ExStart:NavigateHtml
        html_code = "<span>Hello,</span> <span>World!</span>"
        with ah.HTMLDocument(html_code, ".") as document:
            element = document.body.first_child
            print(element.text_content)
            element = element.next_sibling
            print(element.text_content)
            element = element.next_sibling
            print(element.text_content)
        #ExEnd:NavigateHtml
        
    def test_save_file_from_url(self):
        #ExStart:SaveFileFromUrl
        output_dir = "output/"
        os.makedirs(output_dir, exist_ok=True)
        doc = ah.HTMLDocument()
        url = ah.Url("https://docs.aspose.com/html/images/handlers/message-handlers.png")
        request = ahnet.RequestMessage(url)
        response = doc.context.network.send(request)
        if response.is_success:
            file_path = os.path.join(output_dir, os.path.basename(url.pathname))
            with open(file_path, "wb") as file:
                file.write(response.content.read_as_byte_array())
        #ExEnd:SaveFileFromUrl
        
if __name__ == "__main__":
    tests = ExtractDataFromHTMLDocumentsExamples()
    tests.test_extract_data()
    tests.test_extract_icons()
    tests.test_extract_images_from_website()
    tests.test_extract_svg_inline()
    tests.test_extract_svg()
    tests.test_extract_tables()
    tests.test_navigate_html()
    tests.test_save_file_from_url()
    print("✅ Files created successfully.")