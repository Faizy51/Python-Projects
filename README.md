# Python-Projects

I will go ahead and explain how to run each of these.

<h3>1. scramble.py</h3> 
The script takes input from file "input.txt" and scrambles all the words in it.
scrambling is done in a way that all the apostropes are preserved and only the letters are scrambled.
The output is stored into file named "output.txt". You need to create two text files input.txt and output.txt in the same path where program resides.

<h3>2. sele.py </h3>
<p>This script was witten to automate the process of downloading call letter for my interviews. It was a tedious task because
I had to keep checking when it opens and make sure to download it within a minute. 
I made my bot (this script) to do it for me.</br>

Prerequisites - Download cromedriver - https://sites.google.com/a/chromium.org/chromedriver/downloads. Place it in C:\Python27\Scripts. 
You can use the same concepts for a similar work. You can automate any website by changing the URL and HTML tags for elements in the website.
Few steps to follow - </br>
   a. Goto the website of your choice</br>
   b. change the URL in the program to that website</br>
   c. In browser, open your website, open developer tools and find the ids of buttons or text fields you want to interact with</br>
   d. Modify the program accordingly.</br></p>
   
<h3>3. webscrap2.py </h3>

This script was written to scrape the VTU website to fetch my whole class' result in a single console.
This might not work now since the login now requires captcha to be entered. You can still modify and use the script for other websites having no 
captcha.
