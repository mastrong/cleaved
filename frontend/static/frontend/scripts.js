let ingredients = {
    appetizers: [],
    entrees: [],
    desserts: []
}


async function getIngredients(category) {
    clearIngredients(category)

    let url = `${window.location.href}api/${category}/`;
    let response = await fetch(url);
    let data = await response.json();
    let iterator = data.values();

    for (let value of iterator) {
        ingredients[category].push(value.name)
    }

    setIngredients(category)
}

function setIngredients(category) {
    let element = document.getElementById(category + '_list')
    let list = ingredients[category]

    for (let ingredient of list) {
        element.innerHTML += `<li id="${category}_${ingredient}" class="${category}">${ingredient}</li>`
    }
}

function clearIngredients(category) {
    ingredients[category] = []

    let elements = document.querySelectorAll(`.${category}`);

    for (let element of elements) {
        document.getElementById(element.id).remove()
    }
}

function resetAll() {
    location.reload()
}

// function addPlayers() {
//
// }