
const sendRequest = (method, url) => {

    const promise = new Promise((resolve, reject) => {

        const xhr = new XMLHttpRequest();
        xhr.open(method, url);

        xhr.onload = function () {
            resolve(xhr.response);
        }

        xhr.responseType = 'json';

        xhr.send();

    });
    return promise;
}

function createVacancy (id, name, employer_name, salary, area_name, published_at) {

    let newVacancy = document.createElement('tr');
    newVacancy.className = 'vac-item';
    newVacancy.id = id;

    let vacancyName = document.createElement('td');
    vacancyName.className = 'vac-name';
    vacancyName.innerHTML = name;
    vacancyName.className = 'year'

    let vacancyEmployer_name = document.createElement('td');
    vacancyEmployer_name.className = 'vac-employer_name';
    vacancyEmployer_name.innerHTML = employer_name;

    let vacancySalary = document.createElement('td');
    vacancySalary.className = 'vac-salary';
    vacancySalary.innerHTML = salary;

    let vacancyArea_name = document.createElement('td');
    vacancyArea_name.className = 'vac-area_name';
    vacancyArea_name.innerHTML = area_name;

    let vacancyPublished_at = document.createElement('td');
    vacancyPublished_at.className = 'vac-published_at';
    vacancyPublished_at.innerHTML = published_at;

    newVacancy.appendChild(vacancyName);
    newVacancy.appendChild(vacancyEmployer_name);
    newVacancy.appendChild(vacancySalary);
    newVacancy.appendChild(vacancyArea_name);
    newVacancy.appendChild(vacancyPublished_at);

    document.getElementById('lastvac_table').appendChild(newVacancy);
}


sendRequest('GET', 'https://api.hh.ru/vacancies?text=backend&only_with_salary=true&search_field=name&period=2&order_by=publication_time').then(data => {
    for (let i = 0; i < 10; i++) {
        let item = data.items[i];
        createVacancy(item.id, item.name.slice(0 ,100), item.employer.name, `${item.salary.from} - ${item.salary.to} (${item.salary.currency})`.replace('null -', '').replace('- null', ''), item.area.name, item.published_at);
    }
})