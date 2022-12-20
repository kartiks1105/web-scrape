import re
import requests
import numpy as np


email_regex= "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
url = requests.get("https://w05.international.gc.ca/Protocol-Protocole/Heads-Chefs.aspx?lang=eng&_ga=2.134884785.1101894305.1669347188-940224754.1669347188")
html_text = url.text
emails = re.findall(email_regex, html_text)


np.savetxt("emails.csv", emails, delimiter =", ", fmt ='% s')