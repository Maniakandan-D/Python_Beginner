import webbrowser

#webbrowser.open("https://www.python.org", new=1)  # new window  default browser  open
#help(webbrowser)
chrome = webbrowser.get(using="google-chrome $")
chrome.open_new("https://www.python.org")
