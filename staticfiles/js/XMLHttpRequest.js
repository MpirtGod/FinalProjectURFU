var xhr = new XMLHttpRequest();
xhr.open("GET", 'https://api.hh.ru/vacancies?text=backend&search_field=name&period=1', false);
xhr.send();
