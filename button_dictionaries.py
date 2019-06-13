#dictionaries for button fuctions

#HTML tags for add_html_tag function
html_tags = {"Bold": ["<b>", "</b>"], "Italic": ["<i>", "</i>"], 
			"Underline": ["<u>", "</u>"], "All": ["<b><i><u>", "</b></i></u>"],
			"Bold Underline": ["<b><u>", "</b></u>"], "Bold Italic": ["<b><i>", "</b></i>"]}

#special characters for special characters function 
specialCharDict = {193:"&#193;", 201:"&#201;", 205:"&#205;", 211:"&#211;", 
	218:"&#218;",209: "&#209;", 220: "&#220;", 225: "&#225;", 
	233: "&#233;",237:"&#237;", 243: "&#243;",250:"&#250;", 
	241: "&#241;", 252: "&#252;", 191: "&#191;", 161: "&#161;",
	8220: '"', 8221: '"', 8217: "'"}


#Some Spanish characters are interpreted as a regular letter with the
#accent mark added to them; ex: 'Small latin "o" with acute'
#These are read as a string b/c the letter and the accompanying
#accent mark are read separately, but are printed seemingly together

#	{ 65 769: "&#193;", 69 769:"&#201;",
#	73 769:"&#205;", 79 769:"&#211;", 85 769:"&#218;", 78 771: "&#209;", 
#	85 776: "&#220;", 97 769: "&#225;", 101 769: "&#233;", 105 769:"&#237;", 
#	111 769: "&#243;", 117 769:"&#250;", 110 771: "&#241;", 117 776: "&#252;"}

