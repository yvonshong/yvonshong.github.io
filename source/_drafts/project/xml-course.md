---
title: XML Course Responsive Website about xml/python/markdown
date: 2016-04-01 19:05:39
toc: true
---
To write the design of DTD, Schema and some codes about XML in the course of XML Technoligy of SEU.
More detaily, there are
- frame: the design of website
- xml: The instance and data of our XML.
- DTD: The Document Type Definition of our xml data.
- XSD: The Schema of the xml(the .xsd file).
- XSL: The info of our team using XSL/XSLT+Xpath.
- MD: Our log/preblem **html website tranformed from markdown**.
- Py: Try to input the xml data by **spider** from douban.
- FO: Transform the data to pdf or text by XSL-FO technology.
- SVG: A picture (Taiji from China) made by SVG.
- XQuery: Query the data in the XML file.
- SAX: Query the data in the XML file.
- DOM: Query the data in the XML file.

[The Project Site http://www.yvonshong.com/xml](http://www.yvonshong.com/xml)

<!-- more -->

### Group 8

## Update log

Mar 3rd: 

		the_module_of_movies.jpg --- the design of the structure of our XML
      
    	the_module_of_movies.xml
Mar 7th:

		movies.dtd --- the document type definition of movies.

		the_module_of_movies.xml --- reconstruct the xml, add element:score and add attribute:sex of element:star

Mar 8th：

		correct some error of the quotation marks in ddt and xml.
Mar 9th:
	
		movies.xsd --- the schema of the xml.
		the_module_of_movies.xml --- refresh the referrence definition of the schema.
		the_module_of_movies.xml --- reconstruct the xml, add element:score and add attribute:sex of element:star
Mar 19th:

        index_main.xml index_main.xsl --- complete the xml file using XSL/XSLT+Xpath
        xml/xml.css --- in fact, we have complete the css to highlight the xml code long long ago.[HERE](http://yvonshong.gityhub.io/xml.html)
        
Mar 26th:
        change the website for log and problem and summary, replaced by the html trasnformed from README markdown file. 
        try to input the xml data by spider from douban.
        
Mar 27th:
        code for the XSL-FO and find the hardness of the NavigatableString in bs4 of spider.
  

Mar 28th:
		github from han chang
		githubgithub test from yvon

## Problem:

- my xsd and dtd are on the github.com. how can I refer them in xml?
- I will transfer this web to https://coding.net/u/yvonshong/p/xml_course/git to check the dtd and schema.
- in order to modufy the web of next.html to show our plan to sync this README.md, we will use the Pandoc to try to transfer the markdown file to html file.
- rebuild the xslt to process the movie.xml 

## Summary:

- iframe
iframe is hard to be adaptive and to modularize. and there are some errors of link jumping. nestification and modularization are hard by html.
- sync
    Git plus OneDrive are convenient for two computer which are used by the only one person.
    the editor for web like sublime text, vs code. I find the vs code integrate the Git.
- tools
    the online xml - xsl-fo -pdf transform  http://www.utilities-online.info/foprender/#
