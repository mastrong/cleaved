let rounds = {
    'appetizers': 0,
    'entrees': 0,
    'desserts': 0
}

// function checkForSave() {
//     // check for save on local storage
//     if (localStorage.getItem('search_query')) {
//         // request saved search from server
//         let url = 'https://cleaved.azurewebsites.net/api/search' + localStorage.getItem('search_query')
//         fetch(url).then(function (response) {
//             let data = response.json()
//         })
//     } else {
//         localStorage.setItem('search_query', JSON.stringify(search_query));
//     }

function getGroceryList() {

    let container = document.getElementById('groceryList')
    let things = [];

    for (let i of Object.getOwnPropertyNames(appetizers_)) {
        let element = document.getElementById('appetizers_list')
        element.innerHTML += `<li id="${'appetizers'}_${i}" class="${'appetizers'}">${i}</li>`
        things.push(i)
    }

    for (let i of Object.getOwnPropertyNames(entrees_)) {
        let element = document.getElementById('entrees_list')
        element.innerHTML += `<li id="${'entrees'}_${i}" class="${'entrees'}">${i}</li>`
        things.push(i)
    }

    for (let i of Object.getOwnPropertyNames(desserts_)) {
        let element = document.getElementById('desserts_list')
        element.innerHTML += `<li id="${'desserts'}_${i}" class="${'desserts'}">${i}</li>`
        things.push(i)
    }

    things = things.sort()
    console.log(things)

    for (let thing of things) {
        container.innerHTML += `<li>* ${thing}</li>`
    }
}


function getIngredients(category) {

    let elements = document.querySelectorAll(`.${category}`);
    for (let element of elements) {
        element.style.visibility = 'visible';
    }
}


function resetAll() {
    location.reload()
}


window.onload = function () {
    getGroceryList();
}


// Fire effect at bottom https://codepen.io/Mertl/pen/gpzMGV
let canvas = document.getElementById("canvas");
let c = canvas.getContext("2d");
let w = canvas.width = window.innerWidth;
let h = canvas.height = window.innerHeight;

particles = {};
particleIndex = 0;
particleNum = 30;


function particle() {
    this.x = Math.random() * canvas.width;
    this.y = Math.random() * canvas.height / 3 + h * 2 / 3 - 100;
    this.vx = Math.random() * 10 - 5;
    this.vy = Math.random() * 10 - 5;
    particleIndex++;
    particles[particleIndex] = this;
    this.id = particleIndex;
    this.life = 0;
    this.maxLife = Math.random() * 90;
    this.shadeR = Math.floor(Math.random() * 255 + 150) + 50;
    this.shadeG = Math.floor(Math.random() * 150) + 50;
    this.shadeB = 0;
    this.color = 'rgba(' + this.shadeR + ',' + this.shadeG + ',' + this.shadeB + ',' + Math.random() * 0.7 + ')';
    this.size = Math.random() * 3;
}

particle.prototype.draw = function () {
    this.x += this.vx;
    this.y += this.vy;
    if (Math.random() < 0.1) {
        this.vx = Math.random() * 10 - 5;
        this.vy = -2;
    }

    this.life++;
    if (this.life >= this.maxLife) {
        delete particles[this.id];
    }

    c.beginPath();
    c.arc(this.x, this.y, this.size, 0, 2 * Math.PI, false);
    c.fillStyle = this.color;
    c.fill();
};

function drawParticle() {
    c.clearRect(0, 0, w, h);
    for (var i = 0; i < particleNum; i++) {
        new particle();
    }
    for (var i in particles) {
        particles[i].draw();
    }
}


function loop() {

    // window.requestAnimFrame(loop);
    window.requestAnimationFrame(loop);
    drawParticle();
}

loop();

// timer
let duration = 30 * 60 * 1000; // 30 minutes in milliseconds
let endTime;
let timerInterval;
let remainingTime;

function updateTimer() {
    const currentTime = Date.now();
    remainingTime = endTime - currentTime;

    if (remainingTime <= 0) {
        clearInterval(timerInterval);
        document.getElementById('timer').textContent = "Time's up!";
        return;
    }

    const minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);
    // Zero-padding the seconds
    const formattedSeconds = String(seconds).padStart(2, '0');

    document.getElementById('timer').textContent = `${minutes} : ${formattedSeconds}`;
}

function startTimer() {
    const startTime = Date.now();
    endTime = startTime + (remainingTime || duration); // Resume timer if there's remaining time
    updateTimer();
    timerInterval = setInterval(updateTimer, 1000);
}

function stopTimer() {
    clearInterval(timerInterval);
}

function resumeTimer() {
    startTimer(); // Resume is similar to starting the timer
}

function resetTimer() {
    clearInterval(timerInterval);
    document.getElementById('timer').textContent = "30 : 00";
}

resetTimer();