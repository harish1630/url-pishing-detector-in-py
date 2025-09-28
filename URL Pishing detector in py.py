import re

def is_phishing_url(url):
    suspicious = []

    
    if len(url) > 75:
        suspicious.append("URL is too long")

    
    if "@" in url:
        suspicious.append("Contains '@' symbol (possible redirection)")

    
    ip_pattern = re.compile(r"(\d{1,3}\.){3}\d{1,3}")
    if ip_pattern.search(url):
        suspicious.append("Uses IP address instead of domain")

    
    keywords = ["login", "secure", "bank", "verify", "account", "update", "free", "winner"]
    for word in keywords:
        if word in url.lower():
            suspicious.append(f"Contains suspicious keyword: {word}")

    
    if suspicious:
        return "Phishing Suspected!", suspicious
    else:
        return "URL looks safe", []
    urls = [
    "http://example.com/login/verify",
    "http://192.168.0.1/securebank",
    "http://google.com",
    "http://free-winner-prize.com"
]
    for url in urls:
        result, issues = is_phishing_url(url)
        print(f"\nURL: {url}")
        print("Result:", result)
    for issue in issues:
        print(" -", issue)
    


